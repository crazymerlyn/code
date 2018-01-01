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


// The following methods emit code for
// constants and global declarations.

   void code_global_data();
   void code_global_text();
   void code_bools(int);
   void code_select_gc();
   void code_constants();
   void code_prototypes();
   void code_class_nametab();
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
   void set_tags();
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
   std::vector<std::string> dispatch_names;
   std::map<Symbol, int> dispatch_pos;
   std::vector<Symbol> attrs;

public:
   CgenNode(Class_ c,
            Basicness bstatus,
            CgenClassTableP class_table);

   void add_child(CgenNodeP child);
   List<CgenNode> *get_children() { return children; }
   void set_parentnd(CgenNodeP p);
   void set_tag(int tag);
   int get_tag();
   int get_size();
   int get_attr_offset(Symbol attr);
   bool is_basic() { return basic_status == Basic; }
   void build_dispatch_table();
   void code_prototype(ostream& stream);
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
    std::vector<Symbol> attrs;
    Context* parent;
    int stack_max;

    public:
    Context(std::vector<Symbol> attrs): attrs(attrs), parent(NULL) {};
    Context(Context* parent, Formals formals): parent(parent) {
        for (int i = 0; i < formals->len(); ++i) {
            auto formal = formals->nth(i);
            mapping[formal->get_name()] = std::make_pair(SP, i);
        }
    }
    Context(Context* parent, Symbol name): parent(parent) {
        mapping[name] = std::make_pair(SP, 0);
    }
    std::pair<std::string, int> get_mapping(Symbol name, int top=0) {
        if (mapping.find(name) != mapping.end()) {
            auto res = mapping[name];
            res.second += top;
            return res;
        }
        if (parent) return parent->get_mapping(name, top + mapping.size());
        for (size_t i = 0; i < attrs.size(); ++i) {
            if (attrs[i] == name) return std::make_pair(SELF, i + DEFAULT_OBJFIELDS);
        }
        assert(false);
    }
};
