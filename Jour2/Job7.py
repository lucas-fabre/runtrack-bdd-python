import mysql.connector

# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "R00t",
#     database = "entreprise"
# )

# cursor = db.cursor(buffered = True)
# cursor2 = db.cursor(buffered = True)

# cursor.execute("select * from employes where salaire > 3000")
# cursor2.execute("select * from employes inner join services on employes.id_service = services.id")

# res = cursor.fetchall()
# res2 = cursor2.fetchall()
# print("Les personnes ayant un salaire de plus de 3000 euros sont :", res)
# print("Les emmployés et leurs services dans l'entreprise sont : ", res2)

class CRUD:
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "R00t",
        database = "entreprise"
        )
        self.cursor = self.db.cursor()

    def create(self, nom, prenom, salaire, id_service):
        self.cursor.execute(f"insert into employes (nom, prenom, salaire, id_service) \
                       values \
                       ('{nom}', '{prenom}', {salaire}, {id_service}); ")
        
        self.cursor.close()

    # def read(self):

    # def update(self):

    # def delete(self):

crud = CRUD()
crud.create('Pichard', 'Pierre', 2500, 1)