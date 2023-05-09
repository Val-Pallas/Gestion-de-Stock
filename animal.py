import tkinter as tk
import mysql.connector
import csv

# create the tkinter window
window = tk.Tk()
window.title("Zoo Database")

# create a function to connect to the database
def connect_to_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="velvet",
        database="zoo"
    )
    return mydb

# create a function to insert a new animal into the database
def add_animal():
    # get the values entered by the user
    nom = nom_entry.get()
    race = race_entry.get()
    id_cage = id_cage_entry.get()
    ne = ne_entry.get()
    pays = pays_entry.get()

    # connect to the database
    mydb = connect_to_db()

    # insert the new animal
    mycursor = mydb.cursor()
    sql = "INSERT INTO animal (nom, race, id_cage, ne, pays) VALUES (%s, %s, %s, %s, %s)"
    val = (nom, race, id_cage, ne, pays)
    mycursor.execute(sql, val)
    mydb.commit()

    # close the database connection
    mydb.close()

def update(self, id, nom, race, id_cage, ne, pays):
        sql = "UPDATE emlpoye SET nom = %s, prenom =%s, salaire = %s WHERE id = %s"
        val = (nom, race, id_cage, ne, pays)
        self.mycursor.execute(sql, val)
        self.db.commit()
        print(self.mycursor.rowcount, "enregistrement(s) mis a jour.")
# create the widgets for the window
nom_label = tk.Label(window, text="nom")
nom_entry = tk.Entry(window)
race_label = tk.Label(window, text="race")
race_entry = tk.Entry(window)
id_cage_label = tk.Label(window, text="Cage ID")
id_cage_entry = tk.Entry(window)
ne_label = tk.Label(window, text="ne")
ne_entry = tk.Entry(window)
pays_label = tk.Label(window, text="pays")
pays_entry = tk.Entry(window)
add_button = tk.Button(window, text="Add", command=add_animal)

# position the widgets on the window
nom_label.grid(row=0, column=0)
nom_entry.grid(row=0, column=1)
race_label.grid(row=1, column=0)
race_entry.grid(row=1, column=1)
id_cage_label.grid(row=2, column=0)
id_cage_entry.grid(row=2, column=1)
ne_label.grid(row=3, column=0)
ne_entry.grid(row=3, column=1)
pays_label.grid(row=4, column=0)
pays_entry.grid(row=4, column=1)
add_button.grid(row=5, column=1)

# start the tkinter event loop
window.mainloop()

# establish MySQL connection and cursor
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="velvet",
    database="zoo"
)
cursor = db.cursor()

# execute SQL query to select data from table
cursor.execute("SELECT * FROM animal")

# get all rows of data from cursor
rows = cursor.fetchall()

# open CSV file in write mode
with open("animals.csv", "w", newline="") as csvfile:
    # create CSV writer
    writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # write header row
    writer.writerow(["id", "nom", "race", "id_cage", "ne", "pays"])
    
    # write data rows
    for row in rows:
        writer.writerow(row)

# close cursor and MySQL connection
cursor.close()
db.close()

#Sur le tableau de bord, la liste complète des produits en stock sont affichés. L’utilisateur
#doit avoir la possibilité d’ajouter un produit, de supprimer un produit et de modifier le
#produit (stock, prix, ...).

# Create a window
window = tk.Tk()

# Open the CSV file and read its contents
with open('file.csv', newline='') as csvfile:
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

