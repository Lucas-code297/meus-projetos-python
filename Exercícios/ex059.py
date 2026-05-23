from time import sleep
op = 0
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
while op != 5:
    print('[1] Soma;\n'
          '[2] Multiplicar;\n'
          '[3] Maior;\n'
          '[4] Novos números;\n'
          '[5] Sair do programa.')
    op = int(input('Digite a opção desejada: '))
    if op == 1:
        print(f'A soma entre {a} e {b} é {a+b}.')
    elif op == 2:
        print(f'A multiplicação entre {a} e {b} é {a*b}.')
    elif op == 3:
        if a > b:
            print(f'Entre {a} e {b}, o maior valor é {a}.')
        else:
            print(f'Entre {a} e {b}, o maior valor é {b}.')
    elif op == 4:
        c = int(input('Digite o novo valor: '))
        d = int(input('Digite o outro valor: '))
        a = c
        b = d
    sleep(2)
print('Finalizando programa...')
sleep(2)
print('Programa finalizado.')