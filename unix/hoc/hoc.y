%{
#include "hoc.h"
#include <stdio.h>
#include <math.h>
#include <setjmp.h>
extern double Pow(double a, double b);
#define code2(c1, c2) do { code(c1); code(c2); } while (0);
#define code3(c1, c2, c3) do { code(c1); code(c2); code(c3); } while (0);
int yylex();
void yyerror();
void init();
void execerror(char *s, char *t);
%}
%union {           /* stack type */
    Symbol *sym; /* symbol table pointer */
    Inst *inst; /* machine instruction */
}
%token <sym> NUMBER VAR BLTIN UNDEF
%type <val> expr assign
%right '='
%left '+' '-'
%left '*' '/' '%'
%left UNARYMINUS UNARYPLUS
%right '^'
%%

list: /* nothing */
    | list '\n'
    | list expr '\n' { code2(print, STOP); return 1; }
    | list assign '\n' { code2((Inst)pop, STOP); return 1; }
    | list error '\n' { yyerrok; }
    ;
assign: VAR '=' expr { code3(varpush, (Inst)$1, assign); }
      ;
expr: NUMBER        { code2(constpush, (Inst)$1); }
    | VAR           { code3(varpush, (Inst)$1, eval); }
    | assign
    | BLTIN '(' expr ')' { code2(builtin, (Inst)$1->u.ptr); }
    | '(' expr ')'  {}
    | '-' expr %prec UNARYMINUS { code(negate); }
    | '+' expr %prec UNARYPLUS { }
    | expr '+' expr { code(add); }
    | expr '-' expr { code(sub); }
    | expr '*' expr { code(mul); }
    | expr '/' expr { code(division); }
    | expr '%' expr { code(mod); }
    | expr '^' expr { code(power); }
    ;
%%

#include <ctype.h>

char *progname;
jmp_buf begin;

int lineno = 1;

int main(int argc, char **argv) {
    if (argc > 0) progname = argv[0];
    init();
    setjmp(begin);
    for(initcode(); yyparse(); initcode()) {
        execute(prog);
    }
}

int yylex() {
    int c;

    while ((c = getchar()) == ' ' || c == '\t');

    if (c == EOF) return 0;

    if (c == '.' || isdigit(c)) {
        double d;
        ungetc(c, stdin);
        scanf("%lf", &d);
        yylval.sym = install("", NUMBER, d);
        return NUMBER;
    }

    if (isalpha(c)) {
        Symbol *s;
        char sbuf[100];
        char *p = sbuf;
        for (p = sbuf; c != EOF && isalnum(c); c = getchar(), p++) {
            *p = c;
        }
        ungetc(c, stdin);
        
        *p = '\0';
        if ((s = lookup(sbuf)) == NULL) {
            s = install(sbuf, UNDEF, 0.0);
        }
        yylval.sym = s;

        return s->type == UNDEF ? VAR : s->type;
    }
    
    if (c == '\n') lineno++;
    return c;
}

void warning(char *s, char *t) {
    fprintf(stderr, "%s: %s", progname, s);
    if (t) fprintf(stderr, " %s", t);
    fprintf(stderr, " near line %d\n", lineno);
}

void execerror(char *s, char *t) {
    warning(s, t);
    longjmp(begin, 0);
}

void yyerror(char *s) {
    warning(s, NULL);
}

