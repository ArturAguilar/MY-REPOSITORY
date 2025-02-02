import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Criando um DataFrame com várias variáveis (exemplo: vendas, lucro e custos)
dados = {
    'vendas': [200, 220, 210, 250, 270, 280, 290, 300, 310, 320],
    'lucro': [20, 22, 21, 25, 27, 28, 29, 30, 31, 32],
    'custos': [150, 160, 155, 170, 180, 185, 190, 195, 200, 210]
}

df = pd.DataFrame(dados)

# 1. Calculando a correlação entre 'vendas' e 'lucro'
correlacao_vendas_lucro = df['vendas'].corr(df['lucro'])
print(f'Correlação entre Vendas e Lucro: {correlacao_vendas_lucro}')

# 2. Regressão linear entre 'vendas' e 'lucro'
# X será a variável independente (vendas), e y será a variável dependente (lucro)
X = df['vendas'].values.reshape(-1, 1)  # Ajustando a forma para ser uma matriz de uma coluna
y = df['lucro'].values

# Criando e treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Prevendo lucro com base nas vendas
lucro_previsto = modelo.predict(X)

# Exibindo coeficiente angular e intercepto
print(f'Coeficiente angular da regressão: {modelo.coef_[0]}')
print(f'Intercepto da regressão: {modelo.intercept_}')

# 3. Criando gráficos

# Gráfico de dispersão entre Vendas e Lucro
plt.figure(figsize=(15, 5))

# Gráfico de Dispersão (Vendas vs Lucro)
plt.subplot(1, 3, 1)  # Primeiro gráfico: Dispersão
plt.scatter(df['vendas'], df['lucro'], color='b')
plt.title('Dispersão entre Vendas e Lucro')
plt.xlabel('Vendas')
plt.ylabel('Lucro')

# Gráfico de Regressão Linear (Vendas vs Lucro com a linha de regressão)
plt.subplot(1, 3, 2)  # Segundo gráfico: Regressão Linear
plt.scatter(df['vendas'], df['lucro'], color='b')  # Pontos de dados
plt.plot(df['vendas'], lucro_previsto, color='r', linestyle='--')  # Linha de regressão
plt.title('Regressão Linear entre Vendas e Lucro')
plt.xlabel('Vendas')
plt.ylabel('Lucro')

# Matriz de Correlação entre as variáveis
plt.subplot(1, 3, 3)  # Terceiro gráfico: Matriz de Correlação
matriz_correlacao = df.corr()  # Calculando a correlação entre todas as colunas do DataFrame
plt.imshow(matriz_correlacao, cmap='coolwarm', interpolation='none')  # Exibindo a matriz como imagem
plt.colorbar()  # Barra de cores para a escala de correlação
plt.xticks(range(len(matriz_correlacao.columns)), matriz_correlacao.columns, rotation=90)  # Rótulos no eixo x
plt.yticks(range(len(matriz_correlacao.columns)), matriz_correlacao.columns)  # Rótulos no eixo y
plt.title('Matriz de Correlação')

# Exibindo os gráficos
plt.tight_layout()  # Ajustando o layout para evitar sobreposição
plt.show()  # Mostrando os gráficos