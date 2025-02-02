# Importação das bibliotecas necessárias
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Criação de um array com os dados das visitas ao restaurante
visitas_restaurante = np.array([3, 4, 7, 8, 8, 9, 25, 50, 8, 5, 4, 3, 3])

# Exibição dos dados ordenados (crescente)
print(sorted(visitas_restaurante))

# Exibição do tamanho do array (número de elementos)
print(len(visitas_restaurante))

# Exibição dos dados novamente ordenados (repetido)
print(sorted(visitas_restaurante))

# Cálculo e exibição da mediana
print(np.median(visitas_restaurante))

# Cálculo e exibição da média
print(visitas_restaurante.mean())

# Criação de um histograma para visualizar a distribuição dos dados
sns.histplot(visitas_restaurante, kde=True)
plt.show()

# Cálculo da amplitude total (diferença entre o valor máximo e o mínimo)
a = visitas_restaurante.max() - visitas_restaurante.min()
print(a)

# Cálculo da amplitude interquartil (Q3 - Q1)
b = np.quantile(visitas_restaurante, q=0.75) - np.quantile(visitas_restaurante, q=0.25)
print(b)