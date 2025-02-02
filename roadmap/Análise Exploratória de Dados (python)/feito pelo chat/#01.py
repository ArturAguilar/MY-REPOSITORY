import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame de exemplo
data = {'idade': [22, 25, 27, 29, 35, 40, 44, 50, 50, 60],
        'salario': [1500, 1600, 1700, 1800, 2200, 2500, 3000, 3200, 3300, 3500]}
df = pd.DataFrame(data)

# Estatísticas descritivas
print(df.describe())

# Histogramas para visualizar a distribuição
df['idade'].hist(bins=5, alpha=0.7, color='blue', label='Idade')
df['salario'].hist(bins=5, alpha=0.7, color='green', label='Salário')

plt.legend()
plt.title('Distribuição de Idade e Salário')
plt.show()

# Box plot para detecção de outliers
df.boxplot(column=['idade', 'salario'])
plt.title('Box plot de Idade e Salário')
plt.show()