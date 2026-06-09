# análise de dado em grupo
print('-' * 23)
print('CADASTRE UMA PESSOA')
# acumulador
cont = homens = mulheres = 0
while True:
    print('-' * 23)
    idade = int(input('Idade: '))
    sexo = str(input('sexo [F/M]: ')).strip().upper()
    print('-' * 23)
    opçao = str(input('Quer continuar [S/N]? ')).strip().upper()
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    if opçao == 'N':
        break
print(f'Ao todo, {cont} pessoas possuem mais de 18 anos.')
print(f'Total de homens cadastrados: {homens}')
print(f'Temos um total de {mulheres} mulheres com menos de 20 anos.')
