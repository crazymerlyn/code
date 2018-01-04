
(*  Example cool program testing as many aspects of the code generator
    as possible.
 *)

class Main inherits IO {
  main():Object { let a: Int <- 2 in { a <- 3; out_int(a); } };
};
