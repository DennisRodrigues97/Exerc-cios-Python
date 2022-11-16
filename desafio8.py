# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite valor em metros: "))
centimetros = metros * 100
milimetros = centimetros * 10
print("{} metros é igual à {} centimetros e igual a {} milímetros.".format(metros, centimetros, milimetros))


