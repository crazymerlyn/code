#include "hoc.h"
#include "y.tab.h"
#include <math.h>

extern double Log(), Log10(), Exp(), Sqrt(), integer();
static struct {
    char *name;
    double cval;
} consts[] = {
    "PI",    M_PI,
    "E",     M_E,
    "GAMMA", 0.57721566490153286060,
    "DEG",   180.0 / M_PI,
    "PHI",   1.61803398874989484820,
};

static struct {
    char *name;
    double (*func)();
} builtins[] = {
    "sin",  sin,
    "cos",  cos,
    "atan", atan,
    "log", Log,
    "log10", Log10,
    "exp", Exp,
    "sqrt", Sqrt,
    "int", integer,
    "abs", fabs,
};

static struct {
    char *name;
    int kval;
} keywords[] = {
    "if", IF,
    "else", ELSE,
    "while", WHILE,
    "print", PRINT,
};

void init() {
    Symbol *s;

    for (int i = 0; i < sizeof(consts) / sizeof(consts[0]); i++) {
        install(consts[i].name, VAR, consts[i].cval);
    }
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++) {
        install(keywords[i].name, keywords[i].kval, 0.0);
    }
    for (int i = 0; i < sizeof(builtins) / sizeof(builtins[0]); i++) {
        s = install(builtins[i].name, BLTIN, 0.0);
        s->u.ptr = builtins[i].func;
    }
}

