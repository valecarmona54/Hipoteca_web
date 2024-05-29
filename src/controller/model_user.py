import sys
import configparser
import os
sys.path.append("src")

from controller.database_manager import DatabaseManager
import psycopg2

# Leer archivo de configuración
config_file = os.path.join(os.path.dirname(__file__), 'config.cfg')  # Ruta del archivo config.cfg
config = configparser.ConfigParser()
config.read(config_file)

# Imprimir el contenido de config para verificar si se leyó correctamente
print(config)

# Obtener la configuración de la base de datos
try:
    PGHOST = config['database']['PGHOST']
    PGDATABASE = config['database']['PGDATABASE']
    PGUSER = config['database']['PGUSER']
    PGPASSWORD = config['database']['PGPASSWORD']
except KeyError as e:
    print(f"Error: La sección 'database' o alguna de sus claves no se encontró en el archivo de configuración: {e}")

# Crear una instancia de DatabaseManager con la configuración
db = DatabaseManager(host=PGHOST, database=PGDATABASE, user=PGUSER, password=PGPASSWORD)

class Usuario:
  
    @classmethod
    def create(cls, table, data):
        try:
            db.insert_data(table, data)
            print("Usuario creado correctamente.")
            return True
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return False

    @classmethod
    def find_by_credentials(cls, id_usuario, contrasena):
        query = f"SELECT * FROM usuario WHERE ID_usuario = '{id_usuario}' AND contrasena = '{contrasena}'"
        result = db.execute_query(query)
        return result
    
    @classmethod
    def get_field_by_id(cls, id_usuario, field_name):
        query = f"SELECT {field_name} FROM usuario WHERE id_usuario = '{id_usuario}'"
        print(query)
        try:
            result = db.execute_query(query)
            if result:
                return result[0][0]
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el campo {field_name} para el usuario {id_usuario}: {e}")
            return None