# Importando bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Passo 1: Criando dados
# Dados categóricos
categorias = ['Azul', 'Verde', 'Azul', 'Vermelho', 'Verde', 'Azul', 'Amarelo']

# Dados contínuos
dados_continuos = [1.2, 2.3, 3.5, 4.0, 5.1, 3.8, 2.5]

# Passo 2: Calculando a tabela de frequência para dados categóricos
tabela_frequencia_categorias = pd.Series(categorias).value_counts()

# Passo 3: Calculando a distribuição de frequência para dados contínuos
intervalos = pd.cut(dados_continuos, bins=3)
tabela_frequencia_continuos = intervalos.value_counts()

# Passo 4: Gráficos para dados categóricos
# Gráfico de barras
plt.figure(figsize=(8, 4))
plt.bar(tabela_frequencia_categorias.index, tabela_frequencia_categorias.values, color='skyblue')
plt.title("Frequência de Categorias")
plt.xlabel("Categorias")
plt.ylabel("Frequência")
plt.show()

# Gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(tabela_frequencia_categorias.values, labels=tabela_frequencia_categorias.index, autopct='%1.1f%%', colors=['#4CAF50', '#2196F3', '#FFC107', '#FF5722'])
plt.title("Distribuição de Categorias")
plt.show()

# Passo 5: Gráficos para dados contínuos (distribuição de frequência)
# Gráfico de barras para intervalos de classe
plt.figure(figsize=(8, 4))
plt.bar(tabela_frequencia_continuos.index.astype(str), tabela_frequencia_continuos.values, color='coral')
plt.title("Distribuição de Frequência - Dados Contínuos")
plt.xlabel("Intervalos de Classe")
plt.ylabel("Frequência")
plt.show()

# Passo 6: Usando Seaborn para histogramas
# Histograma de dados contínuos com visual mais detalhado
plt.figure(figsize=(8, 4))
sns.histplot(dados_continuos, bins=3, kde=True, color='purple')
plt.title("Histograma de Dados Contínuos com Curva KDE")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.show()