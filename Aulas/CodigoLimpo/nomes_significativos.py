# EXEMPLO BOM

# Variáveis com nomes significativos
idade = 25
nome = "João"
saldo_bancario = 1000.50


# Função com nome significativo:
def calcular_idade_em_dias(idade_atual):
    return idade_atual * 365


# Chamada da função com variável significativa:
idade_em_dias = calcular_idade_em_dias(idade)
print("A idade em dias é:", idade_em_dias)

# ------------------------------------------
# EXEMPLO RUIM

# Variáveis sem nome significativo
x = 25
y = "João"
z = 1000.50


# Função com nome não significativo:
def funcao(x):
    return x * 365


# Chamada da função com variável não significativa:
resultado = funcao(x)
print("O resultado é:", resultado)