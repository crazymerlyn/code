#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "hoc.h"
#include "y.tab.h"

#define NSTACK 256
static Datum *stack; /* the stack */
static int stack_index;
static int stack_size;

#define NPROG 2000
Inst *prog;                 /* the machine */
static int prog_size;
Inst *progp;                /* next free spot for code generation */
Inst *pc;                   /* program counter during execution */

void initcode() {
    stack_size = NSTACK;
    stack = malloc(stack_size * sizeof(Datum));
    if (!stack) {
        perror("can't allocate stack:");
        exit(1);
    }
    stack_index = 0;

    prog_size = NPROG;
    prog = malloc(prog_size * sizeof(Inst));
    if (!prog) {
        perror("can't allocate memory for program");
        exit(1);
    }
    progp = prog;
}

void push(Datum d) {
    if (stack_index >= stack_size) {
        stack_size += stack_size;
        stack = realloc(stack, stack_size * sizeof(Datum));
        if (!stack) {
            perror("can't allocate stack");
            exit(1);
        }
    }

    stack[stack_index] = d;
    stack_index++;
}

Datum pop() {
    if (stack_index <= 0)
        execerror("stack underflow", NULL);
    return stack[--stack_index];
}

Inst *code(Inst f) {
    Inst *oprogp = progp;
    if (progp >= &prog[prog_size]) {
        int new_size = prog_size * 2;
        prog = realloc(prog, new_size * sizeof(Inst));
        if (!prog) {
            perror("can't allocate memory for program");
            exit(1);
        }
        progp = &prog[prog_size];
        prog_size = new_size;
    }
    *progp++ = f;
    return oprogp;
}

void execute(Inst *p) {
    for (pc = p; *pc != STOP;)
        (*pc++)();
}

void constpush() {
    Datum d;
    d.val = ((Symbol*)*pc++)->u.val;
    push(d);
}

void varpush() {
    Datum d;
    d.sym = (Symbol *) (*pc++);
    push(d);
}

void add() {
    Datum d1, d2;
    d2 = pop();
    d1 = pop();
    d1.val += d2.val;
    push(d1);
}

void sub() {
    Datum d1, d2;
    d2 = pop();
    d1 = pop();
    d1.val -= d2.val;
    push(d1);
}

void mul() {
    Datum d1, d2;
    d2 = pop();
    d1 = pop();
    d1.val *= d2.val;
    push(d1);
}

void division() {
    Datum d1, d2;
    d2 = pop();
    d1 = pop();
    d1.val /= d2.val;
    push(d1);
}

void mod() {
    Datum d1, d2;
    d2 = pop();
    d1 = pop();
    d1.val = fmod(d1.val, d2.val);
    push(d1);
}

void power() {
    Datum d1, d2;
    d2 = pop();
    d1 = pop();
    d1.val = pow(d1.val, d2.val);
    push(d1);
}

void negate() {
    Datum d;
    d = pop();
    d.val = -d.val;
    push(d);
}

void eval() {
    Datum d;
    d = pop();
    if (d.sym->type == UNDEF)
        execerror("undefined variable", d.sym->name);
    d.val = d.sym->u.val;
    push(d);
}

void assign() {
    Datum d1, d2;
    d1 = pop();
    d2 = pop();
    if (d1.sym->type != VAR && d1.sym->type != UNDEF)
        execerror("assignment to non-variable",
                   d1.sym->name);

    d1.sym->u.val = d2.val;
    d1.sym->type = VAR;
    push(d2);
}

void print() {
    Datum d;
    d = pop();
    printf("\t%.8g\n", d.val);
}

void builtin() {
    Datum d;
    d = pop();
    d.val = (*(double (*)())(*pc++))(d.val);
    push(d);
}

