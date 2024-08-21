from functools import reduce

# exemplo de uso do map, mas primeiro vamos ver outras alternativas

# pode ser usado o for e o enumerate, "enumerando" a lista
# for i, pneu in enumerate(pilotos_pneus):
#     pilotos_pneus[i] = pneu + 1

# # usando o for e o len, para pegar o tamanho da lista
# for i in range(len(pilotos_pneus)):
#     pilotos_pneus[i] = pilotos_pneus[i] + 1

# agora usando o map. Você passa a função para o map, que ele vai aplicar a lista selecionada
def volta_na_corrida(voltas_pneu):
    return voltas_pneu + 1

pilotos_pneus = [12, 5, 0, 2, 7]
desgate_pneus = map(volta_na_corrida, pilotos_pneus)

print(desgate_pneus)

#exemplo reduce, o reduce ele aplica uma função em todos os itens da lista e retorna um unico valor

max_verstappen_pontos = [25, 0, 12]

def somar(a, b):
    return a + b

total = reduce(somar, max_verstappen_pontos, 0)
print(total)