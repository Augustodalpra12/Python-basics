# Alguns exemplos de alguns "fors" com uso de break, continue e pass

for i in range(1, 13):
    if i / 4 == 3:
        break
    print("Voce não chegou no 12 ainda")

for i in range(1, 13):
    if i / 4 == 3:
        continue
    print("Voce não chegou no 12 ainda")

for i in range(1, 13):
    if i / 4 == 3:
        pass # pass eu não sabia o que era, mas passa o loop, ou pode ser usado em funções quando não tem a implementação dela ainda
    print("Voce não chegou no 12 ainda")