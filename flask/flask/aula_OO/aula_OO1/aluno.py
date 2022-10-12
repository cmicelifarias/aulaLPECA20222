class Aluno:

    def __init__(self, nome,dre):
        self.nome = nome
        self.dre = dre

    def diga_oi(self):
        return "Oi meu nome eh "+self.nome

a = Aluno("Buda","123")
#Aluno,__init__(a,nome,dre)
print(a.diga_oi())
