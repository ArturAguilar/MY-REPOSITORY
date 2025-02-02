"""
Este módulo fornece definições e conceitos básicos de estatística inferencial, incluindo população, amostra, unidade, censo, parâmetro populacional, função paramétrica populacional e estimadores pontuais. Também inclui uma explicação do Teorema Central do Limite (TCL).

Conceitos:
    - população: conjunto de todos os elementos de um estudo.
    - amostra: conjunto de elementos de um estudo que são representativos da população.
    - unidade: elemento de um estudo.
    - censo: quando todos os elementos da população são observados.
    - parâmetro populacional: característica de uma população.
    - função paramétrica populacional: função que relaciona um parâmetro populacional a uma variável aleatória.
    - estimadores pontuais: estimativas de um parâmetro populacional.

Exemplos de parâmetros populacionais:
    - média (μ)
    - diferença de médias
    - proporção
    - diferença de proporções

Exemplos de estimadores pontuais:
    - média
    - diferença de médias
    - proporção
    - diferença de proporções
"""

"""
Teorema Central do Limite (TCL)
    Definição Matemática: Seja X uma variável aleatória com média μ e desvio padrão σ. Se n for suficientemente grande, a distribuição amostral da média de X se aproxima de uma distribuição normal com média μ e desvio padrão σ/√n.
    - Média: Igual à média da população (μ).
    - Desvio padrão: Igual ao desvio padrão da população (σ/√n).

Implicações Práticas:
    - Generalização: Mesmo que a população original não tenha distribuição normal, as médias amostrais serão aproximadamente normais para amostras grandes.
    - Uso em Inferência Estatística: O TCL permite usar ferramentas baseadas na distribuição normal (como testes de hipóteses e intervalos de confiança) mesmo quando os dados não são normalmente distribuídos.
    - Aplicações Universais: Ele é amplamente usado em diversas áreas, como economia, biologia, física e ciência de dados.
"""

import numpy as np
import matplotlib.pyplot as plt

# População: Distribuição uniforme
# Gerando uma população de 100 mil elementos com valores entre 0 e 100
populacao = np.random.uniform(0, 100, 100000)

# Amostras
tamanho_amostra = 30  # Tamanho de cada amostra
num_amostras = 1000  # Número de amostras a serem coletadas
medias_amostrais = []  # Lista para armazenar as médias amostrais

# Coletando amostras e calculando suas médias
for _ in range(num_amostras):
    amostra = np.random.choice(populacao, tamanho_amostra)  # Coletando uma amostra aleatória da população
    medias_amostrais.append(np.mean(amostra))  # Calculando e armazenando a média da amostra

# Gráfico: População original vs Médias amostrais
plt.figure(figsize=(12, 6))  # Configurando o tamanho da figura

# Histograma da população
plt.subplot(1, 2, 1)  # Criando o primeiro subplot
plt.hist(populacao, bins=50, color='blue', alpha=0.7)  # Plotando o histograma da população
plt.title("Distribuição da População (Uniforme)")  # Título do gráfico
plt.xlabel("Valores")  # Rótulo do eixo X
plt.ylabel("Frequência")  # Rótulo do eixo Y

# Histograma das médias amostrais
plt.subplot(1, 2, 2)  # Criando o segundo subplot
plt.hist(medias_amostrais, bins=50, color='green', alpha=0.7)  # Plotando o histograma das médias amostrais
plt.title("Distribuição das Médias Amostrais (Aproximadamente Normal)")  # Título do gráfico
plt.xlabel("Médias Amostrais")  # Rótulo do eixo X
plt.ylabel("Frequência")  # Rótulo do eixo Y

plt.tight_layout()  # Ajustando o layout para evitar sobreposição
plt.show()  # Exibindo o gráfico