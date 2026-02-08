# programa que compara números
# dizendo qual é o menor, qual é maior ou se os números tem o mesmo valor
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a > b:
    print('O primeiro valor é maior.')
elif a < b:
    print('O segundo valor é maior.')
else:
    print('Ambos têm o mesmo valor.')