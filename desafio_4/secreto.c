#include <stdio.h>
#include <string.h>

// ESTE ES EL CÓDIGO FUENTE
// Verás esto, pero el binario 'secreto'
// fue compilado con un código diferente.

void funcion_peligrosa() {
// La flag está en la memoria, pero el programa nunca
// llegará a imprimirla.
char flag_final[] = "FLAG{...esto_es_un_senuelo...}";
char *puntero_nulo = NULL;

printf("Intentando acceder a memoria... esto no saldrá bien.\n");

// Aquí es donde el programa crashea (Segmentation Fault)
// al intentar escribir en la dirección 0x0.
strcpy(puntero_nulo, "hola");

// Esta línea nunca se ejecutará
printf("Si ves esto, eres un mago: %s\n", flag_final);
}
int main() {
printf("Bienvenido al desafío final.\n");
printf("La flag está dentro de 'funcion_peligrosa', pero... ¡boom!\n");
printf("Puedes ver el código en 'secreto.c' para ayudarte.\n");
funcion_peligrosa();
return 0;
}
