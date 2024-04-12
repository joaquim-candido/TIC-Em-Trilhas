# EXEMPLO BOM

# Calcula a média de notas dos alunos
def calcular_media(notas):
    # Soma todas as notas
    soma = sum(notas)
    # Divide a soma pelo número de notas para obter a média
    media = soma / len(notas)
    return media


# Exemplo de uso da função calcular_media
notas_aluno = [7, 8, 9, 6, 8]
media_aluno = calcular_media(notas_aluno)
print("A média do aluno é:", media_aluno)

# ------------------------------
# EXEMPLO RUIM


# Função para calcular média
def calc_media(lista):
    # Aqui somamos todas as notas
    soma = sum(lista)
    # Agora dividimos a soma pelo número total de notas
    media = soma / len(lista)
    return media


# Chamada da função calc_media com uma lista de notas
notas = [7, 8, 9, 6, 8]
resultado = calc_media(notas)  # Chamando a função e armazenando o resultado numa variável
print("Resultado:", resultado)  # Imprimindo o resultado na tela
