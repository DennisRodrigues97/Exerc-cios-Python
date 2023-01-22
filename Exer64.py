cont = soma = 0
num = int(input("Números: "))
while num != 999:
    soma += num
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')
