# programa que calcula a média de um aluno e diz:
# média abaixo de 5.0: reprovado
# média entre 5.0 e 6.9: recuperação
# média entre 7.0 ou superior: aprovado
p = float(input('Digite a sua primeira nota: '))
s = float(input('Digite a sua segunda nota: '))
média = (p + s) / 2
if média < 5.0:
    print('REPROVADO! ESTUDE MAIS!')
elif média <= 6.9:
    print('RECUPERAÇÃO! Boa sorte.')
else:
    print('APROVADO! Parabéns!')
print(f'Sua média foi: {média:.1f}')
