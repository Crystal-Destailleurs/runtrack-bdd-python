import mysql.connector

HOST="localhost"
USER="root"
PW="123soleil"
DB="laplateforme"


connection = mysql.connector.connect(host=HOST, user=USER, password=PW, database=DB)

if connection.is_connected():
    print("Connexion à la base de données réusssie.")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM etudiant")

    result = cursor.fetchall()

    print("Liste des étudiants :")
    print(result)
    for student in result:
        print(student)

    cursor.close()
    connection.close()
    print("Connexion à la base de données fermée.")
