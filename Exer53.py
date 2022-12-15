frase = str(input("Digite sua frase: "))
print(frase, ",", end=",")
frase = "".join(frase.split()).lower()
if frase == frase[::-1]:
    print("É polindromo!")
else:
    print("Não é polindromo!")
