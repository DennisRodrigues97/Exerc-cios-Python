#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = input("1º aluno: ")
a2 = input("2º aluno: ")
a3 = input("3º aluno: ")
a4 = input("4º aluno: ")
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print(alunos)







#print("A ordem é: {}".format(random.choice(alunos)))
