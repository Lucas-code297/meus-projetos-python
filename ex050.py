# programa que lê 6 números inteiros e soma somente os pares, os ímpares ele desconsidera
s = 0
count = 0
for c in range (1, 6+1):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s = s + n
        count = count + 1
print(f'Você digitou {count} números pares, portanto, a soma deles é {s}.')