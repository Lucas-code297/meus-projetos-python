# tratando varios valores
n = 0
# acumuladores
cont = 0
t = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    if n != 999:
        cont += 1
        t += n
print(f'Você digitou {cont} números e a soma deles é {t}.5')