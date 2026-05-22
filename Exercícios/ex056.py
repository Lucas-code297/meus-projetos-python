count = m = mv = 0
nomevelho = ''
for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')). upper()
    if sexo == "F" and idade < 20:
        count += 1
    if idade > 0:
        m += idade / 4
    if sexo == 'M':
        if idade > mv:
            mv = idade
            nomevelho = nome
            if mv < idade:
                mv = idade
                nomevelho = nome
print(f'A média de idade do grupo é {m:.1f} anos.')
if count == 1:
    print(f'Ao todo, apenas {count} mulher possui menos de 20.')
else:
    print(f'Ao todo, {count} mulheres possuem menos de 20.')
print(f'O homem mais velho possui {mv} anos     e se chama {nomevelho. title()}.')