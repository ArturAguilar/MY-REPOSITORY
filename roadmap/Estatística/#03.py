# Importação das bibliotecas necessárias.
import pandas as pd  # Biblioteca para análise e manipulação de dados.
import numpy as np  # Biblioteca para operações numéricas e geração de dados aleatórios.

# Definição de variáveis iniciais.
n = 10000  # Número total de lançamentos da moeda.
cara = 5010  # Número de vezes que deu "cara".
coroa = n - cara  # Número de vezes que deu "coroa" (calculado como o restante dos lançamentos).

# Exibe os valores absolutos de "cara" e "coroa".
print(cara, coroa)

# Cálculo das probabilidades de "cara" e "coroa".
p_cara = cara / n  # Probabilidade de dar "cara".
p_coroa = coroa / n  # Probabilidade de dar "coroa".

# Exibe as probabilidades de "cara" e "coroa".
print(p_cara, p_coroa)

# Simulação de 100 lançamentos de moeda e contagem dos resultados.
a = pd.Series(np.random.randint(0, 2, 100)).value_counts()  
# `np.random.randint(0, 2, 100)` gera uma sequência de 100 números aleatórios entre 0 e 1 (0 para "coroa" e 1 para "cara").
# `pd.Series(...).value_counts()` cria uma série do pandas e conta a frequência de cada valor (quantidade de "cara" e "coroa").