a = int(input('Digite um valor qualquer: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite outro valor: '))
if a > b and a > c:
    print(f'O maior valor digitado foi {a}.')
if b > c and b > a:
    print(f'O maior valor digitado foi {b}.')
if c > b and c > a:
    print(f'O maior valor digitado foi {c}.')
if a < b and a < c:
    print(f'O menor valor digitado foi {a}.')
if b < c and b < a:
    print(f'O menor valor digitado foi {b}.')
if c < b and c < a:
    print(f'O menor valor digitado foi {c}.')
else:
    if a == b == c:
        print(f'Não há valor maior, todos são iguais.')