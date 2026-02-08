# menu de opções
from time import sleep
opção = 1
a = int(input('Digite o primeiro número(inteiro): '))
b = int(input('Digite o segundo número(inteiro): '))
c = ''
d = ''
while opção != 5:
    print('Digite o número de acordo com a opção desejada:\n'
      '[1] somar;\n'
      '[2] multiplicar;\n'
      '[3] maior;\n'
      '[4] novos números;\n'
      '[5] sair do programa.')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        print(f'A soma entre {a} e {b} é {a+b}.')
    elif opção == 2:
        print(f'O resultado da multiplicação entre {a} e {b} é {a*b}.')
    elif opção == 3:
        if a > b:
            print(f'O maior número entre {a} e {b} é {a}.')
        if a < b:
            print(f'O maior número entre {a} e {b} é {b}.')
        else:
            if a == b:
                print('Não há maior, os dois valores são iguais.')
    if opção == 4:
        c = int(input('Digite o primeiro valor novamente: '))
        d = int(input('Digite o segundo valor novamente: '))
        a = c
        b = d
    else:
        if opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5:
            print('Opção inválida! Tente novamente.')
    print(f'{'-=' * 25}')
    sleep(1)
print('Programa finalizado.')