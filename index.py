from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/foi", methods=["GET", "POST"])
def tabela():
    dados = []
    n = request.form['nome']
    e = request.form['email']
    dados.append(n)
    dados.append(e)
    return render_template("table.html", dados=dados)

@app.route("/", methods=["GET", "POST"])
def formulario():
    
    return render_template("form.html")
