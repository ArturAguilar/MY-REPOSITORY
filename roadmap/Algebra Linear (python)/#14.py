import numpy as np

# Base canônica
e1 = np.array([1, 0])  # Vetor unitário na direção x
e2 = np.array([0, 1])  # Vetor unitário na direção y

# Componentes dos vetores v e w
v1, v2 = np.array([1, 3])  # Componentes de v
w1, w2 = np.array([2, -1])  # Componentes de w

# Vetores expandidos na base canônica
v = v1 * e1 + v2 * e2  # Definindo o vetor v = v1 * e1 + v2 * e2
w = w1 * e1 + w2 * e2  # Definindo o vetor w = w1 * e1 + w2 * e2

# Produto escalar diretamente (multiplicando os componentes correspondentes)
x = (v * w).sum()  # Produto escalar v . w, onde cada componente é multiplicado
print("Produto escalar (direto):", x)

# Produto escalar usando a função np.dot()
z = np.dot(v, w)  # Produto escalar utilizando np.dot()
print("Produto escalar (np.dot):", z)