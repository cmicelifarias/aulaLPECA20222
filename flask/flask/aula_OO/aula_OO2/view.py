from flask import Flask, render_template, url_for, request
from control import qrcode_gen

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("vcard.html")

@app.route("/vcard", methods = ["POST"])
def vcard():
    nome = request.form["nome"]
    qrcode_gen(nome)
    return render_template("qrcode.html")
