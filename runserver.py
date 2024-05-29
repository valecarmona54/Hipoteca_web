from os import environ
import sys
sys.path.append("src")

from src.controller.database_manager import DatabaseManager

from src.view_web import app

if __name__ == '__main__':
    
    from src.controller.database_manager import DatabaseManager
    
    db = DatabaseManager()    
    db.create_tables()

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)