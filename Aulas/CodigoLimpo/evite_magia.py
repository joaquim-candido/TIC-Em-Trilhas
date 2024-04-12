# EXEMPLO BOM

PI = 3.14  # Definindo uma constante para o valor de pi


# Função para calcular a área de um círculo
def calcular_area_circulo(raio):
    area = PI * raio ** 2
    return area


# Chamada da função com um raio definido de forma significativa
raio_do_circulo = 5
area_do_circulo = calcular_area_circulo(raio_do_circulo)
print("A área do círculo é:", area_do_circulo)

# ------------------------------
# EXEMPLO RUIM


# Função para calcular a área de um círculo
def calcular_area_circulo():
    area = 3.14 * 5 ** 2  # Usando números sem explicação
    return area


# Chamada da função sem especificar o raio
area_do_circulo = calcular_area_circulo()
print("A área do círculo é:", area_do_circulo)
