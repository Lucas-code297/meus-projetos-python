# programa para aprovar um empréstimo bancário para a compra de uma casa
# deve perguntar: o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# o programa deve dizer se ele irá poder comprar a casa, tendo em vista que o valor não pode exceder 30% de seu salário
# caso isso ocorra, ele não poderá financiar a casa
vc = float(input('Qual é o valor da casa? '))
sc = float(input('Qual é o salário do comprador? '))
anos = int(input('Em quantos pretende pagar a casa? '))
# valor da prestação:
valor = vc / (anos * 12)
# porcetagem do salário:
salário = (sc * 30 / 100)
if valor > salário:
    print('O valor excedeu 30% do seu salário, portanto, não poderá comprar a casa!')
else:
    print(f'Certo. A prestação mensal fica por R${valor:.2f}! \nBoa sorte em sua compra!')