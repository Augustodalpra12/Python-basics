# mostrando mais que variaveis vazias e com valor === 0, são Falsas, enquanto o resto é True

variavel = 'falso' # True
variavel = 0 # False
variavel = 1241251235 # True
variavel = '' # False
variavel = ' ' # True
variavel = [] # False
variavel = {} # False

variavel = 'msg'

if variavel:
    print('Mandou msg')
else:
    print('ficou no vacuo... ;(')

