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
%token <sym> NUMBER VAR BLTIN UNDEF PRINT WHILE IF ELSE
%type <inst> stmt expr assign stmtlist cond while if end
%right '='
%left OR
%left AND
%left GT GE LT LE EQ NE
%left '+' '-'
%left '*' '/' '%'
%left UNARYMINUS UNARYPLUS NOT
%right '^'
%%

list: /* nothing */
    | list '\n'
    | list expr '\n' { code2(print, STOP); return 1; }
    | list stmt '\n' { code(STOP); return 1; }
    | list assign '\n' { code2((Inst)pop, STOP); return 1; }
    | list error '\n' { yyerrok; }
    ;
assign: VAR '=' expr { $$ = $3; code3(varpush, (Inst)$1, assign); }
      ;
stmt: expr          { code((Inst)pop); }
    | PRINT expr    { code(prexpr); $$ = $2; }
    | while cond stmt end {
                ($1)[1] = (Inst)$3;   /* Body of loop */
                ($1)[2] = (Inst)$4; } /* End, If cond fails */
    | if cond stmt end {
                ($1)[1] = (Inst)$3;
                ($1)[3] = (Inst)$4; }
    | if cond stmt end ELSE stmt end {
                ($1)[1] = (Inst)$3;
                ($1)[2] = (Inst)$6;
                ($1)[3] = (Inst)$7; }
    | '{' stmtlist '}' { $$ = $2; }
    ;
cond: '(' expr ')' { code(STOP); $$ = $2; }
    ;
while: WHILE { $$ = code(whilecode); code2(STOP, STOP); }
     ;
if:    IF { $$ = code(ifcode); code3(STOP, STOP, STOP); }
     ;
end:   /* nothing */ { code(STOP); $$ = progp; }
   ;
stmtlist: /* nothing */ { $$ = progp; }
        | stmtlist '\n'
        | stmtlist stmt
        ;
expr: NUMBER        { $$ = code(constpush); code((Inst)$1); }
    | VAR           { $$ = code(varpush); code2((Inst)$1, eval); }
    | assign
    | BLTIN '(' expr ')' { $$ = $3; code2(builtin, (Inst)$1->u.ptr); }
    | '(' expr ')'  { $$ = $2; }
    | '-' expr %prec UNARYMINUS { $$ = $2; code(negate); }
    | '+' expr %prec UNARYPLUS { $$ = $2; }
    | expr '+' expr { code(add); }
    | expr '-' expr { code(sub); }
    | expr '*' expr { code(mul); }
    | expr '/' expr { code(division); }
    | expr '%' expr { code(mod); }
    | expr '^' expr { code(power); }
    | expr GT expr  { code(gt); }
    | expr GE expr  { code(ge); }
    | expr LT expr  { code(lt); }
    | expr LE expr  { code(le); }
    | expr EQ expr  { code(eq); }
    | expr NE expr  { code(ne); }
    | expr AND expr { code(and); }
    | expr OR expr  { code(or); }
    | NOT expr      { $$ = $2; code(not); }
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

int follow(int expect, int ifyes, int ifno) {
    int c = getchar();
    if (c == expect) return ifyes;
    ungetc(c, stdin);
    return ifno;
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
    switch(c) {
    case '>': return follow('=', GE, GT);
    case '<': return follow('=', LE, LT);
    case '=': return follow('=', EQ, '=');
    case '!': return follow('=', NE, NOT);
    case '|': return follow('|', OR, '|');
    case '&': return follow('&', AND, '&');
    }
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

