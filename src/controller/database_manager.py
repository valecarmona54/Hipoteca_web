# database_manager.py

import psycopg2
from configparser import ConfigParser

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        # Lee los datos de conexi n desde el archivo secret.config
        config = ConfigParser()
        config.read('secret.cfg')

        """"
        PGHOST='ep-rapid-fire-a56s2rby.us-east-2.aws.neon.tech'
        PGDATABASE='hipoteca'
        PGUSER='tarjeta_credito_owner'
        PGPASSWORD='j0dkN8AgLCsn'
        """
        self.host = config.get('database', 'PGHOST')
        self.database = config.get('database', 'PGDATABASE')
        self.user = config.get('database', 'PGUSER')
        self.password = config.get('database', 'PGPASSWORD')

        # Establece la conexi n a la base de datos
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            sslmode="require"
        )

    def execute_query(self, query):
        # Ejecuta una consulta en la base de datos
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def insert_data(self, table, data):
        # Inserta datos en una tabla espec fica
        with self.connection.cursor() as cursor:
            columns = ', '.join(data.keys())
            values = ', '.join(f"'{value}'" for value in data.values())
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            print(query)
            cursor.execute(query)
        self.connection.commit()
        
    def get_data(self, table, user_id):
        with self.connection.cursor() as cursor:
            query = f"SELECT * FROM {table} WHERE id_usuario = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()
        return result

    def delete_data(self, table, record_id):
        try:
            with self.connection.cursor() as cursor:
                query = f"DELETE FROM {table} WHERE id = %s"
                cursor.execute(query, (record_id,))
            self.connection.commit()
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
            self.connection.rollback()
            raise e

    def update_data(self, table, data, record_id):
        try:
            with self.connection.cursor() as cursor:
                set_clause = ', '.join(f"{key} = %s" for key in data.keys())
                values = list(data.values())
                values.append(record_id)
                query = f"UPDATE {table} SET {set_clause} WHERE id_usuario = %s"
                cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
            self.connection.rollback()
            raise e

    def create_tables(self):
        create_table_queries = [
            """
            CREATE TABLE IF NOT EXISTS mortgage_lifetime_inverse (
                id SERIAL PRIMARY KEY,
                id_usuario VARCHAR(10),
                total_amount DECIMAL,
                interest DECIMAL,
                interest_housing DECIMAL,
                age INT,
                result DECIMAL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS mortgage_single_reverse (
                id SERIAL PRIMARY KEY,
                id_usuario VARCHAR(10),
                total_amount DECIMAL,
                interest_housing DECIMAL,
                result DECIMAL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS mortgage_temporary_reverse (
                id SERIAL PRIMARY KEY,
                id_usuario VARCHAR(10),
                total_amount DECIMAL,
                interest DECIMAL,
                interest_housing DECIMAL,
                quotas INT,
                result DECIMAL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario VARCHAR(10) PRIMARY KEY,
                contrasena VARCHAR(50),
                edad INT,
                nombre_usuario VARCHAR(100),
                genero VARCHAR(10)
            );
            """
        ]

        for query in create_table_queries:           
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
    
    def delete_all_data(self):
        tables = [
            'mortgage_lifetime_inverse',
            'mortgage_single_reverse',
            'mortgage_temporary_reverse',
            'usuario'
        ]
        try:
            with self.connection.cursor() as cursor:
                for table in tables:
                    query = f"DELETE FROM {table}"
                    cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print(f"Error al eliminar todos los datos: {e}")
            self.connection.rollback()
            raise e

    def close_connection(self):
        self.connection.close()


