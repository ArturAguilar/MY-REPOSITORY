import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Definindo os parâmetros
n = 10  # Número de tentativas
p = 0.5  # Probabilidade de sucesso
k = np.arange(0, n+1)  # Possíveis números de sucessos (0 a n)

# Calculando a probabilidade de cada número de sucessos
probabilidades = binom.pmf(k, n, p)

# Exibindo os resultados
plt.bar(k, probabilidades, color="skyblue")
plt.title("Distribuição Binomial (10 lançamentos, p=0.5)")
plt.xlabel("Número de Sucessos")
plt.ylabel("Probabilidade")
plt.grid(True)
plt.show()