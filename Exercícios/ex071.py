print('=' * 25)
print('BRANCO CEV')
print('=' * 25)
# cédulas
cedula_c = 50
cedula_v = 20
cedula_d = 10
cedula_u = 1
#acumuladores
t = m = valor = subtrair = somar = dividir = resto = resto_10 = 0
somar_10 = multiplicar_10 = subtrair_1 = cont = final = 0
while True:
    sacar = int(input('Quanto você quer sacar? '))
    total_1 = sacar // 50
    m = total_1 * cedula_c # é o valor que eu tenho até então (somando as notas de 50 necessárias)
    somar = m + cedula_c # se o valor que eu tenho somado mais 50, passar do sacar, passa para as cedulas de 20
    if somar > sacar:
        subtrair = sacar - m # subtração para saber o valor da cédula necessário para chegar ao valor de sacar
        if subtrair == 20:
            dividir = subtrair // 20
            print(f'Total de {total_1} de cédula R$50.')
            print(f'Total de {dividir} de R$20.')
        else:
            if subtrair < 20:
                resto_10 = subtrair // cedula_d
                multiplicar_10 = resto_10 * 10
                somar_10 = multiplicar_10 + m
                print(f'Total de {total_1} cédulas de R$50.')
                print(f'Total de {resto_10} cédulas de R$10.')
                if somar_10 < sacar:
                    subtrair_1 = sacar - somar_10
                    while cont < subtrair_1:
                        cont += 1
                        final = cont
                        print(f'Total de {total_1} cédulas de R$50.')
                        print(f'Total de {resto_10} cédulas de 10R$.')
                        print(f'Total de {final} cédulas de R$1.')
    else:
        print(f'Total de {total_1} de R$50')
    if sacar > 0:
        break
print('FIM.')