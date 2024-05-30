import sys
import configparser
import os

sys.path.append("src")


from controller.database_manager import DatabaseManager
import psycopg2

# Se crea una instancia de DatabaseManager para interactuar con la base de datos
db = DatabaseManager()

class Usuario:
    @classmethod
    def create(cls, table, data):
        """
        Crea un nuevo usuario en la base de datos.

        Args:
            table (str): Nombre de la tabla en la que se insertarán los datos del usuario.
            data (dict): Datos del usuario a insertar en la base de datos.

        Returns:
            bool: True si el usuario se crea correctamente, False si hay un error.
        """
        try:
            db.insert_data(table, data)
            print("Usuario creado correctamente.")
            return True
        except Exception as e:
            print(f"Error al crear el usuario: {e}")
            return False

    @classmethod
    def find_by_credentials(cls, id_usuario, contrasena):
        """
        Busca un usuario por sus credenciales en la base de datos.

        Args:
            id_usuario (str): Identificador único del usuario.
            contrasena (str): Contraseña del usuario.

        Returns:
            list: Una lista de tuplas que contiene los datos del usuario encontrado.
        """
        query = f"SELECT * FROM usuario WHERE ID_usuario = '{id_usuario}' AND contrasena = '{contrasena}'"
        result = db.execute_query(query)
        return result
    
    @classmethod
    def get_field_by_id(cls, id_usuario, field_name):
        """
        Obtiene el valor de un campo específico para un usuario dado su ID.

        Args:
            id_usuario (str): Identificador único del usuario.
            field_name (str): Nombre del campo que se desea obtener.

        Returns:
            str: El valor del campo especificado para el usuario, None si hay un error.
        """
        query = f"SELECT {field_name} FROM usuario WHERE id_usuario = '{id_usuario}'"
        print(query)  # Esto puede ser útil para depurar
        try:
            result = db.execute_query(query)
            if result:
                return result[0][0]  # Se asume que el campo es el primer valor de la primera fila del resultado
            else:
                return None
        except Exception as e:
            print(f"Error al obtener el campo {field_name} para el usuario {id_usuario}: {e}")
            return None
