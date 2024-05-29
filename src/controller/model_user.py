

import sys
sys.path.append("src")

from database_manager import DatabaseManager

import psycopg2
from controller import Secret


db = DatabaseManager()

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