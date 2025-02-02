import numpy as np  # Importando a biblioteca NumPy para operações matemáticas

# Definindo a transformação linear: multiplicação por 2
def transformacao_linear(vetor):
    """
    Função para aplicar uma transformação linear simples.
    Neste caso, cada componente do vetor será multiplicado por 2.
    """
    # Multiplicando cada componente do vetor por 2
    return 2 * vetor

# Exemplo de vetor em R^2 (um vetor com duas dimensões)
vetor = np.array([1, 3])

# Aplicando a transformação linear
vetor_transformado = transformacao_linear(vetor)

# Exibindo os vetores original e transformado
print("Vetor original:", vetor)
print("Vetor transformado:", vetor_transformado)


# Definindo a matriz da transformação linear
matriz_transformacao = np.array([[2, 0],  # Linha 1: fator de escala 2 para x
                                  [0, 3]])  # Linha 2: fator de escala 3 para y

# Exemplo de vetor em R^2 (o mesmo vetor usado antes)
vetor = np.array([1, 3])

# Aplicando a transformação linear usando a multiplicação de matrizes
# A multiplicação da matriz pela coluna do vetor é equivalente a aplicar a transformação
vetor_transformado = np.dot(matriz_transformacao, vetor)

# Exibindo os resultados
print("\nMatriz de transformação:")
print(matriz_transformacao)
print("Vetor original:", vetor)
print("Vetor transformado:", vetor_transformado)