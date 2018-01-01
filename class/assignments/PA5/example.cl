
(*  Example cool program testing as many aspects of the code generator
    as possible.
 *)

class Main {
  b: Int <- 45;
  a: Int <- b;
  main():Int { f () };
  f (): Int { let c: Int <- 4 in let d: Int <- c in d};
};

class B {
a: Bool;
};
