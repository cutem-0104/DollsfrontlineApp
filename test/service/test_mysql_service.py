import unittest
import os
import mysql.connector as mydb


class TestMysqlService(unittest.TestCase):
    def test_mysql_connection(self):
        connect_args = {
            'host': os.environ.get('MYSQL_SERVER'),
            'port': 3306,
            'user': 'root',
            'password': os.environ.get('MYSQL_PASSWORD'),
            'database': 'dollsfrontline'
        }
        
        db = mydb.connect(**connect_args)
        self.assertTrue(db.is_connected())
        db.close()


if __name__ == '__main__':
    unittest.main()
