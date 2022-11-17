num = input("Digite um numero entre 0 e 9999: ")
while len(num) > 4:
    print("Você digitou mais caracteres do que o esperado, digite novamente:")
    num = input("Digite um número entre 0 e 9999: ")
else:
    i = 0
    decimalPlaces = ["Milhar:", "Centena:", "Dezena:", "Unidade:"]
    while i < len(num):
        print(decimalPlaces[i], num[i])
        i = i+1






