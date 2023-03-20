import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nicolas',
    database = 'laplateforme'
    )

cursor = bd.cursor()

req = 'select * from etudiants'

cursor.execute(req)
datas = cursor.fetchall()

print(datas)
cursor.close()