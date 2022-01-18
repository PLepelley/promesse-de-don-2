import queue
import mysql.connector as msql

bdd = None
cursor = None


def connexion():
    global bdd
    global cursor

    bdd = msql.connect(
        user="root",
        password="root",
        host="localhost",
        port="8081",
        database="promesse_don",
    )
    cursor = bdd.cursor()


def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()


def set_user(
    user_civilite,
    user_name,
    user_first_name,
    user_birth,
    user_adress,
    user_cp,
    user_country,
    user_email,
    user_phone,
    user_answer,
    user_comment,
):
    global bdd
    global cursor

    connexion()

    query = (
        "INSERT INTO donateur(user_civilite, user_name, user_first_name, user_birth, user_adress, user_cp, user_country, user_email, user_phone, user_answer, user_comment) VALUES ('"
        + user_civilite
        + "','"
        + user_name
        + "','"
        + user_first_name
        + "','"
        + user_birth
        + "','"
        + user_adress
        + "','"
        + user_cp
        + "','"
        + user_country
        + "','"
        + user_phone
        + "','"
        + user_email
        + "','"
        + user_answer
        + "','"
        + user_comment
        + "');"
    )

    cursor.execute(query)
    bdd.commit()

    deconnexion()


def get_user_id(user_name, user_first_name):
    global cursor

    connexion()

    query = (
        "SELECT id_user FROM donateur WHERE user_name= '"
        + user_name
        + "' AND user_first_name= '"
        + user_first_name
        + "';"
    )

    cursor.execute(query)

    id_user = 0
    for enregistrement in cursor:
        id_user = enregistrement[0]

    return id_user


def set_don(user_name, user_first_name, user_region, user_blood):
    global bdd
    global cursor

    connexion()

    id = get_user_id(user_name, user_first_name)
    print(type(id))
    print(id)
    query = (
        "INSERT INTO don(user_region, user_blood, id_user) VALUES ('"
        + user_region
        + "','"
        + user_blood
        + "','"
        + str(id)
        + "');"
    )

    cursor.execute(query)
    bdd.commit()

    deconnexion()


def get_users():
    global cursor

    connexion()
    query = "SELECT donateur.user_name, donateur.user_first_name, don.user_blood, donateur.user_email FROM donateur JOIN don ON donateur.id_user = don.id_user"
    cursor.execute(query)
    donateurs = []

    for enregistrement in cursor:
        donateur = {}
        donateur["nom"] = enregistrement[0]
        donateur["prenom"] = enregistrement[1]
        donateur["sang"] = enregistrement[2]
        donateur["mail"] = enregistrement[3]
        donateurs.append(donateur)

    deconnexion()

    return donateurs


def somme():
    global cursor

    connexion()

    query = "SELECT user_blood FROM don"
    cursor.execute(query)

    total = 0

    for enregistrement in cursor:
        total = total + enregistrement[0]

    deconnexion()

    return total
