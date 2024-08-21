# você pode passar varios parametros, de forma a não especificiar quantos necessarimente precisam ser passados, isso pode ser feito com o *

def pessoas(*nomes):
    return nomes

def status_jogador(**kwargs):
    print(kwargs['nome'])
    print(kwargs['posicao'])
    print(kwargs['idade'])
    print(kwargs['numero'])