import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "R00t",
    database = "LaPlateforme"
)

cursor = db.cursor()
cursor.execute("select sum(superficie) from etage")

res = cursor.fetchone()
print("La superficie de LaPlateforme est de", res[0], "m²")