# programa que calcula a soma de todos os número ímpares e múltiplos de 3 que se encontram no intervalo
# de 1 até 500
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {s}.')
