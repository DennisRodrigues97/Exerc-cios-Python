# Escreva um programa que leia um número inteiro qualquer, e peça
# para o usuário escolher qual será a basede conversão :
# 1 para binário - 2 para octal - 3 para hexadecimal
from time import sleep
from emoji import emojize

print("\033[34m*@\033[m"*20)
print("Conversor de base decimal para binário, octal ou hexadecimal.")
print("\033[34m*@\033[m"*20)

decimal = int(input("Qual número quer converter?\n: "))
baseEscolhida = int(input("Digite:\n1 para binário\n2 para octal\n3 para hexadeciaml\n: "))
binario = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
processando = "Processando... {}".format(emojize("⌛", language="pt"))

if baseEscolhida == 1:
    print(processando)
    sleep(2)
    print("Binário: {}{}{}".format("\033[1;32;40m", binario[2::], "\033[m"))
elif baseEscolhida == 2:
    print(processando)
    sleep(2)
    print("Octal: {}{}{}".format("\033[1;32;40m", octal[2::], "\033[m"))
elif baseEscolhida == 3:
    print(processando)
    sleep(2)
    print("Hexadecimal: {}{}{}".format("\033[1;32;40m", hexadecimal[2::], "\033[m"))
else:
    print("Escolha inválida.")



