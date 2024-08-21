class Formula1:
    def __init__(self, motor, arrasto, asa_dianteira, asa_traseira):
        self.__motor = motor
        self.__arrasto = arrasto
        self.__asa_dianteira = asa_dianteira
        self.__asa_traseira = asa_traseira
        self.__combustivel = 0
        self.__pneu = ''

    def abastecer(self, litros):
        self.__combustivel += litros

    def trocar_pneu(self, novo_pneu):
        self.__pneu = novo_pneu

class Mclaren(Formula1):
    def __init__(self, motor, arrasto, asa_dianteira, asa_traseira, pintura):
        super().__init__(motor, arrasto, asa_dianteira, asa_traseira) # metodo super para sobrescrever o metodo da classe pai
        self.__pintura = pintura

    def selecionar_pintura(self, nova_pintura):
        self.__pintura = nova_pintura

lando_norris = Mclaren('Mercedes', 0.5, 0.5, 0.5, 'laranja')
print(lando_norris.__dict__) # dict para transformar em um dicionario e printar o conteudo do objeto e não o endereço dele
