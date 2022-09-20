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

def calcula_media(p1,p2):
    if (p1+p2)/2 >= 7: return render_template("aprovado.html")
    elif (p1+p2)/2 < 3: return render_template("reprovado.html")
    else: return render_template("final.html") 

@pf.route("/media", methods =["POST"])
def media():

    if request.method == "POST":
        p1 = int(request.form["p1"])
        p2 = int(request.form["p2"])
        return calcula_media(p1,p2) 

    else:
        print ("Deu ruim")
        return "RUIM"

def calcula_final(p1,p2,p3):

    if (((p1+p2)/2)+p3)/2 >= 5: return render_template("aprovado.html")
    else: return render_template("reprovado.html") 


@pf.route("/final", methods =["POST"])
def final():

    if request.method == "POST":
        p1 = int(request.form["p1"])
        p2 = int(request.form["p2"])
        p3 = int(request.form["p3"])
        return calcula_final(p1,p2,p3) 

    else:
        print ("Deu ruim")
        return "RUIM"
        

    

pf.run()
