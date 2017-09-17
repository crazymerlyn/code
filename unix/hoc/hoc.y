%{
#include "hoc.h"
#include <stdio.h>
#include <math.h>
#include <setjmp.h>
extern double Pow(double a, double b);
int yylex();
void yyerror();
void init();
void execerror(char *s, char *t);
%}
%union {           /* stack type */
    double val;   /* actual value */
    Symbol *sym; /* symbol table pointer */
}
%token <val> NUMBER
%token <sym> VAR BLTIN UNDEF
%type <val> expr assign
%right '='
%left '+' '-'
%left '*' '/' '%'
%left UNARYMINUS UNARYPLUS
%right '^'
%%

list: /* nothing */
    | list '\n'
    | list expr '\n' { printf("\t%.8g\n", $2); }
    | list assign '\n' 
    | list expr ';' { printf("\t%.8g\n", $2); }
    | list error '\n' { yyerrok; }
    ;
assign: VAR '=' expr { $$ = $1->u.val = $3; $1->type = VAR; }
      ;
expr: NUMBER        { $$ = $1; }
    | VAR           { if ($1->type == UNDEF)
                        execerror("undefined variable", $1->name);
                      $$ = $1->u.val; }
    | assign
    | BLTIN '(' expr ')' { $$ = ($1->u.ptr)($3); }
    | '-' expr %prec UNARYMINUS { $$ = -$2; }
    | '+' expr %prec UNARYPLUS { $$ = $2; }
    | expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { $$ = $1 / $3; }
    | expr '%' expr { $$ = fmod($1 , $3); }
    | expr '^' expr { $$ = Pow($1, $3); }
    | '(' expr ')'  { $$ = $2; }
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
    yyparse();
}

int yylex() {
    int c;

    while ((c = getchar()) == ' ' || c == '\t');

    if (c == EOF) return 0;

    if (c == '.' || isdigit(c)) {
        ungetc(c, stdin);
        scanf("%lf", &yylval.val);
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

