# Importação das bibliotecas necessárias para cálculos numéricos, gráficos e estatísticas.
import numpy as np  # Biblioteca para manipulação de arrays e funções matemáticas.
import math  # Biblioteca para funções matemáticas básicas, como fatorial.
import scipy  # Biblioteca para cálculos estatísticos, como a distribuição de Poisson.
import pandas as pd  # Biblioteca para manipulação de dados em forma de DataFrames.
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos.

# Definindo os parâmetros da distribuição de Poisson.
l = 20  # Taxa média de eventos (número esperado de ligações).
k = 15  # Número específico de eventos (número de ligações observadas).

# Solução 1: Cálculo da distribuição de Poisson manualmente usando a fórmula.
a = math.factorial(10)  # Cálculo do fatorial de 10 (exemplo de uso de math.factorial).
print(a)  # Exibe o resultado do fatorial de 10.

# Cálculo da probabilidade de obter exatamente 15 ligações (k = 15) com taxa λ = 20 usando a fórmula da distribuição de Poisson.
p_151 = (np.exp(-l)*(l**k))/math.factorial(k)
# `np.exp(-l)` calcula e^(-λ), `l**k` calcula λ^k e `math.factorial(k)` calcula k!.
print(f"{p_151:.2%}")  # Exibe a probabilidade formatada como porcentagem com 2 casas decimais.

# Solução 2: Cálculo da probabilidade usando a função do scipy para a distribuição de Poisson.
p_152 = scipy.stats.poisson.pmf(k=k, mu=l)  
# `scipy.stats.poisson.pmf(k=k, mu=l)` calcula a probabilidade de Poisson usando os parâmetros fornecidos.
print(f"{p_152:.2%}")  # Exibe a probabilidade calculada pelo scipy, formatada como porcentagem.

# Inicializando um dicionário para armazenar os dados do experimento.
experimento = {
    "número de ligações": [],  # Lista para armazenar diferentes valores de k (número de ligações).
    "probabilidade": []  # Lista para armazenar as probabilidades associadas a cada valor de k.
}

# Lista de valores de k de 0 a 39.
k_list = range(40)

# Loop para calcular a probabilidade para cada valor de k de 0 a 39.
for k in k_list:
    p = (scipy.stats.poisson.pmf(k=k, mu=l))  # Calcula a probabilidade de Poisson para cada valor de k.
    experimento["número de ligações"].append(k)  # Adiciona o valor de k à lista de "número de ligações".
    experimento["probabilidade"].append(p)  # Adiciona a probabilidade correspondente à lista.

# Criação de um DataFrame a partir do dicionário "experimento".
df_experimento = pd.DataFrame(experimento)
print(df_experimento)  # Exibe o DataFrame com as probabilidades calculadas para cada valor de k.

# Formatação das probabilidades no DataFrame para exibição com 9 casas decimais.
df_experimento["p_formatado"] = df_experimento["probabilidade"].apply(lambda x: f"{x:.9%}")
print(df_experimento)  # Exibe a tabela com as probabilidades formatadas como porcentagens.

# Cálculo da soma acumulada das probabilidades.
df_experimento["p_acum"] = df_experimento["probabilidade"].cumsum().apply(lambda x: f"{x:.9%}")
print(df_experimento)  # Exibe a tabela com as probabilidades acumuladas, formatadas.

# Plotagem do gráfico da distribuição de Poisson para diferentes valores de k.
b = plt.plot(df_experimento["número de ligações"], df_experimento["probabilidade"])  
# O gráfico exibe a probabilidade associada a cada número de ligações (k).
plt.show()  # Exibe o gráfico.