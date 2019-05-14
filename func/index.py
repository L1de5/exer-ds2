from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def temp1():
    
    return render_template('form.html')

@app.route("/print", methods=['GET', 'POST'])
def print1():
    a = []
    a.append(request.form['username'])
    a.append(request.form['password'])
    return render_template('print.html', dados=a)

