'''
cidade = str(input("Nome da cidade: ").strip())
cidade = cidade.lower()
a = cidade.split()

if a[0] == "santo":
    print("Sua cidade comceça com SANTO!")
else:
    print("Sua cidade não começa com SANTO!")
'''

#Solução do Guanabara:

cidade = str(input("Sua cidade: "))
print(cidade[:5].lower() == "santo")