from flask import Flask, render_template, request

import sqlite3

pf = Flask(__name__)

mediaf = 0

def valida_senha(nome,senha):

    conn = sqlite3.connect('pf.db') 
    c = conn.cursor()
    j = c.execute("SELECT * FROM alunos where nome = '"+nome+"' and dre ='"+senha+"'").fetchall()
                         
    conn.commit()
    
    print(j)
    
    if j:
        return render_template("calculapf.html")
    else:
        return render_template("index.html", erro="Login Incorreto")
    
    print(linha)
  
@pf.route("/")
def hello_world():
    return render_template("index.html")

@pf.route("/login", methods =["POST"])
def login():

    if request.method == "POST":
        nome = request.form["nome"]
        senha = request.form["senha"]
        return valida_senha(nome, senha) 

    else:
        print ("Deu ruim")
        return "RUIM"

def calcula_media(p1,p2):
    if (p1+p2)/2 >= 7: 
        mediaf = (p1+p2)/2
        return render_template("aprovado.html", media=(p1+p2)/2)
    elif (p1+p2)/2 < 3: 
        mediaf = (p1+p2)/2
        return render_template("reprovado.html", media=(p1+p2)/2)
    else:
        mediaf = (p1+p2)/2 
        return render_template("final.html") 

@pf.route("/media", methods =["POST"])
def media():

    if request.method == "POST":
        p1 = int(request.form["p1"])
        p2 = int(request.form["p2"])
        return calcula_media(p1,p2) 

    else:
        print ("Deu ruim")
        return "RUIM"

def calcula_final(mediaf,p3):

    if (mediaf+p3)/2 >= 5: return render_template("aprovado.html",media=(mediaf+p3)/2)
    else: return render_template("reprovado.html", media=(mediaf+p3)/2) 


@pf.route("/final", methods =["POST"])
def final():

    if request.method == "POST":
        p3 = int(request.form["p3"])
        return calcula_final(mediaf,p3) 

    else:
        print ("Deu ruim")
        return "RUIM"
        

    

pf.run()
