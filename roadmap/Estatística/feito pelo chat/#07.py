# Importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm  # Distribuição normal para exemplos

# 1. Definindo a função de distribuição cumulativa (CDF)
# Exemplo: Função de distribuição cumulativa de uma distribuição normal padrão
def cdf(x):
    return norm.cdf(x)  # CDF da normal padrão (média=0, desvio padrão=1)

# 2. Calculando a densidade de probabilidade (PDF) como a derivada da CDF
def pdf(x):
    return norm.pdf(x)  # PDF da normal padrão

# 3. Gerando valores para visualização
x_values = np.linspace(-4, 4, 500)  # Valores de X de -4 a 4

# Calculando a CDF e a PDF para os valores de X
cdf_values = cdf(x_values)
pdf_values = pdf(x_values)

# 4. Visualizando os gráficos
plt.figure(figsize=(12, 6))

# Gráfico da CDF
plt.subplot(1, 2, 1)
plt.plot(x_values, cdf_values, label="CDF (F(x))", color="blue")
plt.title("Função de Distribuição Cumulativa (CDF)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(alpha=0.5)
plt.legend()

# Gráfico da PDF
plt.subplot(1, 2, 2)
plt.plot(x_values, pdf_values, label="PDF (f(x)) = F'(x)", color="green")
plt.title("Função de Densidade de Probabilidade (PDF)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

# 5. Calculando probabilidades para intervalos
# Exemplo: Probabilidade de -1 <= X <= 1
a, b = -1, 1
probabilidade = cdf(b) - cdf(a)
print(f"A probabilidade de X estar entre {a} e {b} é {probabilidade:.4f}")