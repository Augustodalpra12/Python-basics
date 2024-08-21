# os logicos tambem bem parecidos com os de outras linguagens
x = True
y = False

print(x and y)
print(x or y)
print(x != y) # não tem XOR, então se usa o !=
print(not x)

# podem ser combinados
print(x and y or y != x and not x)

#podem ser usados com outras variaveis
par = 12
impar= 3

print(y or par > impar)
print(x and par > impar)