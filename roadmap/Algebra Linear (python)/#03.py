import numpy as np  # Importando a biblioteca NumPy para operações com matrizes

# Definindo as matrizes a e b
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

b = np.array([[9, 8, 7], 
              [6, 5, 4], 
              [3, 2, 1]])

# Adição de Matrizes
x1 = a + b  # A adição de matrizes é feita somando elemento a elemento
print("A soma da matriz A e B: \n", x1, "\n")

# Subtração de Matrizes
x2 = a - b  # A subtração de matrizes é feita subtraindo elemento a elemento
print("A subtração da matriz A e B: \n", x2, "\n")

# Multiplicação de Matrizes (elemento a elemento)
x3 = a * b  # A multiplicação entre matrizes no NumPy, quando usamos * (multiplicação element-wise), 
# significa que estamos multiplicando cada elemento correspondente de a e b
print("A multiplicação da matriz A e B: \n", x3, "\n")

# Não existe divisão de matrizes. O que podemos fazer é multiplicar por uma matriz inversa quando possível