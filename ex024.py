# programa que lê o nome da cidade e diz se ela começa com "SANTO" ou não
cidade = str(input('Qual é o nome da sua cidade?')). strip()
cidade = cidade.upper()
cidade = cidade.split()
print(f'Começa com o nome "SANTO"? {'SANTO' in cidade[0]}')