def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("Escolha uma operação ou 's' para sair:")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a Calculadora Simples!")
            break

        if operacao not in ['1', '2', '3', 4]:
            print("Operação inválida, tente novamente.")
            continue

        primeiro_numero_string = input("Digite o primeiro número:")
        if not primeiro_numero_string.isdigit():
            print(primeiro_numero_string, "não é um número válido! Tente novamente.")
            continue

        segundo_numero_string = input("Digite o segundo número:")
        if not segundo_numero_string.isdigit():
            print(segundo_numero_string, "não é um número válido! Tente novamente.")
            continue

        primeiro_numero = float(primeiro_numero_string)
        segundo_numero = float(segundo_numero_string)

        if operacao == '1':
            resultado = primeiro_numero + segundo_numero
            print("O resultado da operação soma é:", resultado)
        elif operacao == '2':
            resultado = primeiro_numero - segundo_numero
            print("O resultado da operação subtração é:", resultado)
        elif operacao == '3':
            resultado = primeiro_numero * segundo_numero
            print("O resultado da operação multiplicação é:", resultado)
        else:
            if segundo_numero == 0:
                print("Divisões por zero não são permitidas. Tente novamente.")
            else:
                resultado = primeiro_numero / segundo_numero
                print("O resultado da operação divisão é:", resultado)


calculadora()
