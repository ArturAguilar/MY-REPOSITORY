import numpy as np

# Criando uma matriz aleatória 5x5
a = np.random.randint(0, 10, size=(5, 5))  # Matriz de inteiros aleatórios entre 0 e 10
x1 = np.linalg.det(a)  # Calculando o determinante de A
print("\nEssa é a matriz aleatória de tamanho 5x5:\n", a, "\n\nEsse é o determinante da matriz acima: ", x1, "\n")

# Criando uma matriz aleatória 3x4 (não quadrada)
b = np.random.randint(0, 10, size=(3, 4))  # Matriz de inteiros aleatórios entre 0 e 10, mas com 3 linhas e 4 colunas
print("Matriz b (não quadrada):\n", b)

# Tentando calcular o determinante de uma matriz não quadrada
try:
    x2 = np.linalg.det(b)  # Tentando calcular o determinante de b
    print("\nDeterminante de b:", x2)
except np.linalg.LinAlgError:
    print("\nNão é possível calcular o determinante de uma matriz não quadrada.")