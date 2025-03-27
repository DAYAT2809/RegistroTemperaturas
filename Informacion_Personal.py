# Crear el diccionario con la información ficticia
informacion_personal =\
    {
    "nombre": "Stalin Rivera",
    "edad": 33,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
    }

# Acceder al valor de la clave "ciudad" y modificarla

informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor para el número de teléfono

informacion_personal["telefono"] = "0998765432"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

else:
    print("La clave 'telefono' ya existe.")

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el resultado final
print(informacion_personal)
