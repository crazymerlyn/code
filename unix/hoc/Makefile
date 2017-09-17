default: build


build: generate_header hoc.o symbol.o math.o init.o hoc.h
	gcc *.o -o main -Wall -Wextra -Werror -pedantic -g -lm

generate_header: hoc.y
	yacc -d $<

run: build
	./main

clean:
	rm -f main *.o y.tab.*

