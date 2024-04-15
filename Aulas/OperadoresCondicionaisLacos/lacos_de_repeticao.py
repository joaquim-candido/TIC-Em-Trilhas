# lista_de_compras = ["Ovos", "Farinha", "Leite", "Confete", "Chantili", "Arroz"]
#
# for item in lista_de_compras:
#     print("Comprei o item:", item)

numero = 0

while True:
    print("Número", numero)
    numero = numero + 1

    if numero % 2 == 0: # Forma de verificar se número é par
        print(numero, "é par")
        continue

    print(numero, "é impar")
