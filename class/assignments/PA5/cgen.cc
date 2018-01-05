
//**************************************************************
//
// Code generator SKELETON
//
// Read the comments carefully. Make sure to
//    initialize the base class tags in
//       `CgenClassTable::CgenClassTable'
//
//    Add the label for the dispatch tables to
//       `IntEntry::code_def'
//       `StringEntry::code_def'
//       `BoolConst::code_def'
//
//    Add code to emit everyting else that is needed
//       in `CgenClassTable::code'
//
//
// The files as provided will produce code to begin the code
// segments, declare globals, and emit constants.  You must
// fill in the rest.
//
//**************************************************************

#include "cgen.h"
#include "cgen_gc.h"
#include <algorithm>

extern void emit_string_constant(ostream& str, char *s);
extern int cgen_debug;

//
// Three symbols from the semantic analyzer (semant.cc) are used.
// If e : No_type, then no code is generated for e.
// Special code is generated for new SELF_TYPE.
// The name "self" also generates code different from other references.
//
//////////////////////////////////////////////////////////////////////
//
// Symbols
//
// For convenience, a large number of symbols are predefined here.
// These symbols include the primitive type and method names, as well
// as fixed names used by the runtime system.
//
//////////////////////////////////////////////////////////////////////
Symbol 
       arg,
       arg2,
       Bool,
       concat,
       cool_abort,
       copy,
       Int,
       in_int,
       in_string,
       IO,
       length,
       Main,
       main_meth,
       No_class,
       No_type,
       Object,
       out_int,
       out_string,
       prim_slot,
       self,
       SELF_TYPE,
       Str,
       str_field,
       substr,
       type_name,
       val;
//
// Initializing the predefined symbols.
//
static void initialize_constants(void)
{
  arg         = idtable.add_string("arg");
  arg2        = idtable.add_string("arg2");
  Bool        = idtable.add_string("Bool");
  concat      = idtable.add_string("concat");
  cool_abort  = idtable.add_string("abort");
  copy        = idtable.add_string("copy");
  Int         = idtable.add_string("Int");
  in_int      = idtable.add_string("in_int");
  in_string   = idtable.add_string("in_string");
  IO          = idtable.add_string("IO");
  length      = idtable.add_string("length");
  Main        = idtable.add_string("Main");
  main_meth   = idtable.add_string("main");
//   _no_class is a symbol that can't be the name of any 
//   user-defined class.
  No_class    = idtable.add_string("_no_class");
  No_type     = idtable.add_string("_no_type");
  Object      = idtable.add_string("Object");
  out_int     = idtable.add_string("out_int");
  out_string  = idtable.add_string("out_string");
  prim_slot   = idtable.add_string("_prim_slot");
  self        = idtable.add_string("self");
  SELF_TYPE   = idtable.add_string("SELF_TYPE");
  Str         = idtable.add_string("String");
  str_field   = idtable.add_string("_str_field");
  substr      = idtable.add_string("substr");
  type_name   = idtable.add_string("type_name");
  val         = idtable.add_string("_val");
}

static char *gc_init_names[] =
  { "_NoGC_Init", "_GenGC_Init", "_ScnGC_Init" };
static char *gc_collect_names[] =
  { "_NoGC_Collect", "_GenGC_Collect", "_ScnGC_Collect" };


//  BoolConst is a class that implements code generation for operations
//  on the two booleans, which are given global names here.
BoolConst falsebool(FALSE);
BoolConst truebool(TRUE);

int label_no = 0;

int get_label_no() {
    label_no += 1;
    return label_no - 1;
}

CgenClassTable *classtable;

//*********************************************************
//
// Define method for code generation
//
// This is the method called by the compiler driver
// `cgtest.cc'. cgen takes an `ostream' to which the assembly will be
// emmitted, and it passes this and the class list of the
// code generator tree to the constructor for `CgenClassTable'.
// That constructor performs all of the work of the code
// generator.
//
//*********************************************************

void program_class::cgen(ostream &os) 
{
  // spim wants comments to start with '#'
  os << "# start of generated code\n";

  initialize_constants();
  CgenClassTable *codegen_classtable = new CgenClassTable(classes,os);

  os << "\n# end of generated code\n";
}


//////////////////////////////////////////////////////////////////////////////
//
//  emit_* procedures
//
//  emit_X  writes code for operation "X" to the output stream.
//  There is an emit_X for each opcode X, as well as emit_ functions
//  for generating names according to the naming conventions (see emit.h)
//  and calls to support functions defined in the trap handler.
//
//  Register names and addresses are passed as strings.  See `emit.h'
//  for symbolic names you can use to refer to the strings.
//
//////////////////////////////////////////////////////////////////////////////

static void emit_load(char *dest_reg, int offset, const char *source_reg, ostream& s)
{
  s << LW << dest_reg << " " << offset * WORD_SIZE << "(" << source_reg << ")" 
    << endl;
}

static void emit_store(char *source_reg, int offset, const char *dest_reg, ostream& s)
{
  s << SW << source_reg << " " << offset * WORD_SIZE << "(" << dest_reg << ")"
      << endl;
}

static void emit_load_imm(char *dest_reg, int val, ostream& s)
{ s << LI << dest_reg << " " << val << endl; }

static void emit_load_address(char *dest_reg, char *address, ostream& s)
{ s << LA << dest_reg << " " << address << endl; }

static void emit_partial_load_address(char *dest_reg, ostream& s)
{ s << LA << dest_reg << " "; }

static void emit_load_bool(char *dest, const BoolConst& b, ostream& s)
{
  emit_partial_load_address(dest,s);
  b.code_ref(s);
  s << endl;
}

static void emit_load_string(char *dest, StringEntry *str, ostream& s)
{
  emit_partial_load_address(dest,s);
  str->code_ref(s);
  s << endl;
}

static void emit_load_int(char *dest, IntEntry *i, ostream& s)
{
  emit_partial_load_address(dest,s);
  i->code_ref(s);
  s << endl;
}

static void emit_move(char *dest_reg, char *source_reg, ostream& s)
{ s << MOVE << dest_reg << " " << source_reg << endl; }

static void emit_neg(char *dest, char *src1, ostream& s)
{ s << NEG << dest << " " << src1 << endl; }

static void emit_add(char *dest, char *src1, char *src2, ostream& s)
{ s << ADD << dest << " " << src1 << " " << src2 << endl; }

static void emit_addu(char *dest, char *src1, char *src2, ostream& s)
{ s << ADDU << dest << " " << src1 << " " << src2 << endl; }

static void emit_addiu(char *dest, char *src1, int imm, ostream& s)
{ s << ADDIU << dest << " " << src1 << " " << imm << endl; }

static void emit_div(char *dest, char *src1, char *src2, ostream& s)
{ s << DIV << dest << " " << src1 << " " << src2 << endl; }

static void emit_mul(char *dest, char *src1, char *src2, ostream& s)
{ s << MUL << dest << " " << src1 << " " << src2 << endl; }

static void emit_sub(char *dest, char *src1, char *src2, ostream& s)
{ s << SUB << dest << " " << src1 << " " << src2 << endl; }

static void emit_sll(char *dest, char *src1, int num, ostream& s)
{ s << SLL << dest << " " << src1 << " " << num << endl; }

static void emit_jalr(char *dest, ostream& s)
{ s << JALR << "\t" << dest << endl; }

static void emit_jal(char *address,ostream &s)
{ s << JAL << address << endl; }

static void emit_return(ostream& s)
{ s << RET << endl; }

static void emit_gc_assign(ostream& s)
{ s << JAL << "_GenGC_Assign" << endl; }

static void emit_disptable_ref(Symbol sym, ostream& s)
{  s << sym << DISPTAB_SUFFIX; }

static void emit_method_start(ostream& s) {
    emit_addiu(SP, SP, -12, s);
    emit_store(FP, 3, SP, s);
    emit_store(SELF, 2, SP, s);
    emit_store(RA, 1, SP, s);
    emit_addiu(FP, SP, 4, s);
    emit_move(SELF, ACC, s);
}

static void emit_method_end(int args, ostream& s) {
    emit_load(FP, 3, SP, s);
    emit_load(SELF, 2, SP, s);
    emit_load(RA, 1, SP, s);
    emit_addiu(SP, SP, args * WORD_SIZE + 12, s);
    emit_return(s);
}

static void emit_init_ref(Symbol sym, ostream& s)
{ s << sym << CLASSINIT_SUFFIX; }

static void emit_label_ref(int l, ostream &s)
{ s << "label" << l; }

static void emit_protobj_ref(Symbol sym, ostream& s)
{ s << sym << PROTOBJ_SUFFIX; }

static void emit_method_ref(Symbol classname, Symbol methodname, ostream& s)
{ s << classname << METHOD_SEP << methodname; }

static void emit_label_def(int l, ostream &s)
{
  emit_label_ref(l,s);
  s << ":" << endl;
}

static void emit_beqz(char *source, int label, ostream &s)
{
  s << BEQZ << source << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_beq(char *src1, char *src2, int label, ostream &s)
{
  s << BEQ << src1 << " " << src2 << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_bne(char *src1, char *src2, int label, ostream &s)
{
  s << BNE << src1 << " " << src2 << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_bleq(char *src1, char *src2, int label, ostream &s)
{
  s << BLEQ << src1 << " " << src2 << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_blt(char *src1, char *src2, int label, ostream &s)
{
  s << BLT << src1 << " " << src2 << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_blti(char *src1, int imm, int label, ostream &s)
{
  s << BLT << src1 << " " << imm << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_bgti(char *src1, int imm, int label, ostream &s)
{
  s << BGT << src1 << " " << imm << " ";
  emit_label_ref(label,s);
  s << endl;
}

static void emit_branch(int l, ostream& s)
{
  s << BRANCH;
  emit_label_ref(l,s);
  s << endl;
}

//
// Push a register on the stack. The stack grows towards smaller addresses.
//
static void emit_push(char *reg, ostream& str)
{
    str << "# pushing " << reg << endl;
  emit_store(reg,0,SP,str);
  emit_addiu(SP,SP,-4,str);
}

static void emit_pop(char *reg, ostream& str)
{
    str << "# popping " << reg << endl;
  emit_addiu(SP,SP,4,str);
  emit_load(reg,0,SP,str);
}

//
// Fetch the integer value in an Int object.
// Emits code to fetch the integer value of the Integer object pointed
// to by register source into the register dest
//
static void emit_fetch_int(char *dest, char *source, ostream& s)
{ emit_load(dest, DEFAULT_OBJFIELDS, source, s); }

//
// Emits code to store the integer value contained in register source
// into the Integer object pointed to by dest.
//
static void emit_store_int(char *source, char *dest, ostream& s)
{ emit_store(source, DEFAULT_OBJFIELDS, dest, s); }


static void emit_test_collector(ostream &s)
{
  emit_push(ACC, s);
  emit_move(ACC, SP, s); // stack end
  emit_move(A1, ZERO, s); // allocate nothing
  s << JAL << gc_collect_names[cgen_Memmgr] << endl;
  emit_addiu(SP,SP,4,s);
  emit_load(ACC,0,SP,s);
}

static void emit_gc_check(char *source, ostream &s)
{
  if (source != (char*)A1) emit_move(A1, source, s);
  s << JAL << "_gc_check" << endl;
}


///////////////////////////////////////////////////////////////////////////////
//
// coding strings, ints, and booleans
//
// Cool has three kinds of constants: strings, ints, and booleans.
// This section defines code generation for each type.
//
// All string constants are listed in the global "stringtable" and have
// type StringEntry.  StringEntry methods are defined both for String
// constant definitions and references.
//
// All integer constants are listed in the global "inttable" and have
// type IntEntry.  IntEntry methods are defined for Int
// constant definitions and references.
//
// Since there are only two Bool values, there is no need for a table.
// The two booleans are represented by instances of the class BoolConst,
// which defines the definition and reference methods for Bools.
//
///////////////////////////////////////////////////////////////////////////////

//
// Strings
//
void StringEntry::code_ref(ostream& s)
{
  s << STRCONST_PREFIX << index;
}

//
// Emit code for a constant String.
// You should fill in the code naming the dispatch table.
//

void StringEntry::code_def(ostream& s, int stringclasstag)
{
  IntEntryP lensym = inttable.add_int(len);

  // Add -1 eye catcher
  s << WORD << "-1" << endl;

  code_ref(s);  s  << LABEL                                             // label
      << WORD << stringclasstag << endl                                 // tag
      << WORD << (DEFAULT_OBJFIELDS + STRING_SLOTS + (len+4)/4) << endl // size
      << WORD;


      s << Str->get_string() << DISPTAB_SUFFIX << endl;
      s << WORD;  lensym->code_ref(s);  s << endl;            // string length
  emit_string_constant(s,str);                                // ascii string
  s << ALIGN;                                                 // align to word
}

//
// StrTable::code_string
// Generate a string object definition for every string constant in the 
// stringtable.
//
void StrTable::code_string_table(ostream& s, int stringclasstag)
{  
  for (List<StringEntry> *l = tbl; l; l = l->tl())
    l->hd()->code_def(s,stringclasstag);
}

//
// Ints
//
void IntEntry::code_ref(ostream &s)
{
  s << INTCONST_PREFIX << index;
}

//
// Emit code for a constant Integer.
// You should fill in the code naming the dispatch table.
//

void IntEntry::code_def(ostream &s, int intclasstag)
{
  // Add -1 eye catcher
  s << WORD << "-1" << endl;

  code_ref(s);  s << LABEL                                // label
      << WORD << intclasstag << endl                      // class tag
      << WORD << (DEFAULT_OBJFIELDS + INT_SLOTS) << endl  // object size
      << WORD; 

      s << Int->get_string() << DISPTAB_SUFFIX << endl;
      s << WORD << str << endl;                           // integer value
}


//
// IntTable::code_string_table
// Generate an Int object definition for every Int constant in the
// inttable.
//
void IntTable::code_string_table(ostream &s, int intclasstag)
{
  for (List<IntEntry> *l = tbl; l; l = l->tl())
    l->hd()->code_def(s,intclasstag);
}


//
// Bools
//
BoolConst::BoolConst(int i) : val(i) { assert(i == 0 || i == 1); }

void BoolConst::code_ref(ostream& s) const
{
  s << BOOLCONST_PREFIX << val;
}
  
//
// Emit code for a constant Bool.
// You should fill in the code naming the dispatch table.
//

void BoolConst::code_def(ostream& s, int boolclasstag)
{
  // Add -1 eye catcher
  s << WORD << "-1" << endl;

  code_ref(s);  s << LABEL                                  // label
      << WORD << boolclasstag << endl                       // class tag
      << WORD << (DEFAULT_OBJFIELDS + BOOL_SLOTS) << endl   // object size
      << WORD;

      s << Bool->get_string() << DISPTAB_SUFFIX << endl;
      s << WORD << val << endl;                             // value (0 or 1)
}

//////////////////////////////////////////////////////////////////////////////
//
//  CgenClassTable methods
//
//////////////////////////////////////////////////////////////////////////////

//***************************************************
//
//  Emit code to start the .data segment and to
//  declare the global names.
//
//***************************************************

void CgenClassTable::code_global_data()
{
  Symbol main    = idtable.lookup_string(MAINNAME);
  Symbol string  = idtable.lookup_string(STRINGNAME);
  Symbol integer = idtable.lookup_string(INTNAME);
  Symbol boolc   = idtable.lookup_string(BOOLNAME);

  str << "\t.data\n" << ALIGN;
  //
  // The following global names must be defined first.
  //
  str << GLOBAL << CLASSNAMETAB << endl;
  str << GLOBAL; emit_protobj_ref(main,str);    str << endl;
  str << GLOBAL; emit_protobj_ref(integer,str); str << endl;
  str << GLOBAL; emit_protobj_ref(string,str);  str << endl;
  str << GLOBAL; falsebool.code_ref(str);  str << endl;
  str << GLOBAL; truebool.code_ref(str);   str << endl;
  str << GLOBAL << INTTAG << endl;
  str << GLOBAL << BOOLTAG << endl;
  str << GLOBAL << STRINGTAG << endl;

  //
  // We also need to know the tag of the Int, String, and Bool classes
  // during code generation.
  //
  str << INTTAG << LABEL
      << WORD << intclasstag << endl;
  str << BOOLTAG << LABEL 
      << WORD << boolclasstag << endl;
  str << STRINGTAG << LABEL 
      << WORD << stringclasstag << endl;    
}


//***************************************************
//
//  Emit code to start the .text segment and to
//  declare the global names.
//
//***************************************************

void CgenClassTable::code_global_text()
{
  str << GLOBAL << HEAP_START << endl
      << HEAP_START << LABEL 
      << WORD << 0 << endl
      << "\t.text" << endl
      << GLOBAL;
  emit_init_ref(idtable.add_string("Main"), str);
  str << endl << GLOBAL;
  emit_init_ref(idtable.add_string("Int"),str);
  str << endl << GLOBAL;
  emit_init_ref(idtable.add_string("String"),str);
  str << endl << GLOBAL;
  emit_init_ref(idtable.add_string("Bool"),str);
  str << endl << GLOBAL;
  emit_method_ref(idtable.add_string("Main"), idtable.add_string("main"), str);
  str << endl;
}

void CgenClassTable::code_bools(int boolclasstag)
{
  falsebool.code_def(str,boolclasstag);
  truebool.code_def(str,boolclasstag);
}

void CgenClassTable::code_select_gc()
{
  //
  // Generate GC choice constants (pointers to GC functions)
  //
  str << GLOBAL << "_MemMgr_INITIALIZER" << endl;
  str << "_MemMgr_INITIALIZER:" << endl;
  str << WORD << gc_init_names[cgen_Memmgr] << endl;
  str << GLOBAL << "_MemMgr_COLLECTOR" << endl;
  str << "_MemMgr_COLLECTOR:" << endl;
  str << WORD << gc_collect_names[cgen_Memmgr] << endl;
  str << GLOBAL << "_MemMgr_TEST" << endl;
  str << "_MemMgr_TEST:" << endl;
  str << WORD << (cgen_Memmgr_Test == GC_TEST) << endl;
}


//********************************************************
//
// Emit code to reserve space for and initialize all of
// the constants.  Class names should have been added to
// the string table (in the supplied code, is is done
// during the construction of the inheritance graph), and
// code for emitting string constants as a side effect adds
// the string's length to the integer table.  The constants
// are emmitted by running through the stringtable and inttable
// and producing code for each entry.
//
//********************************************************

void CgenClassTable::code_constants()
{
  //
  // Add constants that are required by the code generator.
  //
  stringtable.add_string("");
  inttable.add_string("0");

  stringtable.code_string_table(str,stringclasstag);
  inttable.code_string_table(str,intclasstag);
  code_bools(boolclasstag);
}


void CgenClassTable::code_prototypes()
{
    for (auto p = nds; p; p = p->tl()) {
        p->hd()->code_prototype(str);
    }
}

void CgenClassTable::code_class_nametab()
{
    std::vector<CgenNodeP> nodes(current_tag);
    for (auto p = nds; p; p = p->tl()) {
        nodes[p->hd()->get_tag()] = p->hd();
    }
    str << CLASSNAMETAB << ":" << endl;
    for (auto p: nodes) {
        str << WORD;
        stringtable.lookup_string(p->get_name()->get_string())->code_ref(str);
        str << endl;
    }
}

void CgenClassTable::code_class_objtab()
{
    std::vector<CgenNodeP> nodes(current_tag);
    str << CLASSOBJTAB << ":" << endl;
    for (auto p = nds; p; p = p->tl()) {
        nodes[p->hd()->get_tag()] = p->hd();
    }
    for (auto nd: nodes) {
        str << WORD;
        emit_protobj_ref(nd->get_name(), str);
        str << endl;
        str << WORD;
        emit_init_ref(nd->get_name(), str);
        str << endl;
    }
}

void CgenClassTable::code_dispatch_tables()
{
    for (auto p = nds; p; p = p->tl()) {
        p->hd()->code_dispatch_table(str);
    }
}

void CgenClassTable::code_initializers()
{
    for (auto p = nds; p; p = p->tl()) {
        p->hd()->code_initializer(str);
    }
}


void CgenClassTable::code_methods()
{
    for (auto p = nds; p; p = p->tl()) {
        if (! p->hd()->is_basic()) p->hd()->code_methods(str);
    }
}


CgenClassTable::CgenClassTable(Classes classes, ostream& s) : nds(NULL) , str(s)
{
   enterscope();
   if (cgen_debug) cout << "Building CgenClassTable" << endl;
   install_basic_classes();
   install_classes(classes);

   build_inheritance_tree();

   current_tag = 0;
   set_tags(root());

   stringclasstag = probe(Str)->get_tag();
   intclasstag =    probe(Int)->get_tag();
   boolclasstag =   probe(Bool)->get_tag();

   build_dispatch_tables(root());

   classtable = this;
   code();
   exitscope();
}

void CgenClassTable::install_basic_classes()
{

// The tree package uses these globals to annotate the classes built below.
  //curr_lineno  = 0;
  Symbol filename = stringtable.add_string("<basic class>");

//
// A few special class names are installed in the lookup table but not
// the class list.  Thus, these classes exist, but are not part of the
// inheritance hierarchy.
// No_class serves as the parent of Object and the other special classes.
// SELF_TYPE is the self class; it cannot be redefined or inherited.
// prim_slot is a class known to the code generator.
//
  addid(No_class,
	new CgenNode(class_(No_class,No_class,nil_Features(),filename),
			    Basic,this));
  addid(SELF_TYPE,
	new CgenNode(class_(SELF_TYPE,No_class,nil_Features(),filename),
			    Basic,this));
  addid(prim_slot,
	new CgenNode(class_(prim_slot,No_class,nil_Features(),filename),
			    Basic,this));

// 
// The Object class has no parent class. Its methods are
//        cool_abort() : Object    aborts the program
//        type_name() : Str        returns a string representation of class name
//        copy() : SELF_TYPE       returns a copy of the object
//
// There is no need for method bodies in the basic classes---these
// are already built in to the runtime system.
//
  install_class(
   new CgenNode(
    class_(Object, 
	   No_class,
	   append_Features(
           append_Features(
           single_Features(method(cool_abort, nil_Formals(), Object, no_expr())),
           single_Features(method(type_name, nil_Formals(), Str, no_expr()))),
           single_Features(method(copy, nil_Formals(), SELF_TYPE, no_expr()))),
	   filename),
    Basic,this));

// 
// The IO class inherits from Object. Its methods are
//        out_string(Str) : SELF_TYPE          writes a string to the output
//        out_int(Int) : SELF_TYPE               "    an int    "  "     "
//        in_string() : Str                    reads a string from the input
//        in_int() : Int                         "   an int     "  "     "
//
   install_class(
    new CgenNode(
     class_(IO, 
            Object,
            append_Features(
            append_Features(
            append_Features(
            single_Features(method(out_string, single_Formals(formal(arg, Str)),
                        SELF_TYPE, no_expr())),
            single_Features(method(out_int, single_Formals(formal(arg, Int)),
                        SELF_TYPE, no_expr()))),
            single_Features(method(in_string, nil_Formals(), Str, no_expr()))),
            single_Features(method(in_int, nil_Formals(), Int, no_expr()))),
	   filename),	    
    Basic,this));

//
// The Int class has no methods and only a single attribute, the
// "val" for the integer. 
//
   install_class(
    new CgenNode(
     class_(Int, 
	    Object,
            single_Features(attr(val, prim_slot, no_expr())),
	    filename),
     Basic,this));

//
// Bool also has only the "val" slot.
//
    install_class(
     new CgenNode(
      class_(Bool, Object, single_Features(attr(val, prim_slot, no_expr())),filename),
      Basic,this));

//
// The class Str has a number of slots and operations:
//       val                                  ???
//       str_field                            the string itself
//       length() : Int                       length of the string
//       concat(arg: Str) : Str               string concatenation
//       substr(arg: Int, arg2: Int): Str     substring
//       
   install_class(
    new CgenNode(
      class_(Str, 
	     Object,
             append_Features(
             append_Features(
             append_Features(
             append_Features(
             single_Features(attr(val, Int, no_expr())),
            single_Features(attr(str_field, prim_slot, no_expr()))),
            single_Features(method(length, nil_Formals(), Int, no_expr()))),
            single_Features(method(concat, 
				   single_Formals(formal(arg, Str)),
				   Str, 
				   no_expr()))),
	    single_Features(method(substr, 
				   append_Formals(single_Formals(formal(arg, Int)), 
						  single_Formals(formal(arg2, Int))),
				   Str, 
				   no_expr()))),
	     filename),
        Basic,this));

}

// CgenClassTable::install_class
// CgenClassTable::install_classes
//
// install_classes enters a list of classes in the symbol table.
//
void CgenClassTable::install_class(CgenNodeP nd)
{
  Symbol name = nd->get_name();

  if (probe(name))
    {
      return;
    }

  // The class name is legal, so add it to the list of classes
  // and the symbol table.
  nds = new List<CgenNode>(nd,nds);
  addid(name,nd);
}

void CgenClassTable::set_tags(CgenNodeP nd) {
    nd->set_tag(current_tag);
    current_tag += 1;
    for (auto p = nd->get_children(); p; p = p->tl()) {
        set_tags(p->hd());
    }
    nd->set_final_tag(current_tag - 1);
}

void CgenClassTable::install_classes(Classes cs)
{
  for(int i = cs->first(); cs->more(i); i = cs->next(i))
    install_class(new CgenNode(cs->nth(i),NotBasic,this));
}

//
// CgenClassTable::build_inheritance_tree
//
void CgenClassTable::build_inheritance_tree()
{
  for(List<CgenNode> *l = nds; l; l = l->tl())
      set_relations(l->hd());
}

void CgenClassTable::build_dispatch_tables(CgenNodeP nd)
{
    nd->build_dispatch_table();
    for(List<CgenNode> *l = nd->get_children(); l; l = l->tl())
      build_dispatch_tables(l->hd());
}

//
// CgenClassTable::set_relations
//
// Takes a CgenNode and locates its, and its parent's, inheritance nodes
// via the class table.  Parent and child pointers are added as appropriate.
//
void CgenClassTable::set_relations(CgenNodeP nd)
{
  CgenNode *parent_node = probe(nd->get_parent());
  nd->set_parentnd(parent_node);
  parent_node->add_child(nd);
}

void CgenNode::add_child(CgenNodeP n)
{
  children = new List<CgenNode>(n,children);
}

void CgenNode::set_parentnd(CgenNodeP p)
{
  assert(parentnd == NULL);
  assert(p != NULL);
  parentnd = p;
}


void CgenNode::set_tag(int tag) {
    this->tag = tag;
}

int CgenNode::get_tag() {
    return this->tag;
}

int CgenNode::get_size() {
    int s = 3;
    int parent_attrs = 0;
    if (parentnd && parentnd->get_name() != Object) parent_attrs = parentnd->get_size() - 3;
    for (int i = 0; i < features->len(); ++i) {
        if (! features->nth(i)->is_method()) {
            s += 1;
        }
    }
    return s + parent_attrs;
}

int CgenNode::get_attr_offset(Symbol attr) {
    for (unsigned int i = 0; i < attrs.size(); ++i) {
        if (attrs[i] == attr) {
            return i;
        }
    }
    cerr << attr->get_string() << endl;
    assert(false);
    return -1;
}

int CgenNode::get_dispatch_offset(Symbol method_name) {
    return dispatch_pos[method_name];
}

void CgenNode::code_prototype(ostream& str)
{
    emit_protobj_ref(get_name(), str);
    str << ":" << endl;
    str << WORD << get_tag() << endl;
    str << WORD << get_size() << endl;
    str << WORD;
    emit_disptable_ref(get_name(), str);
    str << endl;
    code_attributes(str);
}

void CgenNode::code_attributes(ostream& str)
{
    if (parentnd && parentnd->get_name() != Object) {
        parentnd->code_attributes(str);
    }
    for (int i = 0; i < features->len(); ++i) {
        auto feature = features->nth(i);
        if (!feature->is_method()) {
            str << WORD;
            auto ty = feature->get_type();
            if (ty == Int) {
                inttable.add_int(0)->code_ref(str);
            } else if (ty == Bool) {
                falsebool.code_ref(str);
            } else if (ty == Str) {
                stringtable.add_string("")->code_ref(str);
            } else {
                str << 0;
            }
            str << endl;
        }
    }
}

void CgenNode::build_dispatch_table()
{
    if (parentnd && parentnd != this) {
        this->dispatch_names = parentnd->dispatch_names;
        this->dispatch_pos = parentnd->dispatch_pos;
        this->attrs = parentnd->attrs;
        this->depth = parentnd->depth + 1;
    }
    for (int i = 0; i < features->len(); ++i) {
        auto feature = features->nth(i);
        if (feature->is_method()) {
            auto name = feature->get_name();
            auto disp_name = std::string(get_name()->get_string()) + "." + name->get_string();
            if (dispatch_pos.find(name) != dispatch_pos.end()) {
                dispatch_names[dispatch_pos[name]] = disp_name;
            } else {
                dispatch_pos[name] = dispatch_names.size();
                dispatch_names.push_back(disp_name);
            }
        } else {
            this->attrs.push_back(feature->get_name());
        }
    }
}

void CgenNode::code_dispatch_table(ostream& str)
{
    emit_disptable_ref(get_name(), str);
    str << ":" << endl;
    for (auto dispatch_name: dispatch_names) {
        str << WORD << dispatch_name << endl;
    }
}

Context CgenNode::get_context() {
    return Context(this);
}

void CgenNode::code_initializer(ostream& str)
{
    emit_init_ref(get_name(), str);
    str << ":" << endl;
    emit_method_start(str);
    if (get_name() != Object) {
        str << JAL;
        emit_init_ref(parentnd->get_name(), str);
        str << endl;
    }
    for (int i = 0; i < features->len(); ++i) {
        auto feature = features->nth(i);
        auto ctx = this->get_context();
        if (! feature->is_method()) {
            auto expr = feature->get_expr();
            if (expr->is_no_expr()) continue;
            expr->code(ctx, str);
            int offset = get_attr_offset(feature->get_name());
            emit_store(ACC, offset+DEFAULT_OBJFIELDS, SELF, str);
        }
    }
    emit_move(ACC, SELF, str);
    emit_method_end(0,str);
}


void CgenNode::code_methods(ostream& str)
{
    for (int i = 0; i < features->len(); ++i) {
        auto feature = features->nth(i);
        if (! feature->is_method()) continue;
        emit_method_ref(get_name(), feature->get_name(), str);
        str << ":" << endl;
        emit_method_start(str);
        auto ctx = get_context();
        auto newctx = Context(&ctx, feature->get_formals());
        feature->get_expr()->code(newctx, str);
        emit_method_end(feature->get_formals()->len(), str);
    }
}


void CgenClassTable::code()
{
  if (cgen_debug) cout << "coding global data" << endl;
  code_global_data();

  if (cgen_debug) cout << "choosing gc" << endl;
  code_select_gc();

  if (cgen_debug) cout << "coding constants" << endl;
  code_constants();

  if (cgen_debug) cout << "coding class name table" << endl;
  code_class_nametab();

  if (cgen_debug) cout << "coding class object table" << endl;
  code_class_objtab();

  if (cgen_debug) cout << "coding prototype objects" << endl;
  code_prototypes();

  if (cgen_debug) cout << "coding dispatch tables" << endl;
  code_dispatch_tables();

  if (cgen_debug) cout << "coding global text" << endl;
  code_global_text();

//                 Add your code to emit
//                   - object initializer
//                   - the class methods
//                   - etc...

  if (cgen_debug) cout << "coding initializers" << endl;
  code_initializers();

  if (cgen_debug) cout << "coding methods" << endl;
  code_methods();

}


CgenNodeP CgenClassTable::root()
{
   return probe(Object);
}


///////////////////////////////////////////////////////////////////////
//
// CgenNode methods
//
///////////////////////////////////////////////////////////////////////

CgenNode::CgenNode(Class_ nd, Basicness bstatus, CgenClassTableP ct) :
   class__class((const class__class &) *nd),
   parentnd(NULL),
   children(NULL),
   basic_status(bstatus)
{ 
   stringtable.add_string(name->get_string());          // Add class name to string table
}


//******************************************************************
//
//   Fill in the following methods to produce code for the
//   appropriate expression.  You may add or remove parameters
//   as you wish, but if you do, remember to change the parameters
//   of the declarations in `cool-tree.h'  Sample code for
//   constant integers, strings, and booleans are provided.
//
//*****************************************************************

void assign_class::code(Context& ctx, ostream &s) {
    expr->code(ctx, s);
    if (name == self) {
        emit_move(SELF, ACC, s);
        return;
    }
    auto mapping = ctx.get_mapping(name);
    emit_store(ACC,mapping.second, mapping.first.c_str(), s);
}

void static_dispatch_class::code(Context& ctx, ostream &s) {
    CgenNodeP nd = classtable->probe(type_name);
    if (actual->len() > 0) {
        s << "# Making space for arguments" << endl;
        emit_addiu(SP, SP, -WORD_SIZE * actual->len(), s);
    }
    for (int i = 0; i < actual->len(); ++i) {
        auto expr = actual->nth(i);
        expr->code(ctx, s);
        emit_store(ACC, actual->len() - i, SP, s);
    }
    expr->code(ctx, s);
    int label = get_label_no();
    emit_bne(ACC, ZERO, label, s);
    emit_load_string(ACC, stringtable.add_string(classtable->probe(Main)->get_filename()->get_string()), s);
    emit_load_imm(T1, 1, s);
    emit_jal("_dispatch_abort", s);
    emit_label_def(label, s);
    auto dispatch_offset = nd->get_dispatch_offset(name);
    s << LA << T1 << " ";
    emit_disptable_ref(type_name, s);
    s << endl;
    emit_load(T1, dispatch_offset, T1, s);
    emit_jalr(T1, s);
    //emit_addiu(SP, SP, WORD_SIZE * actual->len(), s);
}

void dispatch_class::code(Context& ctx, ostream &s) {
    CgenNodeP nd;
    if (expr->type == SELF_TYPE) {
        nd = ctx.get_node();
    } else {
        s << "# Type: " << expr->type << endl;
        nd = classtable->probe(expr->type);
    }
    s << "# Calling " << nd->get_name() << "." << name << endl;
    if (actual->len() > 0) {
        s << "# Making space for arguments" << endl;
        emit_addiu(SP, SP, -WORD_SIZE * actual->len(), s);
    }
    for (int i = 0; i < actual->len(); ++i) {
        auto expr = actual->nth(i);
        expr->code(ctx, s);
        //emit_store(ACC, i+1, SP, s);
        emit_store(ACC, actual->len() - i, SP, s);
    }
    expr->code(ctx, s);
    int label = get_label_no();
    emit_bne(ACC, ZERO, label, s);
    emit_load_string(ACC, stringtable.add_string(classtable->probe(Main)->get_filename()->get_string()), s);
    emit_load_imm(T1, 1, s);
    emit_jal("_dispatch_abort", s);
    emit_label_def(label, s);
    auto dispatch_offset = nd->get_dispatch_offset(name);
    s << "# Offset for " << name << " is: " << dispatch_offset << endl;
    emit_load(T1, DISPTABLE_OFFSET, ACC, s);
    emit_load(T1, dispatch_offset, T1, s);
    emit_jalr(T1, s);
}

void cond_class::code(Context& ctx, ostream &s) {
    pred->code(ctx, s);
    emit_load(ACC, DEFAULT_OBJFIELDS, ACC, s);
    int fals = get_label_no();
    int label = get_label_no();
    emit_beqz(ACC, fals, s);
    then_exp->code(ctx, s);
    emit_branch(label, s);
    emit_label_def(fals, s);
    else_exp->code(ctx, s);
    emit_label_def(label, s);
}

void loop_class::code(Context& ctx, ostream &s) {
    int begin = get_label_no();
    int end = get_label_no();
    s << "# Loop condition begin:" << endl;
    emit_label_def(begin, s);
    pred->code(ctx, s);
    emit_load(ACC, DEFAULT_OBJFIELDS, ACC, s);
    emit_beqz(ACC, end, s);
    s << "# Loop condition end:" << endl;
    body->code(ctx, s);
    emit_branch(begin, s);
    emit_label_def(end, s);
}

void typcase_class::code(Context& ctx, ostream &s) {
    expr->code(ctx, s);
    std::vector<Case> cs;
    for (int i = 0; i < cases->len(); ++i) {
        cs.push_back(cases->nth(i));
    }
    std::sort(cs.begin(), cs.end(), [] (Case a, Case b) -> bool {
            return classtable->probe(a->get_type())->get_tag() > classtable->probe(b->get_type())->get_tag();
    });
    int label = get_label_no();
    emit_bne(ACC, ZERO, label, s);
    emit_load_string(ACC, stringtable.add_string(classtable->probe(Main)->get_filename()->get_string()), s);
    emit_load_imm(T1, 1, s);
    emit_jal("_case_abort2", s);
    s << "# Start of cases" << endl;
    emit_label_def(label, s);
    emit_load(T1, 0, ACC, s);
    int end = get_label_no();
    for (auto c: cs) {
        label = get_label_no();
        auto nd = classtable->probe(c->get_type());
        emit_blti(T1, nd->get_tag(), label, s);
        emit_bgti(T1, nd->get_final_tag(), label, s);
        emit_push(ACC, s);
        auto newctx = Context(&ctx, c->get_name());
        c->get_expr()->code(newctx, s);
        emit_addiu(SP, SP, 4, s);
        emit_branch(end, s);
        emit_label_def(label, s);
    }
    emit_jal("_case_abort", s);
    emit_label_def(end, s);
}

void block_class::code(Context& ctx, ostream &s) {
    for (int i = 0; i < body->len(); ++i) {
        body->nth(i)->code(ctx, s);
    }
}

void let_class::code(Context& ctx, ostream &s) {
    s << "# in let: " << identifier << endl;
    s << LA << ACC << " ";
    if (type_decl == Int) {
        inttable.add_int(0)->code_ref(s);
    } else if (type_decl == Bool) {
        falsebool.code_ref(s);
    } else if (type_decl == Str) {
        stringtable.add_string("")->code_ref(s);
    } else {
        s << 0;
    }
    s << endl;
    if (! init->is_no_expr()) {
        init->code(ctx, s);
    }
    emit_push(ACC, s);
    auto newctx = Context(&ctx, identifier);
    body->code(newctx, s);
    emit_addiu(SP, SP, 4, s);
    s << "# out let: " << identifier << endl;
}

void plus_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_jal("Object.copy", s);
    emit_pop(T1, s);
    emit_fetch_int(T1, T1, s);
    emit_fetch_int(T2, ACC, s);
    emit_add(T2, T1, T2, s);
    emit_store_int(T2, ACC, s);
}

void sub_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_jal("Object.copy", s);
    emit_pop(T1, s);
    emit_fetch_int(T1, T1, s);
    emit_fetch_int(T2, ACC, s);
    emit_sub(T2, T1, T2, s);
    emit_store_int(T2, ACC, s);
}

void mul_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_jal("Object.copy", s);
    emit_pop(T1, s);
    emit_fetch_int(T1, T1, s);
    emit_fetch_int(T2, ACC, s);
    emit_mul(T2, T1, T2, s);
    emit_store_int(T2, ACC, s);
}

void divide_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_jal("Object.copy", s);
    emit_pop(T1, s);
    emit_fetch_int(T1, T1, s);
    emit_fetch_int(T2, ACC, s);
    emit_div(T2, T1, T2, s);
    emit_store_int(T2, ACC, s);
}

void neg_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_jal("Object.copy", s);
    emit_fetch_int(T1, ACC, s);
    emit_neg(T1, T1, s);
    emit_store_int(T1, ACC, s);
}

void lt_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_pop(T2, s);

    int label = get_label_no();
    emit_load_address(T1, "bool_const1", s);
    emit_fetch_int(T2, T2, s);
    emit_fetch_int(ACC, ACC, s);
    emit_blt(T2, ACC, label, s);
    emit_load_address(T1, "bool_const0", s);
    emit_label_def(label, s);
    emit_move(ACC, T1, s);
}

void eq_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_pop(T1, s);
    emit_move(T2, ACC, s);
    emit_load_bool(ACC, truebool, s);
    int label = get_label_no();
    emit_beq(T1, T2, label, s);
    emit_load_bool(A1, falsebool, s);
    emit_jal("equality_test", s);
    emit_label_def(label, s);
}

void leq_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_push(ACC, s);
    auto newctx = Context(&ctx, stringtable.add_string(""));
    e2->code(newctx, s);
    emit_pop(T2, s);

    int label = get_label_no();
    emit_fetch_int(ACC, ACC, s);
    emit_fetch_int(T2, T2, s);
    emit_load_address(T1, "bool_const0", s);
    emit_blt(ACC, T2, label, s);
    emit_load_address(T1, "bool_const1", s);
    emit_label_def(label, s);
    emit_move(ACC, T1, s);
}

void comp_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    emit_fetch_int(T2, ACC, s);
    int label = get_label_no();
    emit_load_address(T1, "bool_const1", s);
    emit_beqz(T2, label, s);
    emit_load_address(T1, "bool_const0", s);
    emit_label_def(label, s);
    emit_move(ACC, T1, s);
}

void int_const_class::code(Context& ctx, ostream& s)  
{
  //
  // Need to be sure we have an IntEntry *, not an arbitrary Symbol
  //
  emit_load_int(ACC,inttable.lookup_string(token->get_string()),s);
}

void string_const_class::code(Context& ctx, ostream& s)
{
  emit_load_string(ACC,stringtable.lookup_string(token->get_string()),s);
}

void bool_const_class::code(Context& ctx, ostream& s)
{
  emit_load_bool(ACC, BoolConst(val), s);
}

void new__class::code(Context& ctx, ostream &s) {
    if (type_name == SELF_TYPE) {
        emit_load_address(T1, CLASSOBJTAB, s);
        emit_load(T2, 0, SELF, s);
        emit_sll(T2, T2, 3, s);
        emit_addu(T1, T1, T2, s);
        emit_push(T1, s);
        emit_load(ACC, 0, T1, s);
    } else {
        s << LA << " " << ACC << " ";
        emit_protobj_ref(type_name, s);
        s << endl;
    }
    emit_jal("Object.copy", s);
    if (type_name == SELF_TYPE) {
        emit_pop(T1, s);
        emit_load(T1, 1, T1, s);
        emit_jalr(T1, s);
    } else {
        s << JAL << " ";
        emit_init_ref(type_name, s);
        s << endl;
    }
}

void isvoid_class::code(Context& ctx, ostream &s) {
    e1->code(ctx, s);
    
    int label = get_label_no();
    emit_load_address(T1, "bool_const1", s);
    emit_beqz(ACC, label, s);
    emit_load_address(T1, "bool_const0", s);
    emit_label_def(label, s);
    emit_move(ACC, T1, s);
    
}

void no_expr_class::code(Context& ctx, ostream &s) {
    emit_move(ACC, ZERO, s);
}

void object_class::code(Context& ctx, ostream &s) {
    if (name == self) {
        emit_move(ACC, SELF, s);
        return;
    }
    auto mapping = ctx.get_mapping(name);
    emit_load(ACC,mapping.second, mapping.first.c_str(), s);
}

