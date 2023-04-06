import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mellon2707!',
    database = "laplateforme"
)

cursor = db.cursor()

cursor.execute("select SUM(capacite) as capacité_totale from salles;")
datas = cursor.fetchall()

print("L'ecole La Plateforme a", datas[0], "m2")


cursor.close()
db.close()