num = int(input("Number: "))
n = 0
for y in range(2, num+1):
    if num % y == 0:
        n = n + 1
if n == 1:
    print("Número primo")
else:
    print("Número composto")

# é possível melhorar a performance do programa adicionando a verificação da raiz perfeita,
# para que seja analisado apenas poucas números primos. https://www.youtube.com/watch?v=rdWotutaSSE