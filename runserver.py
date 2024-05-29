from os import environ
import sys

# Añadir el directorio src al path
sys.path.append("src")

# Importar módulos necesarios
from controller.database_manager import DatabaseManager
from view_web import app

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
