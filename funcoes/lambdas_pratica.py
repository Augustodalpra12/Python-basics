from functools import reduce

# da pra colar um dicionario dentro de uma lista

pilotos = [
    {'nome': 'Vettel', 'titulos': 4},
    {'nome': 'Hamilton', 'titulos': 7},
    {'nome': 'Senna', 'titulos': 3},
    {'nome': 'Rosberg', 'titulos': 1},
    {'nome': 'Raikkonen', 'titulos': 1}
]

#filter serve para voce filtrar sua estrutura baseada em uma função especifica

# exemplo de filter, como é uma função simples de uma linha, ja passei ela como parametro no filter
pilotos_multi_campeos = filter(lambda piloto: piloto['titulos'] > 1, pilotos)

# tranformar em list, se não ele printa o endereço do objeto
print(list(pilotos_multi_campeos))


# posso usar o lambda para acessar so os nomes dos pilotos
nome_piloto = lambda piloto: piloto['nome']

print(list(map(nome_piloto, pilotos)))

#posso usar o reduce para somar os titulos dos pilotos
somar = lambda a, b: a + b

titulos_pilotos = lambda piloto: piloto['titulos']

total = reduce(somar, map(titulos_pilotos, pilotos), 0)

print(total)
# para calcular a media
print(total / len(pilotos))


