import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nicolas',
    database = 'laplateforme'
    )

cursor = bd.cursor()

req = 'select * from salles'

cursor.execute(req)
datas = cursor.fetchall()

print(datas)
cursor.close()