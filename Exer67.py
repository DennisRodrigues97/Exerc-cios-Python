from emoji import emojize
while True:
    print('-'*30)
    taboada = int(input("Quer ver a tabuada de qual valor? "))
    print('-'*30)
    if taboada >= 0:
        for i in range(1, 11):
            print(f'{taboada} x {i:2} = {taboada*i}')
        if taboada == 0:
            print('Qualquer número multiplicado por zero é igual a zero.', emojize('😀\n'))
    else:
        print("Programa TABUADA encerrado. Volte sempre!")
        break
