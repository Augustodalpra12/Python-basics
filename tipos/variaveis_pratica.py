#diferente de outras linguagens, não é necessario definir o tipo da variável
a = 12
b = 8.1
# a soma delas é bem simples tambem
soma = a + b
print(soma)
# ou ate mesmo
print(a + b)

# strings podem ser definidas com aspas duplas "" ou simples ''
aspas_duplas = "String com aspas duplas"
aspas_simples = 'String com aspas simples'

# para juntar strings e outros tipos, pode ser realizado casting da variavel inteira
print(aspas_duplas + str(a))

# a maneira indicada é usar o "fstring"
print(f'{aspas_simples} {a} e aqui ele simplesmente vai escrever a string, diferente do abre/fecha chaves que ele interpreta o codigo')

# você pode multiplicar strings (sim), pode ser uma variavel tambem
print("vou aparecer 4 vezes " * 4)

# em python não tem constantes, para convesão se utiliza as letras maiúsculas para variaveis "constantes"
EULER = 2.718281828

# em comparação ao scanf do C, o input do python recebe a informação do usuario, para armazenar em uma variavel basta colocar o nome da variável = input ...
variavel_de_entrada = input('digite algo: ')

# é possivel ver o tipo da variavel a partir da função "type"
print(type(variavel_de_entrada))

# a operação de potencia quadrada pode ser feita como se fosse duas multiplicações **, ou pow(num, num) para generalizar
print(2 ** 3) # o que vai retornar 8
print(pow(2,3)) # o que tambem vai retornar 8