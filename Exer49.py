from tkinter import *

def tabuada(numero1):
    num1 = int(numero1)
    a = str
    for c in range(1, 11):
        a = "{} x {:2} = {}".format(num1, c, num1 * c)
    numero_escolhido["text"] = a

janela = Tk()
janela.geometry("300x300")
janela.title("Tabuada")
texto = Label(janela, text="Digite qual tabuada você quer: ")
texto.grid(column=0, row=0)
numero = Entry(janela, width=10)
numero.grid(column=0, row=1)
botao = Button(janela, text="Clique aqui.", command=lambda: tabuada(numero.get()))
botao.grid(column=0, row=2)
numero_escolhido = Label(janela, text="")
numero_escolhido.grid(column=0, row=3)

janela.mainloop()