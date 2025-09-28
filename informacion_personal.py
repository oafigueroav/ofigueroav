# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "oscar figueroa",
    "edad": 30,
    "ciudad": "Guayaquil",
    "profesion": "tecnologo"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para "profesion" (ya existe, pero se actualiza)
informacion_personal["profesion"] = "tecnologo en mantenimiento en equipo de computo"

# Verificar si la clave "telefono" existe, y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985364198"

# Eliminar la clave "edad"
informacion_personal.pop("30", None)

# Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
