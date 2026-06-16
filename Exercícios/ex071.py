print('=' * 30)
print(f'{'BANCO CEV':^30}')
print('=' * 30)

sacar = int(input('Quanto você quer sacar? R$ '))

total_cedulas = 0
cedula_atual = 50

while True:
    # Verifica se o valor atual do saque consegue ser pago com a cédula atual
    if sacar >= cedula_atual:
        sacar -= cedula_atual
        total_cedulas += 1
    else:
        # Se contamos alguma cédula do valor atual, mostramos na tela
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula_atual}')

        # Mudamos para a próxima cédula disponível
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1

        # Zeramos o contador para a nova cédula
        total_cedulas = 0

        # Se o valor do saque chegou a 0, encerramos o programa
        if sacar == 0:
            break

print('=' * 25)
print('FIM DO PROGRAMA. Volte sempre!')