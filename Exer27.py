nome = str(input("Nome completo: ")).strip().split()
primeiro = nome[0]
ultimo = nome[len(nome)-1]

print("Primeiro nome: {}\nUltimo nome: {}".format(primeiro, ultimo))

