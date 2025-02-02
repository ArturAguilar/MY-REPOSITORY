import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame com dados de uma série histórica (exemplo: vendas mensais)
dados = {
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'vendas': [200, 220, 210, 250, 270, 280, 290, 300, 310, 320, 330, 350]
}

df = pd.DataFrame(dados)

# Criando os subgráficos com o tamanho da figura definido
plt.figure(figsize=(15, 5))

# Gráfico de Linha
plt.subplot(1, 3, 1)  # Criando o primeiro subplot (1 linha, 3 colunas, 1º gráfico)
plt.plot(df['mes'], df['vendas'], marker='o', linestyle='-', color='b')  # Gráfico de linha com marcadores
plt.title('Gráfico de Linha')  # Título do gráfico
plt.xlabel('Meses')  # Rótulo do eixo X
plt.ylabel('Vendas')  # Rótulo do eixo Y

# Gráfico de Área
plt.subplot(1, 3, 2)  # Criando o segundo subplot (1 linha, 3 colunas, 2º gráfico)
plt.fill_between(df['mes'], df['vendas'], color="skyblue", alpha=0.4)  # Preenchendo a área abaixo da linha
plt.title('Gráfico de Área')  # Título do gráfico
plt.xlabel('Meses')  # Rótulo do eixo X
plt.ylabel('Vendas')  # Rótulo do eixo Y

# Gráfico de Dispersão
plt.subplot(1, 3, 3)  # Criando o terceiro subplot (1 linha, 3 colunas, 3º gráfico)
plt.scatter(df['mes'], df['vendas'], color='r')  # Gráfico de dispersão
plt.title('Gráfico de Dispersão')  # Título do gráfico
plt.xlabel('Meses')  # Rótulo do eixo X
plt.ylabel('Vendas')  # Rótulo do eixo Y

# Ajuste do layout para evitar sobreposição
plt.tight_layout()

# Exibindo os gráficos
plt.show()