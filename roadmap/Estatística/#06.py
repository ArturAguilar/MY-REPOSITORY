# Importação das bibliotecas necessárias para cálculos, gráficos e estatísticas.
import numpy as np  # Biblioteca para manipulação de arrays e funções matemáticas.
import matplotlib.pyplot as plt  # Biblioteca para criar gráficos.
import seaborn as sns  # Biblioteca para visualizações estatísticas.
import scipy  # Biblioteca para cálculos científicos e estatísticos.

# Parâmetros para uma distribuição normal padrão (média = 0, desvio padrão = 1).
m, s = 0, 1  

# Geração de uma linha de valores no intervalo de -5 a 5, com 1000 pontos.
x = np.linspace(-5, 5, 1000)

# Cálculo da função densidade de probabilidade da distribuição normal (PDF).
y = (1 / (s * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / s) ** 2)

# Plota a distribuição normal com a função de densidade de probabilidade calculada.
plt.plot(x, y)  
plt.show()

# Geração de 100.000 amostras de uma distribuição normal com média 0 e desvio padrão 1.
dados = np.random.normal(m, s, 100000)

# Plota a distribuição dos dados usando a estimativa de densidade kernel (KDE).
#sns.histplot(dados, kde=True, stat="density")  # Este comando foi comentado.
sns.kdeplot(dados)  # Plota a estimativa de densidade kernel (KDE) dos dados.

# Recria a linha de valores e calcula novamente a função densidade de probabilidade para comparação.
x = np.linspace(-5, 5, 100000)
y = (1 / (s * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / s) ** 2)

# Plota a linha da função densidade de probabilidade gerada com a curva KDE em vermelho.
plt.plot(x, y, color='red')  
plt.show()

# Outra forma de gerar amostras de uma distribuição normal utilizando scipy.
dados = scipy.stats.norm.rvs(m, s, 100000)  
# `scipy.stats.norm.rvs` gera 100.000 amostras de uma distribuição normal com média 0 e desvio padrão 1.
print(dados)  # Exibe os dados gerados.

# Calcula a proporção de valores de dados que estão dentro do intervalo -1 <= x <= 1.
b = dados[np.abs(dados) <= 1].shape[0] / 100000  
# `np.abs(dados) <= 1` filtra os valores de dados que estão no intervalo [-1, 1].
print(b)  # Exibe a proporção de valores dentro de um desvio padrão.

# Calcula a proporção de valores de dados que estão dentro do intervalo -2 <= x <= 2.
c = dados[np.abs(dados) <= 2].shape[0] / 100000  
# `np.abs(dados) <= 2` filtra os valores de dados que estão no intervalo [-2, 2].
print(c)  # Exibe a proporção de valores dentro de dois desvios padrão.

# Plota um histograma dos dados gerados para visualização.
sns.histplot(dados)  
plt.show()