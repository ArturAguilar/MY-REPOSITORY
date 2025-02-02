# Função para calcular o determinante de uma matriz 2x2
def determinante_2x2(matriz):
    """
    Calcula o determinante de uma matriz 2x2.
    Fórmula do determinante:
    det(A) = a*d - b*c
    Onde:
    - a, b: elementos da primeira linha
    - c, d: elementos da segunda linha
    """
    a, b = matriz[0]  # Primeira linha: elementos a e b
    c, d = matriz[1]  # Segunda linha: elementos c e d
    return a * d - b * c  # Determinante calculado pela fórmula

# Exemplo de uso: Matriz 2x2
matriz_2x2 = [[4, 2],  # Primeira linha
              [3, 1]]  # Segunda linha

# Calculando e exibindo o determinante da matriz 2x2
det_2x2 = determinante_2x2(matriz_2x2)
print(f"Determinante da matriz 2x2: {det_2x2}")


# Função para calcular o determinante de uma matriz 3x3
def determinante_3x3(matriz):
    """
    Calcula o determinante de uma matriz 3x3 usando a regra de Sarrus.
    Fórmula do determinante:
    det(A) = a(ei − fh) − b(di − fg) + c(dh − eg)
    Onde:
    - a, b, c: elementos da primeira linha
    - d, e, f: elementos da segunda linha
    - g, h, i: elementos da terceira linha
    """
    # Extraindo os elementos da matriz
    a, b, c = matriz[0]  # Primeira linha
    d, e, f = matriz[1]  # Segunda linha
    g, h, i = matriz[2]  # Terceira linha
    
    # Calculando o determinante pela fórmula
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

# Exemplo de uso: Matriz 3x3
matriz_3x3 = [[1, 2, 3],  # Primeira linha
              [0, 4, 5],  # Segunda linha
              [1, 0, 6]]  # Terceira linha

# Calculando e exibindo o determinante da matriz 3x3
det_3x3 = determinante_3x3(matriz_3x3)
print(f"Determinante da matriz 3x3: {det_3x3}")