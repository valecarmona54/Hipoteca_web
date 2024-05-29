import unittest
import psycopg2
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import sys
sys.path.append("src")
from  src.controller.database_manager  import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        cls.db_manager = DatabaseManager()
        cls.db_manager.create_tables()
        cls.db_manager.delete_all_data()

    async def test_insert_data(self):
        # Caso de prueba normal
        data = {'id_usuario': 'test', 'contrasena': 'test',  'edad': 75, 'nombre_usuario': 'test', 'genero': 'test'}
        await self.db_manager.insert_data('usuario', data)
        result = await self.db_manager.get_data('usuario', 'test')
        self.assertEqual(result[0], tuple(data.values()))

        # Caso de prueba de error
        with self.assertRaises(psycopg2.errors.UniqueViolation):
            data = {'id_usuario': 'test', 'contrasena': 'test',  'edad': 75, 'nombre_usuario': 'test', 'genero': 'test'}
            await self.db_manager.insert_data('usuario', data)
            
    async def test_get_data(self):
        # Caso de prueba normal
        result = await self.db_manager.get_data('usuario', 'test')
        self.assertIsNotNone(result)

        # Caso de prueba de error
        with self.assertRaises(psycopg2.errors.UndefinedTable):
            await self.db_manager.get_data('non_existent_table', 'test')

    async def test_delete_data(self):
        # Caso de prueba normal
        await self.db_manager.delete_data('usuario', 'test')
        result = await self.db_manager.get_data('usuario', 'test')
        self.assertEqual(result, [])

        # Caso de prueba de error DUDOSO
        with self.assertRaises(psycopg2.errors.ForeignKeyViolation):
            await self.db_manager.delete_data('usuario', '5')

    async def test_update_data(self):
        # Caso de prueba normal

        data = {'id_usuario': 'test', 'contrasena': 'test',  'edad': 75, 'nombre_usuario': 'test', 'genero': 'test'}
        await self.db_manager.insert_data('usuario', data)

        data = {'edad': 80}
        await self.db_manager.update_data('usuario', data, 'test')
        result = await self.db_manager.get_data('usuario', 'test')
        self.assertEqual(result[0][2], 80)

        # Caso de prueba de error
        with self.assertRaises(psycopg2.errors.NotNullViolation):
            data = {'edad': None}
            await self.db_manager.update_data('usuario', data, 'test')

if __name__ == '__main__':
    unittest.main()
