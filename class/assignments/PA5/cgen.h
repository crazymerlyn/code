#include <assert.h>
#include <stdio.h>
#include <vector>
#include <map>
#include "emit.h"
#include "cool-tree.h"
#include "symtab.h"

enum Basicness     {Basic, NotBasic};
#define TRUE 1
#define FALSE 0

class CgenClassTable;
typedef CgenClassTable *CgenClassTableP;

class CgenNode;
typedef CgenNode *CgenNodeP;

class CgenClassTable : public SymbolTable<Symbol,CgenNode> {
private:
   List<CgenNode> *nds;
   ostream& str;
   int stringclasstag;
   int intclasstag;
   int boolclasstag;
   int current_tag;


// The following methods emit code for
// constants and global declarations.

   void code_global_data();
   void code_global_text();
   void code_bools(int);
   void code_select_gc();
   void code_constants();
   void code_prototypes();
   void code_class_nametab();
   void code_class_objtab();
   void code_dispatch_tables();
   void code_initializers();
   void code_methods();

// The following creates an inheritance graph from
// a list of classes.  The graph is implemented as
// a tree of `CgenNode', and class names are placed
// in the base class symbol table.

   void install_basic_classes();
   void install_class(CgenNodeP nd);
   void install_classes(Classes cs);
   void set_tags(CgenNodeP nd);
   void build_inheritance_tree();
   void build_dispatch_tables(CgenNodeP nd);
   void set_relations(CgenNodeP nd);
public:
   CgenClassTable(Classes, ostream& str);
   void code();
   CgenNodeP root();
};


class CgenNode : public class__class {
private: 
   CgenNodeP parentnd;                        // Parent of class
   List<CgenNode> *children;                  // Children of class
   Basicness basic_status;                    // `Basic' if class is basic
                                              // `NotBasic' otherwise
   int tag;
   int final_tag;
   std::vector<std::string> dispatch_names;
   std::map<Symbol, int> dispatch_pos;
   std::vector<Symbol> attrs;
   int depth;

public:
   CgenNode(Class_ c,
            Basicness bstatus,
            CgenClassTableP class_table);

   void add_child(CgenNodeP child);
   List<CgenNode> *get_children() { return children; }
   void set_parentnd(CgenNodeP p);
   void set_tag(int tag);
   void set_final_tag(int tag) { final_tag = tag; }
   int get_tag();
   int get_final_tag() { return final_tag; }
   int get_size();
   int get_attr_offset(Symbol attr);
   int get_dispatch_offset(Symbol method_name);
   bool is_basic() { return basic_status == Basic; }
   void build_dispatch_table();
   void code_prototype(ostream& stream);
   void code_attributes(ostream& stream);
   void code_dispatch_table(ostream& stream);
   void code_initializer(ostream& stream);
   void code_methods(ostream& stream);
   Context get_context();
   CgenNodeP get_parentnd() { return parentnd; }
   int basic() { return (basic_status == Basic); }
};

class BoolConst 
{
 private: 
  int val;
 public:
  BoolConst(int);
  void code_def(ostream&, int boolclasstag);
  void code_ref(ostream&) const;
};

class Context {
    private:
    std::map<Symbol, std::pair<std::string, int>> mapping;
    Context* parent;
    CgenNodeP nd;
    int stack_max;
    int count;

    public:
    Context(CgenNodeP nd): parent(NULL), nd(nd), stack_max(0), count(0) {};
    Context(Context* parent, Formals formals): parent(parent), nd(parent->nd), stack_max(parent->stack_max), count(0) {
        for (int i = 0; i < formals->len(); ++i) {
            auto formal = formals->nth(i);
            mapping[formal->get_name()] = std::make_pair(FP, i - formals->len() +1 - 3);
        }
        stack_max += parent->count;
    }
    Context(Context* parent, Symbol name): parent(parent), nd(parent->nd), stack_max(parent->stack_max), count(1) {
        mapping[name] = std::make_pair(FP, 1);
        stack_max += parent->count;
    }
    std::pair<std::string, int> get_mapping(Symbol name) {
        if (mapping.find(name) != mapping.end()) {
            auto res = mapping[name];
            res.second += stack_max;
            res.second = -res.second;
            return res;
        }
        if (parent) return parent->get_mapping(name);
        return std::make_pair(SELF, nd->get_attr_offset(name) + DEFAULT_OBJFIELDS);
    }

    CgenNodeP get_node() { return nd; }
};
