#!python3

a = 'valor' # True
a = 0 # False
a = -0.0001 # True
a = '' # False
a = ' ' # True
a = [] # False
a = {} # False

print(not not 'valor')

if a:
    print('Existe!!!')
else:
    print('nao existe ou zero ou vazio...')