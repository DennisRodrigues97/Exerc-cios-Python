cont = countNumbers = 0
while True:
    numbers = int(input("Digite um valor (999 pra parar): "))
    if numbers == 999:
        break
    countNumbers += numbers
    cont += 1
print(f'A soma dos {cont} valores foi {countNumbers}!')
