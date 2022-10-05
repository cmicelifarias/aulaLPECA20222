class Carro:

    def __init__(self, dono, placa):    
        self.__dono = dono
        self.__placa = placa

    def get_dono(self):
        return self.__dono

    def get_placa(self):
        return self.__placa

a = Carro('Edu', 'aaa-1111')
print(a.get_dono())
