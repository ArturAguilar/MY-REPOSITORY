# Função para calcular o Teorema de Bayes
def bayes(P_B_given_A, P_A, P_B):
    return (P_B_given_A * P_A) / P_B

# Exemplo de Diagnóstico de Doença
P_Doenca = 0.1  # Probabilidade de ter a doença
P_Positivo_given_Doenca = 0.9  # Probabilidade de teste positivo dado que a pessoa tem a doença
P_Positivo = 0.2  # Probabilidade de teste positivo

# Aplicando o Teorema de Bayes
P_Doenca_given_Positivo = bayes(P_Positivo_given_Doenca, P_Doenca, P_Positivo)

print(f"A probabilidade de ter a doença, dado um teste positivo, é: {P_Doenca_given_Positivo:.2f}")