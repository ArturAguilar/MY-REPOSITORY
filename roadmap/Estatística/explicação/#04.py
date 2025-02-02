"""
Medidas de Tendência Central
    Essas medidas nos ajudam a entender onde os dados se concentram. As principais são:

    Média: A média aritmética é a soma de todos os valores dividida pelo número de valores.
    Mediana: A mediana é o valor que divide o conjunto de dados em duas metades, sendo o valor do meio quando os dados estão ordenados.
        Se o número de elementos for ímpar, a mediana é o valor do meio.
        Se for par, a mediana é a média dos dois valores centrais.
    Moda: A moda é o valor que aparece com maior frequência no conjunto de dados.
"""

"""
Medidas de Dispersão
    Essas medidas ajudam a entender a variabilidade dos dados. As principais são:

    Desvio-padrão (σ): O desvio-padrão é a média das diferenças quadradas entre cada valor e a média. Ele nos dá uma ideia de quão dispersos os dados estão em relação à média.
    formula: σ = √(Σ(xi - μ)² / N)

    Variância (σ²): A variância é o quadrado do desvio-padrão. Ela nos dá uma ideia da dispersão dos dados em relação à média.
    formula: σ² = Σ(xi - μ)² / N

    Amplitude: A amplitude é a diferença entre o maior e o menor valor do conjunto de dados. Ela nos dá uma ideia da variação total dos dados.
    formula: Amplitude = Valor Máximo - Valor Mínimo
"""

"""
Medidas de Posição
    Essas medidas fornecem informações sobre a posição de um valor dentro do conjunto de dados.

    Quartis: São os valores que dividem o conjunto de dados ordenado em quatro partes iguais:
        Q1 (1º quartil): 25% dos dados são menores que Q1.
        Q2 (2º quartil ou mediana): 50% dos dados são menores que Q2.
        Q3 (3º quartil): 75% dos dados são menores que Q3.
    Percentis: Dividem o conjunto de dados em 100 partes iguais. O p-ésimo percentil é o valor abaixo do qual 𝑝% dos dados caem.
    Valor Máximo e Mínimo: O maior e o menor valor do conjunto de dados.
"""

"""
Tabelas e Gráficos
    A estatística descritiva também inclui a organização dos dados em tabelas e a criação de gráficos para facilitar a visualização. Alguns gráficos comuns são:

        Histograma: Usado para mostrar a distribuição de um conjunto de dados contínuos.
        Gráfico de barras: Usado para dados categóricos ou discretos.
        Boxplot (diagrama de caixa): Mostra a dispersão dos dados através de quartis e valores atípicos.
"""

import numpy as np
import matplotlib.pyplot as plt

# Exemplo de dados
dados = [12, 15, 14, 10, 18, 20, 12, 14, 13, 11]

# Medidas de tendência central
media = np.mean(dados)
mediana = np.median(dados)
moda = np.argmax(np.bincount(dados))

# Medidas de dispersão
desvio_padrao = np.std(dados)
variancia = np.var(dados)
amplitude = np.max(dados) - np.min(dados)

# Medidas de posição
q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)  # Mediana
q3 = np.percentile(dados, 75)

# Exibindo os resultados
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desvio-padrão: {desvio_padrao}")
print(f"Variância: {variancia}")
print(f"Amplitude: {amplitude}")
print(f"Quartil 1 (Q1): {q1}")
print(f"Quartil 2 (Q2): {q2}")
print(f"Quartil 3 (Q3): {q3}")

# Gráfico Boxplot
plt.boxplot(dados)
plt.title("Boxplot dos Dados")
plt.show()