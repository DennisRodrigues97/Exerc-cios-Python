frase = str(input("Digite sua frase: "))
frase = "".join(frase.split()).lower()
print("{}, ".format(frase[::-1]), end="")
if frase == frase[::-1]:
    print("é polindromo!")
else:
    print("não é polindromo!")
