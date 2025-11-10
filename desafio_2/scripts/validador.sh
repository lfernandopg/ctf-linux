#!/bin/bash
PASSWORD_SECRETO="linux_es_poder"
FLAG_CODIFICADA="RkxBR3tFbF9HdTRyZDE0bl9kM2xfU2gzbGx9"

if [ "$1" == "$PASSWORD_SECRETO" ]; then
echo "¡Acceso Concedido!"
echo "Has demostrado entender shell scripts."
echo "La segunda flag es:"
echo "$FLAG_CODIFICADA" | base64 --decode
echo ""
echo "Pista para el Desafío 3: El archivo 'desafio_3.zip' te espera."
echo "Usa la flag que acabas de obtener como contraseña."
echo "Revisa el directorio 'desafio_3'. Hay un proyecto de C que necesita ser 'construido'."
else
echo "Acceso Denegado."
echo "Debes ejecutar este script con la contraseña correcta como primer argumento."
echo "Ejemplo: ./validador.sh [contraseña]"
echo "(Pista: ¡Lee el código fuente de este script!)"
fi
