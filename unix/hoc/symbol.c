#include "hoc.h"
#include "y.tab.h"

#include <string.h>
#include <stdlib.h>

static Symbol *symlist = 0;

Symbol *lookup(char *name) {
    for (Symbol *sp = symlist; sp != NULL; sp = sp->next) {
        if (strcmp(name, sp->name) == 0) return sp;
    }
    return NULL;
}

Symbol *install(char *s, int t, double d) {
    Symbol *sp;

    sp = malloc(sizeof(Symbol));
    sp->name = malloc(strlen(s) + 1);
    strcpy(sp->name, s);

    sp->type = t;
    sp->u.val = d;
    sp->next = symlist;
    symlist = sp;
    return sp;
}

