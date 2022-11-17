# Escreva um programa para aprovar o emprestimo bancário de uma casa.
# O programa vai perguntar o SALÁRIO do comprador, o VALOR DA CASA, e em QUANTOS ANOS ELE VAI PAGAR
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado
from math import ceil

salario = float(input("Salário: "))
valorImovel = float(input("Valor da casa: "))
anos = float(input("Em quantos anos: "))
meses = ceil(anos * 12)
condicao = 30 / 100 * salario
prestacao = valorImovel / meses

if prestacao > condicao:
    print("Infelizmente a prestação foi {:.2f} e passou dos 30% e seu emprestimo foi {}NEGADO{}.".format(prestacao, "\033[31m", "\033[m"))
else:
    print("Seu emprestimo foi {}APROVADO{}, as parcelas são de R${:.2f}.".format("\033[32m", "\033[m", prestacao))






