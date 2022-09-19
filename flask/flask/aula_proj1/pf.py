from flask import Flask, render_template, request

pf = Flask(__name__)

def valida_senha(nome,senha):

    #abrindo arquivo
    arquivo = open("./senha.txt","r+")

    #vendo se o candango já está no arquivo
    
    linha = arquivo.readlines()

    teste = nome+"-"+senha+"\n"

    if teste in linha:
        return render_template("calculapf.html")
    else:
        return render_template("badlogin.html")
    
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
    

pf.run()
