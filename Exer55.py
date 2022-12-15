maior = 0
menor = 0
pessoas = ["João", "Maria", "Josefina", "Antonio", "Miguel", "Fernanda", "Oliver"]
for i in range(0, 6):
    peso = float(input("peso {}: ".format(pessoas[i])))
    if peso > maior:
        maior = peso
        pessoaMa = pessoas[i]
    elif peso < peso:
        menor = peso
        pessoaMe = pessoas[i]
print(maior, menor)
