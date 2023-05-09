import tkinter as tk
import mysql.connector
import csv


class Produits:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="velvet",
            database="magasin"
        )
        self.mycursor = self.db.cursor()
        

def create(self, nom, description, prix, quantite, id_categorie):
    sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, description, prix, quantite, id_categorie)
    self.mycursor.execute(sql, val)
    self.db.commit()
    print(self.mycursor.rowcount, "enregistrement inséré.")
    
def read(self):
    self.mycursor.execute("SELECT * FROM produit")
    result = self.mycursor.fetchall()
    for row in result:
        print(row)
        
def update(self, id, nom, description, prix, quantite, id_categorie):
    sql = "UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s"
    val = (nom, description, prix, quantite, id_categorie, id)
    self.mycursor.execute(sql, val)
    self.db.commit()
    print(self.mycursor.rowcount, "enregistrement(s) mis à jour.")

def delete(self, id):
    sql = "DELETE FROM produit WHERE id = %s"
    val = (id,)
    self.mycursor.execute(sql, val)
    self.db.commit()
    print(self.mycursor.rowcount, "enregistrement(s) supprimé(s).")

class Categorie:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="velvet",
            database="magasin"
        )
        self.mycursor = self.db.cursor()
        self.mycursor.execute("SELECT COUNT(id) FROM categorie")
        result = self.mycursor.fetchone()
        print("nombre de catégories:", result[0])

    
def create(self, nom):
    sql = "INSERT INTO categorie nom) VALUES (%s)"
    val = (nom,)
    self.mycursor.execute(sql, val)
    self.db.commit()
    print(self.mycursor.rowcount, "enregistrement inséré.")
    
def read(self):
    self.mycursor.execute("SELECT * FROM magasin")
    result = self.mycursor.fetchall()
    for row in result:
        print(row)

def update(self, id, nom):
    sql = "UPDATE categorie SET nom = %s WHERE id = %s"
    val = (nom, id)
    self.mycursor.execute(sql, val)
    self.db.commit()
    print(self.mycursor.rowcount, "enregistrement(s) modifié(s)")


def delete(self, id):
    sql = "DELETE FROM categorie WHERE id = %s"
    val = (id,)
    self.mycursor.execute(sql, val)
    self.db.commit()
    print(self.mycursor.rowcount, "enregistrement(s) supprimé(s)")


window = tk.Tk()
window.title("Magasin Database")
# create the widgets for the window
nom_label = tk.Label(window, text="nom")
nom_entry = tk.Entry(window)
description_label = tk.Label(window, text="description")
description_entry = tk.Entry(window)
prix_label = tk.Label(window, text="prix")
prix_entry = tk.Entry(window)
quantite_label = tk.Label(window, text="quantite")
quantite_entry = tk.Entry(window)
id_categorie_label = tk.Label(window, text="id_categorie")
id_categorie_entry = tk.Entry(window)
add_button = tk.Button(window, text="Add", command=Produits)

# position the widgets on the window
nom_label.grid(row=0, column=0)
nom_entry.grid(row=0, column=1)
description_label.grid(row=1, column=0)
description_entry.grid(row=1, column=1)
prix_label.grid(row=2, column=0)
prix_entry.grid(row=2, column=1)
quantite_label.grid(row=3, column=0)
quantite_entry.grid(row=3, column=1)
id_categorie_label.grid(row=4, column=0)
id_categorie_entry.grid(row=4, column=1)
add_button.grid(row=5, column=1)


# establish MySQL connection and cursor
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="magasin"
)
cursor = db.cursor()

# execute SQL query to select data from table
cursor.execute("SELECT * FROM produit")

# get all rows of data from cursor
rows = cursor.fetchall()

# open CSV file in write mode
with open("produit.csv", "w", newline="") as csvfile:
    # create CSV writer
    writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # write header row
    writer.writerow(["id", "nom", "description","prix", "id_categorie"])
    
    # write data rows
    for row in rows:
        writer.writerow(row)

# close cursor and MySQL connection
cursor.close()
db.close()

#Sur le tableau de bord, la liste complète des produits en stock sont affichés. L’utilisateur
#doit avoir la possibilité d’ajouter un produit, de supprimer un produit et de modifier le
#produit (stock, prix, ...).

# Open the CSV file and read its contents
with open('produit.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    rows = list(reader)

# Create a listbox to display the contents of the CSV file
listbox = tk.Listbox(window)
for row in rows:
    listbox.insert(tk.END, ', '.join(row))

# Add the listbox to the window and pack it
listbox.pack()




# Run the window
window.mainloop()




