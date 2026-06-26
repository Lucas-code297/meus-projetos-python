from time import sleep
print('=' * 20)
print('BRASILEIRÃO')
print('=' * 20)
sleep(1)
# tabela do brasileirão
tupla_timetodos = ('Palmeiras\n''Flamengo\n' 'Fluminense\n''Atlético-PR\n''Bragantino\n''Bahia\n''Coritiba\n''São paulo\n'
                   'Atlético-MG\n''Corinthians\n''Cruzeiro\n''Botafogo\n''EC Vitória\n''Internacional\n''Santos\n''Grêmio\n'
                   'Vasco da Gama\n''Remo\n''Mirassol\n''Chapecoense\n')
# ordem alfabética
tupla_ordem = ('Atlético-PR\n''Atlético-MG\n''Bragantino\n''Bahia\n''Botafogo\n''Coritiba\n''Corinthians\n''Cruzeiro\n'
               'Chapecoense\n''EC Vitória\n''Grêmio\n''Flamengo\n''Fluminense\n''Internacional\n''Mirassol\n''Palmeiras\n''Remo\n''Santos\n'
               'Vasco da Gama\n''')
tupla_topcinco = ('Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-PR', 'Bragantino\n')
tupla_topquatro = ('Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-PR\n')
while True:
    print('Escolha uma das opções abaixo:')
    print('[1] Mostrar os 5 primeiros colocados da tabela;\n'
          '[2] Mostrar os últimos 4 colocados da tabela;\n'
          '[3] Uma lista com os times em ordem alfabética;\n'
          '[4] Em que posição da tabela está o time da Chapecoense;\n'
          '[0] Finalizar programa.')
    sleep(2)
    op = int(input('Digite o número de acordo com a opção desejada: '))
    sleep(2)
    if op != 0:
        if op == 1:
            print(f'Os 5 primeiros colocados da tabela são: {tupla_topcinco}')
        elif op == 2:
            print(f'Os 4 primeiros colocados da tabela são: {tupla_topquatro}')
        elif op == 3:
            print(f'Times em ordem alfabética: {tupla_ordem}')
        elif op == 4:
            print('O time da Chapecoense está em 20ª colocado.')
        print('=' * 35)
        sleep(2)
    else:
        break
print('Programa finalizado.')