import os

print("¡Felicidades por completar el CTF!")
print("Vamos a generar tu archivo de entrega.")
print("Por favor, introduce las 4 flags que encontraste.")

flag1 = input("Introduce la Flag 1: ")
flag2 = input("Introduce la Flag 2: ")
flag3 = input("Introduce la Flag 3: ")
flag4 = input("Introduce la Flag 4: ")

estudiante = input("Introduce tu nombre completo: ")
cedula = input("Introduce tu cédula: ")

# Crear el contenido del archivo
nombre_archivo = f"entrega_ctf_{cedula}.txt"
# Se corrige la indentación del string multi-línea
contenido = f"""--- Entrega CTF Linux ---
Estudiante: {estudiante}
Cédula: {cedula}

--- Flags Encontradas ---
Flag 1: {flag1}
Flag 2: {flag2}
Flag 3: {flag3}
Flag 4: {flag4}
"""

# Guardar el archivo
try:
    # Estas líneas ahora están indentadas correctamente
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"\n¡Éxito!")
    print(f"Se ha creado tu archivo de entrega: '{nombre_archivo}'")
    print("Por favor, sube este archivo a la plataforma del curso para ser evaluado.")
except Exception as e:
    # Esta línea ahora está indentada correctamente
    print(f"\nError: No se pudo crear el archivo de entrega.")
    print(f"Detalle: {e}")
