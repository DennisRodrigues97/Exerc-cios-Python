# Faça um programa que leia um ano qualquer e diga se ele é bissexto.
from datetime import date

import dateutil.utils

ano = int(input("Diga qualquer ano para saber se ele é bissexto: "))
print(ano % 100)

if ano % 4 == 0 and ano % 100 != 0:
    print("{} é um ano bissexto!".format(ano))
else:
    print("{} não é um ano bissexto!".format(ano))

# como importar o ano
ano_hoje = date.today().year
print(ano_hoje)
