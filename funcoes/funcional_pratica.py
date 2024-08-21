# você pode "armazenar funções" em variaveis no python

def calor(a):
    if a >= 30:
        return True
    return False

temperatura = calor
print(temperatura(30))

# tambem é possivel passar funções como argumentos
def redes_neurais(fn_ativacao, saida_processamento):
    return fn_ativacao(saida_processamento)

# voce pode fazer funções dentro de funções, pode ser util para dividir as etapas de processamento do algoritmo implementado
def funcao_fora(fn_ativacao):
    def funcao_dentro(saida_processamento):
        return fn_ativacao(saida_processamento)
    return funcao_dentro

