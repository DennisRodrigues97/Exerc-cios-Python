num = int(input("Número inteiro: "))
par = num % 2

if par == 1:
    print("O número {} é par!".format(num))
else:
    print("O número {} é ímpar!".format(num))
