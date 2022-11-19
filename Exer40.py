# Crie um programa que leia duas notas do aluno e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
cor = {
    "fecha": "\033[m",
    "vermelho": "\033[1;31m",
    "verde": "\033[1;32m",
    "azul": "\033[34m",
    "amarelo": "\033[33m"
}
if media < 5:
    print("Sua média foi {}{}{}, portanto você foi {}reprovado{}.".format(cor["azul"], media, cor["fecha"], cor["vermelho"], cor["fecha"]))
elif 5 <= media <= 6.9:
    print("{}Recuperação{}, sua nota foi {}{}{}".format(cor["amarelo"], cor["fecha"], cor["azul"], media, cor["fecha"]))
elif media >= 7:
    print("{}Aproado{}! Sua nota foi {}{}{}".format(cor["verde"], cor["fecha"], cor["azul"], media, cor["fecha"]))
