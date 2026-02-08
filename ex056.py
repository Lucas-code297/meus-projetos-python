# programa que lê nome, idade e sexo de 4 pessoas e no final mostra:
# a média de idade do grupo; qual é o nome do homem mais velho; quantas mulheres tem menos de 20 anos
mais = 0
m = 0
count = 0
nomevelho = ''
for pergunta in range(1, 4+1):
    print(f'{'=' * 10} {pergunta}° PESSOA {'=' * 10}')
    nome = str(input('Qual é o seu nome? ')). title()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual é o seu sexo [M/F]? '))
    m = m + idade
    if sexo == 'F' or sexo == 'f':
        if idade < 20:
            count = count + 1
    if sexo == 'M' or sexo == 'm':
        if pergunta == 1:
            mais = idade
            nomevelho = nome
        elif idade > mais:
            mais = idade
            nomevelho = nome
print(f'A média de idade do grupo é {m / 4:.1f} anos.')
print(f'Ao todo, {count} mulheres têm menos de 20 anos.')
print(f'O homem mais velho tem {mais} anos e se chama {nomevelho}.')