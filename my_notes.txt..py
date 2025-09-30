# Escritura de Archivo de Texto

# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales usando write()
archivo.write("La identificación de activos es clave para proteger la información crítica de una organización.\n")
archivo.write("Automatizar procesos con Python y Excel reduce errores y mejora la eficiencia operativa.\n")
archivo.write("Los métodos write() y readline() son muy útiles.\n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura de Archivo de Texto

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos línea por línea usando readline() dentro de un bucle
print("Contenido del archivo:")
while True:
    linea = archivo.readline()  # Lee una línea
    if not linea:               # Si no hay más líneas, termina el bucle
        break
    print(linea.strip())        # Mostramos la línea en consola sin el salto de línea

# Cerramos el archivo después de leer
archivo.close()
