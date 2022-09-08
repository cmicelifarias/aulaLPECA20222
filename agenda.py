
agenda = {}

'''
A funcao action eh a primeira interface com o usuario

ela fa a pergunta pela opcoes e retorna uma string com a opcao desejada
'''

def action():

    return input("Digite a opcao desejada: (i)incluir, (d)deletar, (b) busca, (s) sair: ")      

'''
A funcao incluir cria um registro contendo
nome, email e telefone

'''

def incluir():

    print("Incluindo uma pessoa na minha agenda")
    nome = input("Digite o nome do contato ")
    email = input("Digite o email do contato ")
    tel = input("Digite o tel do contato ")
    temp = {nome:[email,tel]}
    #global agenda
    agenda.update(temp)
    '''
    for nome in temp:
        global agenda[nome] = temp[nome]
    '''
    print(temp)
    print(agenda)

'''
Exclui um elemento da agenda global

'''

def excluir():

    ceifador = input("Quem vai rodar ")
    del agenda[ceifador]

'''

Printo um elemento da agenda com base no
nome

'''

def buscar():
    google = input("Mostre os dados de: ")
    print(agenda[google])
    

print("Agenda de LP")
a = action()

while True:

    if (a =="i" ): 
        incluir()

    elif(a=="d"):
        excluir()

    elif(a=="b"): 
        buscar()

    elif(a=="s"):
       print("Obrigado por usar a agenda")
       break

    else:
        print("Digita direito seu jumento")

    a = action()
   
