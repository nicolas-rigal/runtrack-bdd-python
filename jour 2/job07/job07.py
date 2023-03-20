import mysql.connector

bd = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Nicolas',
    database = 'laplateforme'
    )


cursor = bd.cursor()

req = 'SELECT SUM(capacite) AS capacite_totale FROM salles'
cursor.execute(req)
datas = cursor.fetchall()
result = "La capacité de toutes le salles est de " + str(datas[0][0])
print(result)
cursor.close()