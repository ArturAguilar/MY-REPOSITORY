# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Criando um conjunto de dados fictício
# Variáveis: Altura (em cm) e Peso (em kg)
dados = {
    'Altura': [150, 160, 165, 170, 175, 180, 185, 190, 195, 200],
    'Peso': [50, 55, 60, 65, 70, 80, 85, 90, 100, 110]
}

# Convertendo para um DataFrame
df = pd.DataFrame(dados)

# 1. Visualizando os dados
print("Conjunto de Dados:\n", df)

# 2. Gráfico de dispersão (scatter plot)
plt.figure(figsize=(8, 5))
plt.scatter(df['Altura'], df['Peso'], color='blue', alpha=0.7, label='Dados')
plt.title('Relação entre Altura e Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.grid(alpha=0.5, linestyle='--')
plt.legend()
plt.show()

# 3. Cálculo da Correlação (Pearson)
# A correlação mede a força e a direção da relação linear entre duas variáveis
correlacao, p_valor = pearsonr(df['Altura'], df['Peso'])
print(f"Coeficiente de Correlação de Pearson: {correlacao:.2f}")
print(f"P-valor: {p_valor:.4f}")

# 4. Interpretação dos Resultados
if correlacao > 0.7:
    interpretacao = "Correlação forte positiva"
elif 0.3 < correlacao <= 0.7:
    interpretacao = "Correlação moderada positiva"
elif 0 < correlacao <= 0.3:
    interpretacao = "Correlação fraca positiva"
elif -0.3 <= correlacao < 0:
    interpretacao = "Correlação fraca negativa"
elif -0.7 <= correlacao < -0.3:
    interpretacao = "Correlação moderada negativa"
else:
    interpretacao = "Correlação forte negativa"

print(f"Interpretação da Correlação: {interpretacao}")