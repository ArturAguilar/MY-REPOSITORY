# Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Criando o conjunto de dados fictício
# Variável independente (X): Número de horas de estudo
# Variável dependente (Y): Nota na prova
horas_estudo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reformatando para array 2D
notas_prova = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])  # Array 1D

# 2. Visualizando os dados em um gráfico de dispersão
plt.figure(figsize=(8, 5))
plt.scatter(horas_estudo, notas_prova, color='blue', label='Dados')
plt.title('Horas de Estudo vs Nota na Prova')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota na Prova')
plt.grid(alpha=0.5, linestyle='--')
plt.legend()
plt.show()

# 3. Criando o modelo de regressão linear
modelo = LinearRegression()

# Treinando o modelo com os dados (ajuste da linha de regressão)
modelo.fit(horas_estudo, notas_prova)

# Obtendo os coeficientes da linha de regressão
intercepto = modelo.intercept_  # Intercepto (β0)
coeficiente = modelo.coef_[0]   # Coeficiente angular (β1)

print(f"Equação da linha de regressão: Y = {intercepto:.2f} + {coeficiente:.2f}X")

# 4. Fazendo previsões com o modelo
notas_previstas = modelo.predict(horas_estudo)

# 5. Visualizando a linha de regressão
plt.figure(figsize=(8, 5))
plt.scatter(horas_estudo, notas_prova, color='blue', label='Dados reais')
plt.plot(horas_estudo, notas_previstas, color='red', label='Linha de Regressão')
plt.title('Regressão Linear Simples')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota na Prova')
plt.grid(alpha=0.5, linestyle='--')
plt.legend()
plt.show()

# 6. Avaliando o modelo
# Métrica 1: Erro quadrático médio (MSE)
mse = mean_squared_error(notas_prova, notas_previstas)
print(f"Erro Quadrático Médio (MSE): {mse:.2f}")

# Métrica 2: Coeficiente de Determinação (R²)
r2 = r2_score(notas_prova, notas_previstas)
print(f"Coeficiente de Determinação (R²): {r2:.2f}")

# 7. Fazendo previsões para novos dados
# Por exemplo: Prevendo a nota de uma pessoa que estudou 7,5 horas
nova_hora = np.array([[7.5]])
nota_prevista = modelo.predict(nova_hora)
print(f"Nota prevista para 7,5 horas de estudo: {nota_prevista[0]:.2f}")