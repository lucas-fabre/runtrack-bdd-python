import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "R00t",
    database = "LaPlateforme"
)

cursor = db.cursor()
cursor.execute("select * from etudiants")

res = cursor.fetchall()
print(res)