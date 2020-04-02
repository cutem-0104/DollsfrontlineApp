import os
import mysql.connector as mydb


class MySqlService():    
    def connect(self):
        connect_args = {
            'host': os.environ.get('MYSQL_SERVER'),
            'port': 3306,
            'user': 'root',
            'password': os.environ.get('MYSQL_PASSWORD'),
            'database': 'dollsfrontline'
        }
        return mydb.connect(**connect_args)

    def is_connected(self):
        db = self.connect()
        result = db.is_connected()
        db.close()
        return result

    def select_all(self):
        select = 'SELECT * FROM dolls'
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(select)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    def select_count(self):
        select = 'SELECT count(*) FROM dolls'
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(select)
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result
