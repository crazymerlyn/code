typedef struct Symbol {
    char *name;
    short type; /* VAR, BLTIN, UNDEF */
    union {
        double val;
        double (*ptr)();
    } u;
    struct Symbol *next;
} Symbol;

Symbol *install();
Symbol *lookup();

