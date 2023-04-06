import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mellon2707!',
    database = "laplateforme"
)

cursor = db.cursor()

cursor.execute('SELECT nom, capacite FROM salles')
datas = cursor.fetchall()

print(datas)
cursor.close()