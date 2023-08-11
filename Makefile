CC=gcc
CFLAGS=-I.

all: integral

integral: integral.c
	$(CC) -o integral integral.c $(CFLAGS)

.PHONY: clean

clean:
	rm -f integral