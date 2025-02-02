import numpy as np
import matplotlib.pyplot as plt

# Definindo o vetor original
v = np.array([1, 1])

# a) rotação
theta = np.pi / 4  # ângulo de rotação em radianos (45 graus)
r = np.array([[np.cos(theta), -np.sin(theta)],   # matriz de rotação 2x2
              [np.sin(theta), np.cos(theta)]])
rotated_v = np.dot(r, v)  # aplicação da rotação no vetor original

# b) escalonamento
s = np.array([[2, 0],    # matriz de escalonamento (2x2)
              [0, 0.5]])  # fator de escala para x e y
scaled_v = np.dot(s, v)  # aplicação do escalonamento no vetor original

# c) reflexão
f = np.array([[1, 0],    # matriz de reflexão (2x2) no eixo x
              [0, -1]])  # inverte o sinal de y
reflected_v = np.dot(f, v)  # aplicação da reflexão no vetor original

# d) cisalhamento
h = np.array([[1, 0.5],  # matriz de cisalhamento (2x2) no eixo x
              [0, 1]])    # desloca o componente x de acordo com y
sheared_v = np.dot(h, v)  # aplicação do cisalhamento no vetor original

# Plotando os vetores transformados
plt.figure(figsize=(10, 8))

# Vetor original
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original')

# Vetor após rotação
plt.quiver(0, 0, rotated_v[0], rotated_v[1], angles='xy', scale_units='xy', scale=1, color='red', label='Rotação')

# Vetor após escalonamento
plt.quiver(0, 0, scaled_v[0], scaled_v[1], angles='xy', scale_units='xy', scale=1, color='green', label='Escalonamento')

# Vetor após reflexão
plt.quiver(0, 0, reflected_v[0], reflected_v[1], angles='xy', scale_units='xy', scale=1, color='yellow', label='Reflexão')

# Vetor após cisalhamento
plt.quiver(0, 0, sheared_v[0], sheared_v[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Cisalhamento')

# Ajustando os limites dos eixos
plt.xlim(-1, 3)  # limite do eixo x
plt.ylim(-1, 3)  # limite do eixo y

# Labels e título
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)  # linha do eixo x
plt.axvline(0, color='black', linewidth=0.5)  # linha do eixo y
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # linha de grade
plt.gca().set_aspect('equal', adjustable='box')  # manter proporção igual nos eixos
plt.legend()  # adicionar legenda
plt.title("Transformações Lineares Aplicadas a um Vetor")

# Exibindo o gráfico
plt.show()