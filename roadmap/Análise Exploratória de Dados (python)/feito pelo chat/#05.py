import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um DataFrame de exemplo com outliers
dados = {
    'valor': [10, 12, 13, 12, 14, 15, 100, 16, 14, 11, 15, 18, 300]
}

df = pd.DataFrame(dados)

# Gerar boxplot para identificar outliers
# O boxplot ajuda a visualizar os valores atípicos (outliers) por meio da caixa (IQR) e dos pontos fora dos limites.
plt.boxplot(df['valor'])
plt.title("Boxplot para Identificação de Outliers")
plt.show()

# Calcular o IQR (Intervalo Interquartil)
Q1 = df['valor'].quantile(0.25)  # 1º quartil (25%)
Q3 = df['valor'].quantile(0.75)  # 3º quartil (75%)
IQR = Q3 - Q1  # Intervalo interquartil (distância entre Q3 e Q1)

# Definir limites para outliers com base no IQR
# Limite inferior e superior para detectar outliers
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Identificar outliers
# Filtramos os valores fora dos limites definidos
outliers = df[(df['valor'] < limite_inferior) | (df['valor'] > limite_superior)]
print("Outliers identificados:")
print(outliers)

# Tratamento: Remover outliers
# Utilizamos a função isin para excluir os valores identificados como outliers
df_sem_outliers = df[~df['valor'].isin(outliers['valor'])]
print("\nDataFrame sem outliers:")
print(df_sem_outliers)

# Tratamento: Substituir outliers pela mediana
# Substituímos os outliers pela mediana da coluna 'valor'
mediana = df['valor'].median()
df['valor'] = df['valor'].apply(lambda x: mediana if x > limite_superior or x < limite_inferior else x)
print("\nDataFrame com outliers substituídos pela mediana:")
print(df)

# Tratamento: Aplicar transformação logarítmica
# Transformação logarítmica para reduzir o impacto de valores extremos
df['valor_transformado'] = np.log(df['valor'])
print("\nDataFrame com transformação logarítmica:")
print(df)