import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nicolas',
    database='laplateforme'
)

cursor = bd.cursor()

req = 'SELECT SUM(superficie) AS superficie_totale FROM etage'
cursor.execute(req)
datas = cursor.fetchall()
result = "La superficie de la plateforme est de " + str(datas[0][0]) + " m2"
print(result)
cursor.close()