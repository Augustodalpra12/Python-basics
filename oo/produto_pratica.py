# trabalhando com classes
#classes vazias basta usar o pass
class Vazia:
    pass

# uma classe com atributos, tem sua incializacão como primeiro passo

class Piloto:
    def __init__(self, nome):
        self.nome = nome


p1 = Piloto('Vettel')

print(p1.nome)

# exemplo com mais atributos
# e com metodos
class Escuderia:
    def __init__(self, nome, pais, pilotos, motor):
        self.nome = nome 
        self.pais = pais
        self.pilotos = pilotos
        self.__motor = motor
        self.__privado = 'privado' # dois __ atributo 'private'

    def num_piltos(self):
        return len(self.pilotos)
    
    @property
    def motor(self):
        return self.__motor

    # para setar é melhor utilizar o decorator @.setter
    @motor.setter
    def motor(self, novo_motor):
        self.__motor = novo_motor
    
    # para transformar um metodo em uma variavel, utiliza-se @property
    @property
    def nome_e_pais(self):
        return self.nome + ' (' + self.pais + ')'

e1 = Escuderia('Mercedes', 'Alemanha', ['Russel', 'Hamilton'], 'Mercedes')
e2 = Escuderia('Mclaren' , 'Reino Unido', ['Norris', 'Piastri'], 'Mercedes')

print(e1.pilotos, e1.pais, e1.nome, e1.num_piltos(), e1.nome_e_pais, e1._Escuderia__privado) # acessa o atributo "private" e1._Escuderia__privado de forma "errada"
print(e2.pilotos, e2.pais, e2.nome, e2.num_piltos(), e2.nome_e_pais)

# para acessar o atributo de forma correta, seria melhor criar uma função que retorna o atributo
# def get_nome(self):
#     return self.__nome

# alterando com o setter
e2.motor = 'Renault'
print(e2.motor)
