# Importação das bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do arquivo CSV que contém os dados de alturas, pesos e sexo
df = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Estatística/planilhas/alturas_pesos.csv')

# Visualização inicial do DataFrame, mostrando as primeiras 5 linhas
df.head()

# Contagem de ocorrências para cada valor na coluna 'sexo' (Feminino e Masculino)
a = df['sexo'].value_counts()
print(a)  # Exibe a quantidade de mulheres e homens no conjunto de dados

# Informações sobre a estrutura do DataFrame, como número de colunas, entradas não nulas e tipos de dados
b = df.info()
print(b)

# Estatísticas descritivas para colunas numéricas (como média, mediana, desvio padrão, etc.)
c = df.describe()
print(c)

# Criação de um histograma para visualizar a distribuição dos valores de altura no conjunto de dados
sns.histplot(data=df, x='altura')
plt.show()  # Exibe o gráfico na tela

# Criação de um histograma para visualizar a distribuição dos valores de peso no conjunto de dados
sns.histplot(data=df, x='peso')
plt.show()  # Exibe o gráfico na tela

# Histograma para visualizar a distribuição de peso, diferenciando por sexo
sns.histplot(data=df, x='peso', hue='sexo')
plt.show()  # Exibe o gráfico, separando os pesos entre homens e mulheres

# Histograma para visualizar a distribuição de altura, diferenciando por sexo
sns.histplot(data=df, x='altura', hue='sexo')
plt.show()  # Exibe o gráfico, separando as alturas entre homens e mulheres

# Separação dos dados em dois subconjuntos com base no sexo
dados = {
    "F": df.query("sexo == 'F'").copy(),  # Subconjunto contendo apenas os dados das mulheres
    "M": df.query("sexo == 'M'").copy()   # Subconjunto contendo apenas os dados dos homens
}
print(dados)  # Exibe os subconjuntos de dados no console