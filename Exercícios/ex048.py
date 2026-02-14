count = 0
t = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        t += c
print(f'A soma de todos os {count} valores solicitados é {t}.')
