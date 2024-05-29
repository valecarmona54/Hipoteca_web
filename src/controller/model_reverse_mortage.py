import sys
sys.path.append("src")

from database_manager import DatabaseManager


db = DatabaseManager()

class model_reverse:
    @classmethod
    def create(cls, table, data):
        try:
            db.insert_data(table, data)
            print("Hipoteca Inversa Vitalicia creada correctamente.")
            return True
        except Exception as e:
            print(f"Error al crear la Hipoteca Inversa Vitalicia: {e}")
            return False

    @classmethod
    def find_by_credentials(cls, id_usuario):
        query = f"SELECT * FROM mortgage_lifetime_inverse WHERE id_usuario = '{id_usuario}"
        result = db.execute_query(query)
        return result
    

class data_reverse:
    @classmethod
    def get_info(cls, table, idusuario):
        try:
            db.get_data(table, idusuario)
            return True
        except Exception as e:
            print(f"Ah ocurrido un error: {e}")
            return False