print('_' * 25)
print('LOJA DO SUPER BARATÃO')
# acumuladores
total = totmil = cont = barato = 0
# pegar o nome do produto mais barato
nome_barato = ''
while True:
    print('_' * 25)
    produto = str(input('Nome do produto comprado: '))
    preço = int(input('Preço: '))
    op = str(input('Quer continuar [S/N]? ')).strip().upper()
    # conta quantas vezes o programa se repete
    cont += 1
    # irá pegar o preço e nome do produto mais barato
    if cont == 1:
        barato = preço
        nome_barato = produto
    else:
        if preço < barato:
            barato = preço
            nome_barato = produto
    # irá fazer a soma de todos os preços
    total += preço
    # se for mais de 1000, vai guardar no acumulador
    if preço >= 1000:
        totmil += 1
    # finaliza o programa quando o usuario não quiser mais continuar
    if op == 'N':
        break
print('_' * 15, 'FIM DO PROGRAMA', '_' * 15)
print(f'O total da compra foi R${total:.2f}.')
print(f'Ao todo, {totmil} produtos custam mais de R$1000.00.')
print(f'O produto mais barato foi {nome_barato. strip()}, custando R${barato:.2f}.')
print('Fim.')