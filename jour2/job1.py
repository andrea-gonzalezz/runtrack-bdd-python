import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mellon2707!',
    database = "laplateforme"
)

cursor = db.cursor()
requete = 'SELECT * FROM etudiants' 
cursor.execute(requete)
datas = cursor.fetchall()

print(datas)
cursor.close()