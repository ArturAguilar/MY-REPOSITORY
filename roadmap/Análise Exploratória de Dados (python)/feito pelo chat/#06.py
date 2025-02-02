import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame com variáveis categóricas
dados = {
    'categoria': ['A', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'B', 'A'],
    'grupo': ['X', 'X', 'Y', 'Y', 'X', 'Z', 'Z', 'X', 'Y', 'Z']
}

df = pd.DataFrame(dados)

# Contagem de frequências das categorias
# O método value_counts() é utilizado para contar o número de ocorrências de cada categoria
contagem_categoria = df['categoria'].value_counts()
contagem_grupo = df['grupo'].value_counts()

# Gráfico de barras para a variável 'categoria'
plt.figure(figsize=(12, 6))  # Definindo o tamanho da figura

# Subplot 1: Gráfico de barras para 'categoria'
plt.subplot(1, 2, 1)  # Criando o primeiro subplot (1 linha, 2 colunas, 1º gráfico)
plt.bar(contagem_categoria.index, contagem_categoria.values)  # Criando o gráfico de barras
plt.xlabel('Categorias')  # Rótulo do eixo X
plt.ylabel('Frequência')  # Rótulo do eixo Y
plt.title('Distribuição das Categorias')  # Título do gráfico

# Subplot 2: Gráfico de pizza para 'grupo'
plt.subplot(1, 2, 2)  # Criando o segundo subplot (1 linha, 2 colunas, 2º gráfico)
plt.pie(contagem_grupo.values, labels=contagem_grupo.index, autopct='%1.1f%%', startangle=90)
# Criando o gráfico de pizza com os valores de 'grupo', com percentuais e rotacionando o gráfico em 90º
plt.title('Distribuição dos Grupos')  # Título do gráfico
plt.axis('equal')  # Garantindo que o gráfico de pizza seja circular

# Ajustando o layout para que os gráficos não se sobreponham
plt.tight_layout()

# Exibindo os gráficos
plt.show()