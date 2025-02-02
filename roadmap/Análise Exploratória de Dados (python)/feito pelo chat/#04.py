import pandas as pd

# Criando um DataFrame de exemplo com dados faltantes
dados = {
    'nome': ['Ana', 'Carlos', 'João', None, 'Maria'],  # Nome de pessoas, com um valor faltante
    'idade': [23, None, 30, 22, None],  # Idade das pessoas, com valores faltantes
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Belo Horizonte', None],  # Cidade de residência, com valor faltante
    'pais': ['Brasil', 'Brasil', 'Brasil', 'Brasil', 'Brasil']  # Coluna constante (todos os valores são iguais)
}

# Criando o DataFrame a partir dos dados
df = pd.DataFrame(dados)

# 1. Identificar dados faltantes
# A função isnull() retorna True para os valores faltantes (NaN), e sum() conta o número de valores True por coluna
print("Dados faltantes por coluna:")
print(df.isnull().sum())

# 2. Preencher dados faltantes com a média (para a coluna 'idade')
# A função fillna() preenche os valores faltantes com a média da coluna 'idade'
df['idade'] = df['idade'].fillna(df['idade'].mean())

# 3. Identificar e remover colunas constantes
# A função nunique() retorna o número de valores únicos por coluna
print("\nNúmero de valores únicos por coluna:")
print(df.nunique())

# A função loc é utilizada para selecionar apenas as colunas que têm mais de um valor único (removendo as constantes)
df_limpo = df.loc[:, df.nunique() > 1]
print("\nDataFrame após remoção de colunas constantes:")
print(df_limpo)

# 4. Exibir o DataFrame final
# Aqui o DataFrame original é exibido após o preenchimento de valores faltantes e remoção de colunas constantes
print("\nDataFrame final:")
print(df)