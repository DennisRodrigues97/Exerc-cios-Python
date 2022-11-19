# A confederação nacional de natação precisa de um programa que leio o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade
# Até 9 anos = mirim
# Até 14 anos = infantil
# Até 19 anos = junior
# Até 20 anos = senior
# Acima = master.

import datetime

nascimento = int(input("Ano de nascimento: "))
a = datetime.date.today().year
idade = a - nascimento
categoria = str
if idade <= 9:
    categoria = "mirim"
elif idade <= 14:
    categoria = "infantil"
elif idade <= 19:
    categoria = "junior"
else:
    categoria = "master"

print("Categoria {}".format(categoria))
