# um pouco mais sobre classes

class Piloto_mclaren:
    patrocinios = 12 # atributo de classe, e não da instancia

    def add_patrocinio_pessoal(self):
        return 'Adicinou um patrocinio pessoal'
    
    # agora um metodo de classe, e não da instancia 'classmethod'
    @classmethod
    def add_patrocinio(cls):
        cls.patrocinios += 1
        return cls.patrocinios
    
    # agora um metodo estatico, que não precisa acessar nada da classe
    def desculpa_piloto(desculpa):
        return 'Hoje a culpa foi do {}'.format(desculpa)


# chamando simplesmente a classe
Piloto_mclaren.add_patrocinio()

print(Piloto_mclaren.patrocinios)

gabriel_bortoleto = Piloto_mclaren() # instancia da classe

print(gabriel_bortoleto.add_patrocinio_pessoal())

# chamando o estatico
print(Piloto_mclaren.desculpa_piloto('motor'))

# tomar o cuidado onde patrocinios é da classe e não da instancia do piloto.
# então se eu tiver um metodo para aumentar os patrocinios de um piloto, ele vai aumentar so da instancia Piloto e não da classe, Instacia !=Classe