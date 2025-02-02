# Estatística Básica: Média, Mediana e Moda

# Importamos a biblioteca 'statistics', que tem funções úteis para cálculos estatísticos
import statistics

# Um conjunto de dados simples (uma lista de números)
dados = [10, 20, 20, 30, 40, 40, 40, 50]

# 1. Cálculo da Média
# A média é a soma de todos os números dividida pelo total de números
media = statistics.mean(dados)
print(f"Média: {media}")  # Saída: 31.25

# 2. Cálculo da Mediana
# A mediana é o número central de um conjunto de dados ordenados.
# Se o conjunto tiver um número par de elementos, a mediana será a média dos dois valores centrais.
mediana = statistics.median(dados)
print(f"Mediana: {mediana}")  # Saída: 35.0

# 3. Cálculo da Moda
# A moda é o número que aparece com mais frequência no conjunto de dados.
moda = statistics.mode(dados)
print(f"Moda: {moda}")  # Saída: 40