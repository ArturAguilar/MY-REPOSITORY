import numpy as np

# Definindo os vetores
a = np.array([1, 2, 6])
b = np.array([5, 2, 1])
c = np.array([2, 2, 10])

# Calculando o produto vetorial entre a e b
produto_vetorial = np.cross(a, b)

# Calculando o produto escalar entre c e o resultado do produto vetorial
produto_escalar = np.dot(c, produto_vetorial)

# Calculando o valor absoluto do produto escalar
x = np.abs(produto_escalar)

print(x)