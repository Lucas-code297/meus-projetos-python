a = float(input('Digite sua primeira nota: '))
b = float(input('Digite sua segunda nota: '))
média = (a + b) / 2
if média < 5.0:
    print(f'REPROVADO! Sua média atingida foi {média:.1f}.')
elif média <= 6.9:
    print(f'RECUPERAÇÃO! Sua média atingida foi {média:.1f}.')
else:
    if média >= 7.0:
        print(f'APROVADO! Sua média atingida foi {média:.1f}.')