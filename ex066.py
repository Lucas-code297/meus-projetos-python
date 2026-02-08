count = s = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    count += 1
    s += n
print(f'A soma dos {count} valores é {s}.')