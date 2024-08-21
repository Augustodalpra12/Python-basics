# tem sintaxe diferente do C, não precisa de chaves e paresteses

for i in range(12): # quer dizer que dado I, ele vai ter um "range", um alcance de i ate 11, (o 12 n entra), nesse caso i começa em 0 por padrão
    print(i)

# se eu quiser escolher o começo de i (ou da variavel que voce escolher), basta adicionar ao range
for i in range(4, 12):
    print(i)

# Posso escolher ate de quanto vai ser a incrementação, basta adicionar ao range
for i in range(4, 13, 4):
    print(i)

# pode ser de forma "invertida"
for i in range(12, 4, -1):
    print(i)

# usando listas (comumente o for utiliza "for singular in plural:")
impares = [1, 3, 5, 7, 9, 11]

for impar in impares:
    print(impar, end = ' ') # o end é um parametro do print, dessa forma ele não vai printar um elemento em cada linha e sim na mesma pulando com espaços

# Pode se utilzar em strings tambem

texto = 'Tutututu Max Verstappen'
print('\n')
for letra in texto:
    print(letra, end = '')

# pode ser utilzado com conjuntos, listas etc

for n in {4, 19, 3, 81}:
    print(n)

# é possivel iterar mais do que um valor no for, o que é bem util quando se utiliza dicionarios

jogador = {
    'nome': 'Javonte Green',
    'camisa': 24,
    'posição': 'guard/foward'
}

for atrib in jogador:
    print(atrib, jogador[atrib])

for atrib, valor in jogador.items(): # função itens para iterar o dicionario e ja pegar os "itens" desse dicionario
    print(atrib,' ', valor)

# ou para percorrer so os valores, utilize values()
for valor in jogador.values(): 
    print("So os valores: ", valor)

# ou para percorrer so as chaves, keyes()
for atrib in jogador.keys(): 
    print("Chaves: ", atrib)