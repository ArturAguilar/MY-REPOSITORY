import pandas as pd

# Criando um DataFrame de exemplo
dados = {
    'regiao': ['Norte', 'Sul', 'Leste', 'Oeste', 'Norte', 'Sul', 'Leste', 'Oeste'],
    'produto': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'vendas': [100, 150, 200, 250, 120, 180, 220, 270],
}

# Criando o DataFrame a partir dos dados
df = pd.DataFrame(dados)

# Agrupar os dados por região e calcular a soma das vendas
# A função groupby cria grupos com base na coluna 'regiao'
# A função sum soma os valores de vendas para cada grupo (região)
agrupado_soma = df.groupby('regiao')['vendas'].sum()
print("Soma das vendas por região:")
print(agrupado_soma)

# Agrupar os dados por região e calcular a média das vendas
# A função mean calcula a média dos valores de vendas para cada grupo (região)
agrupado_media = df.groupby('regiao')['vendas'].mean()
print("\nMédia das vendas por região:")
print(agrupado_media)