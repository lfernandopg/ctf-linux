# Makefile para el Desafío 3
# OBJETIVO: Repara las 2 reglas rotas (main.o, impresor.o).

CC=gcc
CFLAGS=-Wall -g
OBJETOS=main.o impresor.o
EJECUTABLE=programa_final

LIBS=-L. -lflag

all: $(EJECUTABLE)

$(EJECUTABLE): $(OBJETOS)
	$(CC) $(CFLAGS) -o $(EJECUTABLE) $(OBJETOS) $(LIBS)

main.o: main.c impresor.h
	

impresor.o: impresor.c impresor.h flag_secreta.h
	

clean:
	rm -f $(OBJETOS) $(EJECUTABLE)
