# Importação das bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do arquivo CSV que contém os dados de altura e peso
df = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Estatística/planilhas/alturas_pesos.csv')
df.head()  # Exibe as primeiras 5 linhas do DataFrame

# Cálculo da média da coluna 'altura' usando dois métodos diferentes
a = df['altura'].mean()
print(f'Média da altura: {a}')  # Usando o método .mean() do pandas

b = sum(df['altura'].values) / len(df['altura'].values)
print(f'Média da altura: {b}')  # Cálculo manual usando NumPy

# Separação das colunas 'altura' e 'peso' para facilitar análises
c = "altura peso".split()
print(c)  # Lista com os nomes das colunas selecionadas

# Cálculo da média agrupada por sexo para as colunas 'altura' e 'peso'
d = df.groupby('sexo')["altura peso".split()].mean()
print(d)  # Exibe a média agrupada

# Cálculo da mediana agrupada por sexo para as colunas 'altura' e 'peso'
e = df.groupby('sexo')['altura peso'.split()].median()
print(e)  # Exibe a mediana agrupada

# Cálculo do primeiro quartil (Q1) para a coluna 'altura'
f = np.quantile(df['altura'], q=1/4)
print(f)

# Cálculo dos quartis (Q1, Q2, Q3) e exibição dos resultados
q1 = np.quantile(df['altura'], q=0.25)
q2 = np.quantile(df['altura'], q=0.5)
q3 = np.quantile(df['altura'], q=0.75)
print(f'Q1: {q1}, Q2: {q2}, Q3: {q3}')

# Criação de um histograma para a coluna 'altura' com uma curva de densidade
sns.histplot(data=df, x='altura', kde=True)

# Marcação dos quartis e da média no gráfico de histograma
media = df['altura'].mean()

plt.axvline(x=q1, label=f'Q1 = {q1:.2f} cm', color='k', linestyle=':')
plt.axvline(x=q2, label=f'Q2 = {q2:.2f} cm', color='k')
plt.axvline(x=q3, label=f'Q3 = {q3:.2f} cm', color='k', linestyle='-.')
plt.axvline(x=media, label=f'Média = {media:.2f} cm', color='r')

plt.legend(bbox_to_anchor=(1, 0.5), loc='center left')
plt.show()  # Exibe o gráfico

# Cálculo da moda para a coluna 'altura'
g = df['altura'].mode()
print(g)

# Exibição das 10 alturas mais frequentes no conjunto de dados
h = df['altura'].value_counts().iloc[:10]
print(h)

# Contagem de todas as ocorrências para a coluna 'altura'
i = df['altura'].value_counts()
print(i)

# Criação de uma nova coluna 'altura_m' convertendo as alturas para metros
df['altura_m'] = np.round(df['altura'] / 100, 2)

# Contagem de ocorrências para a coluna 'altura_m'
j = df['altura_m'].value_counts()
print(j)

# Cálculo da moda para a nova coluna 'altura_m'
k = df['altura_m'].mode()
print(k)

# Gráfico de densidade para a coluna 'altura_m'
sns.kdeplot(data=df, x='altura_m')

# Recalcular os quartis e a média para a nova coluna 'altura_m'
q1 = np.quantile(df['altura_m'], q=0.25)
q2 = np.quantile(df['altura_m'], q=0.5)
q3 = np.quantile(df['altura_m'], q=0.75)
media = df['altura_m'].mean()

# Marcação dos quartis e da média no gráfico de densidade
plt.axvline(x=q1, label=f'Q1 = {q1:.2f} m', color='k', linestyle=':')
plt.axvline(x=q2, label=f'Q2 = {q2:.2f} m', color='k')
plt.axvline(x=q3, label=f'Q3 = {q3:.2f} m', color='k', linestyle='-.')
plt.axvline(x=media, label=f'Média = {media:.2f} m', color='r')

plt.legend(bbox_to_anchor=(1, 0.5), loc='center left')
plt.show()

# Estatísticas descritivas da coluna 'altura' (mínimo e máximo)
l = df.describe().loc["min max".split()]
print(l)

# Cálculo da amplitude para cada coluna numérica no DataFrame
for altura in df.select_dtypes(include=np.number):
    print(f"Amplitude da variável {altura}: {df[altura].max() - df[altura].min():.2f} cm")

# Outra maneira de calcular e exibir a amplitude das colunas numéricas
for coluna in df.select_dtypes(include=np.number):
    print(f"Amplitude da variável {coluna}: {df[coluna].max() - df[coluna].min():.2f} cm")

# Criação de um histograma simples para a coluna 'altura'
sns.histplot(data=df, x='altura')
plt.show()

# Cálculo do coeficiente de assimetria para a coluna 'altura'
m = df['altura'].skew()
print(m)

# Criação de um boxplot para visualizar a distribuição e possíveis outliers na coluna 'altura'
sns.boxplot(data=df, x='altura')
plt.show()