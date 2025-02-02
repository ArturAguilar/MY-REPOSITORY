import numpy as np

# Definindo o vetor original (1, 1)
v = np.array([[1], [1]])

# a) Rotação
theta = np.pi / 4  # Ângulo de rotação em radianos (45 graus)
# Matriz de rotação 2D
r = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
# Aplicando a rotação ao vetor
rotated_v = np.dot(r, v)

# b) Escalonamento
# Matriz de escalonamento (dobra no eixo x e reduz pela metade no eixo y)
s = np.array([[2, 0],
              [0, 0.5]])
# Aplicando o escalonamento ao vetor
scaled_v = np.dot(s, v)

# c) Reflexão
# Matriz de reflexão em relação ao eixo x
f = np.array([[1, 0],
              [0, -1]])
# Aplicando a reflexão ao vetor
reflected_v = np.dot(f, v)

# d) Cisalhamento
# Matriz de cisalhamento (adicionando 0.5 ao componente x)
h = np.array([[1, 0.5],
              [0, 1]])
# Aplicando o cisalhamento ao vetor
sheared_v = np.dot(h, v)

# Exibindo os resultados
print("\na) rotação:")
print(rotated_v)  # Resultado da rotação do vetor
print("\nb) escalonamento:")
print(scaled_v)  # Resultado do escalonamento do vetor
print("\nc) reflexão:")
print(reflected_v)  # Resultado da reflexão do vetor
print("\nd) cisalhamento:")
print(sheared_v)  # Resultado do cisalhamento do vetor