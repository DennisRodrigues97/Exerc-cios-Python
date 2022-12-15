import random
from emoji import emojize

emoji = {
    "1": emojize(":right-facing_fist:"),
    "pedra2": emojize(":raised_fist:"),
    "2": emojize(":hand_with_fingers_splayed:"),
    "3": emojize(":victory_hand:"),
    "empate": emojize(":handshake:")
}
usuario = input("1 - Pedra\n2 - Papel\n3 - Tesoura\n")
comput = random.randint(1, 3)
comput = str(comput)
vencedor = ""

print("Você escolheu {}".format(emoji[usuario]))
print("O computador escolheu {}".format(emoji[comput]))

if usuario == comput:
    print("Vocês empataram {}".format(emoji["empate"]))
elif usuario == "1" and comput == "2":
    vencedor = "computador"
elif usuario == "1" and comput == "3":
    vencedor = "você"
elif usuario == "2" and comput == "1":
    vencedor = "você"
elif usuario == "2" and comput == "3":
    vencedor = "computador"
elif usuario == "3" and comput == "1":
    vencedor = "computador"
elif usuario == "3" and comput == "2":
    vencedor = "você"

if comput != usuario:
    if vencedor == "você":
        print("O vencedor foi {}{}{}".format("\033[32m", vencedor, "\033[m"))
    else:
        print("O vencedor foi {}{}{}".format("\033[1;32;40m", vencedor, "\033[m"))



