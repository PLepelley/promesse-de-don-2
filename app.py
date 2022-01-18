from flask import Flask, render_template, request
import data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/add", methods=["GET"])
def add():
    civilite = request.values.get("user_civilite")
    name = request.values.get("user_name")
    first_name = request.values.get("user_first_name")
    birth = request.values.get("user_birth")
    adress = request.values.get("user_adress")
    cp = request.values.get("user_cp")
    country = request.values.get("user_country")
    mail = request.values.get("user_email")
    phone = request.values.get("user_phone")
    answer = request.values.get("user_answer")
    comment = request.values.get("user_comment")

    # ---------------------------------------------
    region = request.values.get("user_region")
    blood = request.values.get("user_blood")
    # print("blood =" + blood)

    data.set_user(
        civilite,
        name,
        first_name,
        birth,
        adress,
        cp,
        country,
        phone,
        mail,
        answer,
        comment,
    )
    data.set_don(name, first_name, region, blood)

    datas = data.get_users()
    total_sang = data.somme()

    return render_template("add.html", donateurs=datas, somme_sang=total_sang)


@app.route("/donateurs")
def donateurs():
    datas = data.get_users()
    total_sang = data.somme()
    return render_template("donateurs.html", donateurs=datas, somme_sang=total_sang)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
