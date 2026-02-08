# tabuada melhorada
while True:
    n = int(input('Digite um número inteiro: '))
    s = n
    if n < 0:
        break
    while n != 10:
        s += 1
        print(f'{s} x {}')
        if s == 10:
            break