produto = float(input('Quanto custa o produto?'))
desconto = produto - ((produto * 5) / 100)
print(f'Certo! O preço do produto deixa de ser R${produto:.2f} e passa a ser R${desconto:.2f}')