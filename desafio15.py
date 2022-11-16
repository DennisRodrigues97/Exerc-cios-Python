#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input("Diga, quantos KM's percorreu: "))
dia = int(input("Diga, por quantos dias o carro foi alugado: "))
vdia = dia * 60
vkm = km * 0.15
print("O valor da sua conta é: R$ {:.2f}.".format(vdia+vkm))

