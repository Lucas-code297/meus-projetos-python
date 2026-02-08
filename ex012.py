# programa que lê o preço de um produto e diz qual será o seu novo preço
# com 5% de desconto
produto = float(input('Qual é o preço do produto? '))
c = (produto * 5) / 100
d = produto - c
print(f'Com o desconto, seu novo preço é R${d:.2f}!')