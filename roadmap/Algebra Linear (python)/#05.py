import numpy as np

# Definindo a matriz A (coeficientes das equações) e o vetor b (resultados)
a = np.array([[1, 2, 3], 
              [2, 3, 3], 
              [1, 2, 0]])
b = np.array([1, -3, 6])

# Calculando o inverso da matriz A
inv_a = np.linalg.inv(a)

# Resolvendo o sistema de equações lineares com a matriz inversa
x = np.dot(inv_a, b)  # Multiplicamos a matriz inversa de A por b
print("\nA solução usando a matriz inversa é x =", x)

# Resolvendo o sistema de equações lineares diretamente com np.linalg.solve
x_solve = np.linalg.solve(a, b)  # Método direto para resolver o sistema
print("\nA solução usando o solve é:", x_solve)