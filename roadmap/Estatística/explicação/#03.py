"""
Distribuição de Bernoulli
    Descrição: é uma das mais simples e fundamentais em estatística. Ela descreve experimentos que têm apenas dois resultados possíveis: sucesso ou falha (também chamados de 1 e 0).
    Exemplo: O lançamento de uma moeda, onde cara é sucesso e coroa é falha.

Características da Distribuição de Bernoulli
    Definição: Um experimento de Bernoulli tem uma única tentativa, onde:
    - A probabilidade de sucesso é p.
    - A probabilidade de falha é 1 - p.

    Variável Aleatória: A variável X assume apenas dois valores:
    x = {1, com probabilidade p 
         0, com probabilidade 1 - p}

    Função de Probabilidade: P(X = x) = p^x * (1 - p)^(1 - x)

    média = E[X] = p
    variância = Var[X] = p * (1 - p)
"""

"""
Distribuição Uniforme
    Descrição: Todos os eventos têm a mesma probabilidade de ocorrer.
    Exemplo: O lançamento de um dado honesto, onde todos os números (1 a 6) têm a mesma chance de ocorrer.

    formula (discreta)
    Se n é o número de eventos possíveis, p(x = x) = 1 / n

    formula (contínua)
    para a < x < b, f(x) = 1 / (b - a) 
"""

"""
Distribuição Normal (ou Gaussiana)
    Descrição: É uma das distribuições mais importantes. É simétrica em torno da média e tem formato de sino.
    Parâmetros: Média (μ) e Desvio Padrão (σ).
    exemplo: altura de uma população.

    formula: f(x) = (1 / (σ * sqrt(2 * π))) * exp(-((x - μ)² / (2 * σ²)))
"""

"""
Distribuição Binomial
    Descrição: Modela o número de sucessos em n tentativas independentes. Cada uma com a mesma probabilidade de sucesso (p)
    Exemplo: O número de caras ao lançar uma moeda 10 vezes.
    Fórmula: P(X = k) = (n! / (k! * (n - k)!)) * p^k * (1 - p)^(n - k)
"""

"""
Distribuição de Poisson
    Descrição: Modela o número de eventos que ocorrem em um intervalo de tempo ou espaço fixo.
    Exemplo: Número de chamadas recebidas por um call center em uma hora.
    Fórmula: P(X = k) = (λ^k * exp(-λ)) / k!
"""

"""
Distribuição Exponencial
    Descrição: Modela o tempo entre dois eventos consecutivos em um processo de Poisson.
    Exemplo: O tempo até a próxima chamada em um call center.
    Fórmula: f(x) = λ * exp(-λ * x)
"""

"""
Distribuição Geométrica
    Descrição: Modela o número de tentativas até o primeiro sucesso em experimentos de Bernoulli.
    Exemplo: Número de lançamentos de um dado até obter o número 6.
    Fórmula: P(X = k) = (1 - p)^(k - 1) * p
"""

"""
Distribuição T de Student
    Descrição: É usada quando temos um tamanho de amostra pequeno e não conhecemos o desvio-padrão da população.
    Exemplo: Comparação de médias entre duas amostras pequenas.
    Fórmula: Complexa, geralmente definida pela função densidade específica.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson

# 1. Distribuição Normal
mu, sigma = 0, 1  # média e desvio-padrão
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y, label='Normal (μ=0, σ=1)')

# 2. Distribuição Binomial
n, p = 10, 0.5  # tentativas e probabilidade de sucesso
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)
plt.bar(x, y, alpha=0.6, label='Binomial (n=10, p=0.5)')

# 3. Distribuição de Poisson
lambda_ = 3  # taxa média de eventos
x = np.arange(0, 15)
y = poisson.pmf(x, lambda_)
plt.bar(x, y, alpha=0.6, label='Poisson (λ=3)')

plt.legend()
plt.title('Exemplos de Distribuições de Probabilidade')
plt.show()