print('=' * 25)
print('BRANCO CEV')
print('=' * 25)
# cédulas
cedula_c = 50
cedula_v = 20
cedula_d = 10
cedula_u = 1
#acumulador
t = m = valor = subtrair = soma = 0
while True:
    sacar = int(input('Quanto você quer sacar? '))
    total_1 = sacar // 50
    while t < total_1:
        t = sacar // cedula_c
        valor = t * cedula_c
        m = valor + 50
        if m > sacar:
            subtrair = valor - sacar
            soma = subtrair + valor
            if soma == sacar:
                print(f'Total de {t} cédulas de R$50')
                print(f'Total de {t}')
    if sacar > 0:
        break
print('FIM.')