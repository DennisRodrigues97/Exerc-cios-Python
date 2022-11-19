# Escreva um programa que leia dois números inteiros, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
cores = {
    "fecha": "\033[m",
    "amarelo": "\033[1;34m",
    "azul": "\033[1;33m"
}

if num1 > num2:
    print("O {}primeiro valor{} é o {}maior{}".format(cores["amarelo"], cores["fecha"], cores["azul"], cores["fecha"]))
elif num2 > num1:
    print(" O {}segundo valor{} é o {}maior{}".format(cores["amarelo"], cores["fecha"], cores["azul"], cores["fecha"]))
elif num1 == num2:
    print("{}Não existe{} valor maior, os dois são {}iguais{}.".format(cores["amarelo"], cores["fecha"], cores["azul"], cores["fecha"]))

