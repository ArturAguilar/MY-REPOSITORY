import numpy as np  # Importando a biblioteca NumPy para operações vetoriais

# Definindo os vetores a e b
a = np.array([2, 3, 4])  # Vetor 'a' no espaço R^3
b = np.array([1, 0, 5])  # Vetor 'b' no espaço R^3

# Calculando o produto vetorial entre 'a' e 'b'
produto_vetorial = np.cross(a, b)  # O produto vetorial é calculado usando np.cross()
# O produto vetorial resulta em um vetor perpendicular a 'a' e 'b'

# Exibindo o produto vetorial
print("Produto vetorial de a e b:", produto_vetorial)

# Calculando a área do paralelogramo formado pelos vetores 'a' e 'b'
area = np.linalg.norm(produto_vetorial)  # A área é dada pelo módulo (norma) do produto vetorial
print("Área do paralelogramo formado por a e b:", area)

# Definindo o vetor posição e a força para calcular o momento de força (torque)
r = np.array([2, 1, 0])  # Vetor posição (r) no espaço R^3
F = np.array([0, 0, 5])  # Vetor força (F) no espaço R^3

# Calculando o momento de força (torque)
torque = np.cross(r, F)  # O momento de força é calculado pelo produto vetorial entre r e F
print("Momento de força (torque):", torque)