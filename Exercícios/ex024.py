cidade = str(input('Digite o nome da cidade que voce nasceu: ')). strip().title()
cidade = cidade.split()
print(f'Essa cidade começa com a palavra "Santo"? {'Santo' in cidade[0]}')