nomes = ('Zach Lavine', 'Josh Gidey', 'Lonzo Ball') # tuplas são imutáveis e são representadas por parenteses

# voce pode verificar se um nome existe na tupla, usando o "in", isso funciona em listas tambem
print('Zach Lavine' in nomes)
print('Lebron James' in nomes)

# muitas funcionalidades da lista funcionam em tupla e vice-versa

# você pode usar "numero" : "numero", para acessar um determinado intervalo na tupla
print(nomes[0:2])

# isso é uma string
x = ('Demar Derozan')
print(type(x))

# isso é uma tupla
y = ('Demar Derozan',)
print(type(y))

# outra forma de brincar com os "indices"
print(nomes[2:]) # pegar todos os elementos a partir do indice 2
print(nomes[:2]) # pegar todos os elementos antes do indice 2