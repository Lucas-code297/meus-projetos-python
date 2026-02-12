valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar a prestação da casa mensal? '))
# 30% do salário do comprador
porcentagem = (30 * salario) / 100
# prestação mensal
prestação = valorcasa / (anos * 12)
if prestação > porcentagem:
    print(f'Empréstimo negado! A prestação mensal ultrapassou 30% do seu salário.')
else:
    print(f'Empréstimo aprovado! Você deve pagar R${prestação:.2f} mensalmente por {anos} anos.')