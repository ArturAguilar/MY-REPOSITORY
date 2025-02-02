import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv('dados.csv')

# 1. Visão geral dos dados
print("Primeiras 5 linhas:")
print(df.head())

# 2. Resumo Estatístico
print("\nResumo estatístico:")
print(df.describe())

# 3. Tipos de dados e valores nulos
print("\nInformações gerais:")
print(df.info())

# 4. Verificar valores ausentes
print("\nValores ausentes em cada coluna:")
print(df.isnull().sum())

# 5. Verificar registros duplicados
print("\nRegistros duplicados:")
print(df.duplicated().sum())

# 6. Verificar distribuição de uma variável categórica
print("\nDistribuição de 'coluna_categorica':")
print(df['coluna_categorica'].value_counts())

# 7. Visualizar box plot para detectar outliers
df.boxplot()
plt.show()

# 8. Visualizar histogramas para a distribuição de variáveis numéricas
df.hist(bins=10, figsize=(10, 7))
plt.show()