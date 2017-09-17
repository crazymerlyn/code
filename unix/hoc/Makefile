default: build


build: hoc.o
	gcc $< -o main -Wall -Wextra -Werror -pedantic -g -lm

run: build
	./main

clean:
	rm -f main *.o

