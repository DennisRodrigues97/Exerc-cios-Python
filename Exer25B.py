nome = input("Seu nome: ")
nome = nome.split()

i = 0
while i < len(nome):
   
    if nome[i] == "silva":
        print("Seu nome tem Silva!")
    elif nome[i] != "silva " and i == len(nome)-1:
        print("Você não tem Silva no nome!")


    i = i + 1








