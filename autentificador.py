#!/usr/bin/env python3

import mysql.connector
import datetime

def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Establecer conexión con la base de datos
    db = mysql.connector.connect(
        host="localhost",
        user="administrador",
        password="tecsup123",
        database="credenciales_db"
    )

    # Crear un cursor para realizar consultas
    cursor = db.cursor()

    # Consulta para verificar las credenciales
    query = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
    values = (username, password)

    # Ejecutar la consulta
    cursor.execute(query, values)

    # Obtener el resultado de la consulta
    result = cursor.fetchone()

    # Verificar si se encontraron coincidencias
    if result is None:
        print("Nombre de usuario o contraseña incorrectos.")
    else:
        print("Inicio de sesión exitoso!")

        # Actualizar la columna "ultima_sesion" con la fecha y hora actual
        update_query = "UPDATE usuarios SET ultima_sesion = %s WHERE username = %s"
        update_values = (datetime.datetime.now(), username)

        # Ejecutar la consulta de actualización
        cursor.execute(update_query, update_values)

        # Hacer commit para guardar los cambios en la base de datos
        db.commit()

    # Cerrar la conexión y el cursor
    cursor.close()
    db.close()
	
# Llamar a la función de login
login()