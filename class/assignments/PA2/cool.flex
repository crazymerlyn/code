/*
 *  The scanner definition for COOL.
 */

/*
 *  Stuff enclosed in %{ %} in the first section is copied verbatim to the
 *  output, so headers and global definitions are placed here to be visible
 * to the code in the file.  Don't remove anything that was here initially
 */
%{
#include <cool-parse.h>
#include <stringtab.h>
#include <utilities.h>

/* The compiler assumes these identifiers. */
#define yylval cool_yylval
#define yylex  cool_yylex

/* Max size of string constants */
#define MAX_STR_CONST 1025
#define YY_NO_UNPUT   /* keep g++ happy */

extern FILE *fin; /* we read from this file */

/* define YY_INPUT so we read from the FILE fin:
 * This change makes it possible to use this scanner in
 * the Cool compiler.
 */
#undef YY_INPUT
#define YY_INPUT(buf,result,max_size) \
	if ( (result = fread( (char*)buf, sizeof(char), max_size, fin)) < 0) \
		YY_FATAL_ERROR( "read() in flex scanner failed");

char string_buf[MAX_STR_CONST]; /* to assemble string constants */
char *string_buf_ptr;

extern int curr_lineno;
extern int verbose_flag;

extern YYSTYPE cool_yylval;

/*
 *  Add Your own definitions here
 */

IdTable identifiers;
IntTable integers;
StrTable strings;

int is_keyword(char *token, int len);
int keywords[] = {CLASS, ELSE, IF, FI, IN, INHERITS, LET, LOOP, POOL, THEN, WHILE, CASE,
                  ESAC, OF, NEW, ISVOID, NOT};
int comment_level = 0;
bool contains_escaped_null;
bool null_in_string;

%}

/*
 * Define names for regular expressions here.
 */

DARROW          =>
ASSIGN          <-
LE              <=
IDENT           [a-zA-Z][a-zA-Z0-9_]*
INTEGER         [0-9]+
WHITESPACE      [ \t\f\015\013]+
NEWLINE         \n
COMMENT_START   "(*"
COMMENT_END     "*)"
LCOMMENT_START  "--"
STRING_START    \"
STRING_END      \"
TRUE            t[rR][uU][eE]
FALSE           f[aA][lL][sS][eE]

%START COMMENT LINECOMMENT STRING

%%

 /*
  *  Nested comments
  */


 /*
  *  The multiple-character operators.
  */
<COMMENT>[^*\n(]*   {}
<COMMENT>{COMMENT_START} { comment_level += 1; }
<COMMENT>"*"/[^)]    {}
<COMMENT>"("/[^*]    {}
<COMMENT>{COMMENT_END} {
    comment_level -= 1;
    if (comment_level == 0) BEGIN 0;
}
<COMMENT><<EOF>>       {
    cool_yylval.error_msg = "EOF in comment";
    BEGIN 0;
    return (ERROR);
}

<LINECOMMENT>[^\n]*     {}
<LINECOMMENT>\n         { curr_lineno += 1; BEGIN 0; }

<STRING>{STRING_END} {
    BEGIN 0;
    if (contains_escaped_null) {
        cool_yylval.error_msg = "String contains escaped null character.";
        return ERROR;
    }
    if (null_in_string) {
        cool_yylval.error_msg = "String contains null character.";
        return ERROR;
    }
    if ((string_buf_ptr - string_buf) < MAX_STR_CONST) {
        cool_yylval.symbol = strings.add_string(string_buf, string_buf_ptr - string_buf);
        return STR_CONST;
    } else {
        cool_yylval.error_msg = "String constant too long";
        return ERROR;
    }
}
<STRING>[^\\\"\n\0] {
    if ((string_buf_ptr - string_buf) < MAX_STR_CONST) {
        *string_buf_ptr = yytext[yyleng-1];
        string_buf_ptr++;
    }
}
<STRING>\0 {
    null_in_string = true;
}
<STRING>\\(.|\n)  {
    if ((string_buf_ptr - string_buf) < MAX_STR_CONST) {
    switch(yytext[yyleng - 1]) {
    case 'n':
        *string_buf_ptr = '\n';
        break;
    case 't':
        *string_buf_ptr = '\t';
        break;
    case 'b':
        *string_buf_ptr = '\b';
        break;
    case 'f':
        *string_buf_ptr = '\f';
        break;
    case '\n':
        *string_buf_ptr = '\n';
        curr_lineno += 1;
        break;
    case '\0':
        contains_escaped_null = true;
        break;
    default:
        *string_buf_ptr = yytext[yyleng-1];
    }
    string_buf_ptr++;
    }
}
<STRING>{NEWLINE}   {
    BEGIN 0;
    curr_lineno += 1;
    cool_yylval.error_msg = "Unterminated string constant";
    return (ERROR);
}
<STRING><<EOF>>       {
    cool_yylval.error_msg = "EOF in string";
    BEGIN 0;
    return (ERROR);
}
<INITIAL>{STRING_START}  {
    string_buf_ptr = string_buf;
    contains_escaped_null = false;
    null_in_string = false;
    BEGIN STRING;
}
<INITIAL>{COMMENT_END} {
    cool_yylval.error_msg = "Unmatched *)";
    return (ERROR);
}
{NEWLINE}           { curr_lineno += 1; }
<INITIAL>{DARROW}		{ return (DARROW); }
<INITIAL>{ASSIGN}        { return (ASSIGN); }
<INITIAL>{LE}            { return (LE); }
<INITIAL>{TRUE}          { cool_yylval.boolean = 1; return (BOOL_CONST); }
<INITIAL>{FALSE}         { cool_yylval.boolean = 0; return (BOOL_CONST); }
<INITIAL>{INTEGER}       {
    cool_yylval.symbol = integers.add_string(yytext);
    return (INT_CONST);
}
<INITIAL>{IDENT}         {
    int token = is_keyword(yytext, yyleng);
    if (token) return token;

    cool_yylval.symbol = identifiers.add_string(yytext);
    if ('A' <= yytext[0] && yytext[0] <= 'Z')
        return (TYPEID);
    else
        return (OBJECTID);
}
<INITIAL>{WHITESPACE}        {}
<INITIAL>{COMMENT_START}     { comment_level = 1; BEGIN COMMENT; }
<INITIAL>{LCOMMENT_START}    { BEGIN LINECOMMENT; }
<INITIAL>[-;{}().:=,+<*~/@]    { return yytext[yyleng-1]; }
.                            { cool_yylval.error_msg = yytext; return (ERROR); }

 /*
  * Keywords are case-insensitive except for the values true and false,
  * which must begin with a lower-case letter.
  */


 /*
  *  String constants (C syntax)
  *  Escape sequence \c is accepted for all characters c. Except for 
  *  \n \t \b \f, the result is c.
  *
  */


%%

int is_keyword(char *token, int len) {
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); ++i) {
        char *keyword = cool_token_to_string(keywords[i]);
        bool match = true;
        for (int j = 0; j < len; j++) {
            if (toupper(token[j]) != keyword[j]) {
                match = false;
                break;
            }
        }
        if (match && keyword[len] == 0) return keywords[i];
    }
    return 0;
}
