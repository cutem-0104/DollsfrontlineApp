import os
import mysql.connector as mydb
from src.service.dolls_service import DollsYamlRepository


connect_args = {
    'host': os.environ.get('MYSQL_SERVER'),
    'port': 3306,
    'user': 'root',
    'password': os.environ.get('MYSQL_PASSWORD'),
    'database': 'dollsfrontline'
}

db = mydb.connect(**connect_args)
cursor = db.cursor()

select = 'SELECT count(*) FROM dolls'
delete = 'DELETE FROM dolls'
insert = 'INSERT INTO ' + \
    'dolls (name, type, star, time, link_url, how_to_get, image_url) ' + \
    'VALUES (%s, %s, %s, %s, %s, %s, %s)'

dolls = DollsYamlRepository().result

# cursor.execute(delete)

# for d in dolls:
#     params = (d.name, d.type, d.star, str(d.time.strftime('%H:%M:%S')),
#     d.link_url, d.how_to_get, d.image_url)
#     cursor.execute(insert, params)
# db.commit()

result = cursor.execute(select)
print(cursor.fetchone())

cursor.close()
db.close()
