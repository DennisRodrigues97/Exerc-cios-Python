#Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em ºC: "))
fahrenheit = celsius * 1.8 + 32
print("{} ºC é igual a {} ºF.".format(celsius, fahrenheit))
