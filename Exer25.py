'''
nome = input("Diga seu nome: ")
nome = nome.split()
i = 0

while i < len(nome):
    if nome[i] == "silva":
        print("Seu nome tem Silva.")
        break
    else:
        i = i+1
'''

nome = str(input("Nome completo: ")).strip()
if "silva" in nome.lower():
    print("Seu nome tem Silva.")
else:
    print("Seu nome não tem Silva.")


