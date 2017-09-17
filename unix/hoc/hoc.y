%{
#include <stdio.h>
#include <math.h>
#define YYSTYPE double

int yylex();
void yyerror();
%}

%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left UNARYMINUS UNARYPLUS
%%

list: /* nothing */
    | list '\n'
    | list expr '\n' { printf("\t%.8g\n", $2); }
    ;
expr: NUMBER        { $$ = $1; }
    | '-' expr %prec UNARYMINUS { $$ = -$2; }
    | '+' expr %prec UNARYPLUS { $$ = $2; }
    | expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr { $$ = $1 / $3; }
    | expr '%' expr { $$ = fmod($1 , $3); }
    | '(' expr ')'  { $$ = $2; }
    ;
%%

#include <stdio.h>
#include <ctype.h>

char *progname;

int lineno = 1;

int main(int argc, char **argv) {
    if (argc > 0) progname = argv[0];
    yyparse();
}

int yylex() {
    int c;

    while ((c = getchar()) == ' ' || c == '\t');

    if (c == EOF) return 0;

    if (c == '.' || isdigit(c)) {
        ungetc(c, stdin);
        scanf("%lf", &yylval);
        return NUMBER;
    }
    
    if (c == '\n') lineno++;
    return c;
}

void warning(char *s, char *t) {
    fprintf(stderr, "%s: %s", progname, s);
    if (t) fprintf(stderr, " %s", t);
    fprintf(stderr, " near line %d\n", lineno);
}

void yyerror(char *s) {
    warning(s, NULL);
}

