produto = float(input('Qual é o preço do produto?R$ '))
desconto = produto - ((5 * produto) / 100)
print(f'O produto que custa {produto} passará a custar R${desconto:.2f} com o desconto de 5%.')