# sequencia de fibornacci
print('_' * 25)
print('SEQUÊNCIA DE FIBONACCI')
print('_' * 25)
# perguntando ao usuario quantos termos ele quer que mostrar
termos = int(input('Quantos termos você quer mostrar? '))
# variaveis para a sequencia
a = 1
b = c = 0
# acumulador para o laço saber quando parar
cont = 0
while cont != termos:
    print(f'{c}', end=' --> ')
    cont += 1
    b = a # b passa a valer 1
    a = c # a passa a valer 0
    c = a + b # vai somando os números até a quantidade de termos desejado pelo usuario
print('Finalizado.')
