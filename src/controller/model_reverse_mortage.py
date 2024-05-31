import sys
sys.path.append("src")  

from controller.database_manager import DatabaseManager  

# Instancia del gestor de la base de datos
db = DatabaseManager()

class model_reverse:
    @classmethod
    def create(cls, table, data):
        """
        Método estático para crear un registro en la base de datos.
        
        Args:
            table (str): Nombre de la tabla en la base de datos.
            data (dict): Datos a insertar en la tabla.
            
        Returns:
            bool: True si la inserción fue exitosa, False en caso contrario.
        """
        try:
            db.insert_data(table, data)  # Inserta los datos en la tabla utilizando el gestor de la base de datos
            print("Hipoteca Inversa Vitalicia creada correctamente.")
            return True
        except Exception as e:
            print(f"Error al crear la Hipoteca Inversa Vitalicia: {e}")
            return False

    @classmethod
    def find_by_credentials(cls, id_usuario):
        """
        Método estático para buscar registros por credenciales de usuario.
        
        Args:
            id_usuario (str): ID del usuario para buscar en la tabla.
            
        Returns:
            list: Lista de resultados de la consulta.
        """
        query = f"SELECT * FROM mortgage_lifetime_inverse WHERE id_usuario = '{id_usuario}"  # Construye la consulta SQL
        result = db.execute_query(query)  # Ejecuta la consulta utilizando el gestor de la base de datos
        return result
    

class data_reverse:
    @classmethod
    def get_info(cls, table, idusuario):
        """
        Método estático para obtener información de la base de datos.
        
        Args:
            table (str): Nombre de la tabla en la base de datos.
            idusuario (str): ID del usuario para buscar en la tabla.
            
        Returns:
            bool: True si la consulta fue exitosa, False en caso contrario.
        """
        try:
            db.get_data(table, idusuario)  # Obtiene los datos de la tabla utilizando el gestor de la base de datos
            return True
        except Exception as e:
            print(f"Ah ocurrido un error: {e}")
            return False
