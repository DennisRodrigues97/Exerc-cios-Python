nome = str(input("Nome completo: ")).split()
maiuscula = nome.upper()
minuscula = nome.lower()
nome = nome.split()
numLetras = "".join(nome)
numLetras0 = len(numLetras)
numLetrasPrimeiro = len(nome[0])

print("Nome com letras maiúsculas:", maiuscula)
print("Nome com letras minúsculas:", minuscula)
print("Número de letras do nome:", numLetras0)
print("Seu primeiro nome é {} e tem {} letras.".format(nome[0], numLetrasPrimeiro))

# Solução proposta pelo Guanabara:

# Conta quantas letras tem o nome completo:
# print("Seu nome tem {} letras".format((len(nome) - nome.count(" "))))
# Conta quantas letras tem o primeiro nome:
# print("Seu primeiro nome tem {} letras.".format(nome.find(" ")))
