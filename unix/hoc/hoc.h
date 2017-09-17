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

typedef union Datum {
    double val;
    Symbol *sym;
} Datum;

extern Datum pop();

typedef void (*Inst)(); /* machine instruction */
#define STOP (Inst)0

extern Inst *prog;
extern void eval(), add(), sub(), mul(), division(), mod(), negate(), power();
extern void assign(), builtin(), varpush(), constpush(), print();
extern void execerror(char *s, char *t);
extern Inst *code(Inst f); 
extern void initcode();
void execute(Inst *p);

