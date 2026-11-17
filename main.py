from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar_aluno", methods=["POST"])
def cadastrar_aluno():
    #lógica do db
    return "Aluno cadastrado com sucesso! (Em construção)"

@app.route("/cadastrar_professor", methods=["POST"])
def cadastrar_professor():
    #lógica do db
    return "Professor cadastrado com sucesso! (Em construção)"

if __name__ == "__main__":
    app.run(debug=True)