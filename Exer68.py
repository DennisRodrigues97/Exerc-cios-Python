from random import randint

contador = 0

while True:
    computador = randint(0, 10)
    usuario = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    parOuImpar = (computador + usuario) % 2
    if escolha == 'I' and parOuImpar == 1 or escolha == 'P' and parOuImpar == 0:
        print(f'O computador jogou {computador} e você jogou {usuario}. Total de {computador+usuario}',
              'DEU PAR.' if parOuImpar == 0 else "DEU ÍMPAR.")
        print('Você venceu!\nVamos jogar novamente...')
        contador += 1
    else:
        print(f'O computador jogou {computador} e você jogou {usuario}. Total de {computador + usuario}',
              'DEU PAR.' if parOuImpar == 0 else "DEU ÍMPAR.")
        print('Você perdeu!')
        break
print(f'GAME OVER! Você venceu {contador}', 'vezes' if contador > 1 else 'vez.')

