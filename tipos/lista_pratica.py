nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # declaração de lista em python, nesse caso de inteiros
print(type(nums)) # vai retornar list

nums.append(3) # append é o metodo para adicionar itens na lista, a lista permite a repetição de itens
nums.append("texto") # pode adicionar outros tipos 
print(nums)
print(type(nums)) # continua sendo lista

print(len(nums)) # a função len retorna o tamanho da lista, muito util para diversas implementações

print(nums[3]) # é possivel selecionar um elemento a partir do seu indice na lista
nums[3] = "alterado" # bem como altera-lo pelo seu indice
print(nums)

nums.insert(0, "insert") # é possivel realizar a inserção a partir do metodo insert
print(nums)

# para acessar o ultimo elemento da lista, basta pegar o indice do tamanho da lista e subtrair 1
print(nums[12])
# entretanto no python pode utilizar o -1, se parar pra pensar é como se fosse uma "lista circular" onde o que vem antes do indice 0 é o indice -1. Isso se aplica ao -2 , -3 ...
print(nums[-1])

# muitas funcionalidades da lista funcionam em tupla e vice-versa