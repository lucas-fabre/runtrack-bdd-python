import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "R00t",
    database = "LaPlateforme"
)

cursor = db.cursor()
cursor.execute("select sum(capacite) from salles")

res = cursor.fetchone()
print("La capacité total des salles est de", res[0], "personnes")