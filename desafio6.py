# Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input("Digite um número fi: "))
dobro = n * 2
triplo = n * 3
raiz = pow(n, 1/2)
print("Dobro: {}\nTriplo {}\nRaiz quadrada: {:.2f}".format(dobro, triplo, raiz))
