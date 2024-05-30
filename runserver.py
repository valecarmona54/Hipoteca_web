

from os import environ
from flask import Flask
import sys

# Añadir el directorio src al path
sys.path.append("src")
from flask import template_rendered
from view_web import views

# Importar módulos necesarios
from controller.database_manager import DatabaseManager

app =Flask(__name__)

if __name__ == '__main__':
    # Crear una instancia de DatabaseManager y crear tablas
    db = DatabaseManager()
    db.create_tables()

    # Configurar y ejecutar el servidor
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
