# Importando bibliotecas necessárias
import numpy as np
import pandas as pd
from scipy import stats

# Criando dados de exemplo (dados fictícios)
dados = [12, 15, 14, 10, 13, 14, 15, 16, 12, 11, 12, 15, 14]

# 1. Medidas de Posição
# Média
media = np.mean(dados)  # Soma dos valores dividida pelo total de elementos
print(f"Média: {media:.2f}")

# Mediana
mediana = np.median(dados)  # Valor central dos dados ordenados
print(f"Mediana: {mediana:.2f}")

# Moda
moda, contagem = stats.mode(dados)  # Valor mais frequente nos dados
print(f"Moda: {moda[0]} (aparece {contagem[0]} vezes)")

# 2. Medidas de Dispersão (Variabilidade)
# Amplitude
amplitude = np.ptp(dados)  # Diferença entre o maior e o menor valor
print(f"Amplitude: {amplitude}")

# Variância
variancia = np.var(dados, ddof=1)  # Variância amostral (ddof=1 para amostra)
print(f"Variância: {variancia:.2f}")

# Desvio padrão
desvio_padrao = np.std(dados, ddof=1)  # Raiz quadrada da variância
print(f"Desvio Padrão: {desvio_padrao:.2f}")

# Coeficiente de variação
coeficiente_variacao = (desvio_padrao / media) * 100  # Expressa a variabilidade como porcentagem da média
print(f"Coeficiente de Variação: {coeficiente_variacao:.2f}%")

# Visualização Gráfica para Contextualizar
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

# Distribuição dos Dados
plt.hist(dados, bins=5, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(media, color='red', linestyle='--', label=f'Média: {media:.2f}')
plt.axvline(mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.2f}')
plt.axvline(moda[0], color='purple', linestyle='--', label=f'Moda: {moda[0]}')

plt.title("Distribuição dos Dados e Medidas de Posição")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()