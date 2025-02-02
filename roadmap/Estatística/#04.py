# Importação de bibliotecas necessárias para análise de dados, visualização e estatística.
import pandas as pd  # Biblioteca para manipulação de dados.
import matplotlib.pyplot as plt  # Biblioteca para criar gráficos.
import seaborn as sns  # Biblioteca para visualizações estatísticas.
import scipy  # Biblioteca para cálculos científicos e estatísticos.

# Carregamento do dataset Titanic a partir de um arquivo CSV.
df_titanic = pd.read_csv('/home/arturaguilar426/GitHub/projetos/Plus-Education.github.io/Estatística/planilhas/titanic.csv')

# Análise descritiva da variável "Age" (idade).
a = df_titanic['Age'].describe()  
# O método `.describe()` retorna estatísticas descritivas como média, mediana, desvio padrão, valores mínimo e máximo, e quartis.
print(a)

# Gráfico de histograma da variável "Age".
b = sns.histplot(data=df_titanic, x='Age')  
# `sns.histplot` cria um histograma que mostra a distribuição das idades.
plt.show()

# Gráfico de densidade (KDE) da variável "Age".
c = sns.kdeplot(data=df_titanic, x='Age')  
# `sns.kdeplot` mostra a densidade estimada da variável "Age" usando kernel density estimation (KDE).
plt.show()

# Gráfico de histograma combinado com KDE para a variável "Age".
d = sns.histplot(data=df_titanic, x='Age', kde=True)  
# O argumento `kde=True` adiciona a curva de densidade ao histograma.
plt.show()

# Simulação de 100 lançamentos de uma variável aleatória de Bernoulli com probabilidade de sucesso `p=0.5`.
resultado_ber = scipy.stats.bernoulli.rvs(p=0.5, size=100)  
# `scipy.stats.bernoulli.rvs` gera valores de 0 ou 1 (falha ou sucesso) com base na probabilidade fornecida.
print(resultado_ber)

# Frequência relativa dos resultados da simulação de Bernoulli.
e = pd.Series(resultado_ber).value_counts(normalize=True)  
# `.value_counts(normalize=True)` retorna as proporções de cada valor (0 ou 1) na série.
print(e)

# Gráfico de contagem dos resultados da simulação de Bernoulli.
f = sns.countplot(resultado_ber)  
# `sns.countplot` cria um gráfico de barras que mostra a frequência de cada valor (0 ou 1).
plt.show()

# Histograma dos resultados de Bernoulli, mostrando densidade (proporção em vez de contagem).
g = sns.histplot(resultado_ber, stat='density')  
# O argumento `stat='density'` ajusta o gráfico para mostrar a densidade relativa dos valores.
plt.show()

# Repetição do histograma dos resultados de Bernoulli.
h = sns.histplot(resultado_ber, stat='density')  
plt.show()

# Extração da coluna "survived" do dataset Titanic (sobreviventes).
i = df_titanic["survived"]  
# A coluna "survived" contém 1 para sobreviventes e 0 para não sobreviventes.
print(i)

# Gráfico de contagem de sobreviventes no Titanic.
j = sns.countplot(data=df_titanic, x="survived")  
# `sns.countplot` exibe o número de sobreviventes e não sobreviventes.
plt.show()

# Cálculo da proporção média de sobreviventes.
k = i.mean()  
# A média da coluna "survived" representa a proporção de sobreviventes no total de passageiros.
print(k)

# Frequência relativa de sobreviventes e não sobreviventes.
l = i.value_counts(normalize=True)  
# `.value_counts(normalize=True)` calcula as proporções de sobreviventes e não sobreviventes no total.
print(l)