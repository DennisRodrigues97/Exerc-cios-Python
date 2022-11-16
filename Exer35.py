# Pergunte ao usuário o tamanho de três retas e diga-lhe se estas medidas
# podem formar um triângulo.

r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
maior = float

if r1 > r2 and r1 > r3:
    maior = r1
elif r2 > r3:
    maior = r2
else:
    maior = r3

triangulo = r1 + r2 + r3 - maior

if triangulo > maior:
    print("Estas retas podem formar um triângulo!")
else:
    print("Estas retas não podem formar um triângulo!")


