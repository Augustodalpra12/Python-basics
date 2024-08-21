# dicionarios tambem são definidos com chaves {}, mas tem varios tipos de dados dentro dele
jogador = {
    'nome': 'Yago dos Santos',
    'altura': 1.78,
    'ativo': True,
    'posicao': 'PG'
}

print(jogador['nome']) # você pode acessar pelo nome da chave

# é possivel usar o len, ele vai retornar quantas chaves / valor tem no dicionario
print(len(jogador))