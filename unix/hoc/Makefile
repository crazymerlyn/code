default: build


build: y.tab.c
	gcc $< -o main -Wall -Wextra -Werror -pedantic -g

y.tab.c: hoc.y
	yacc $<

run: build
	./main

clean:
	rm -f main *.o y.tab.c

