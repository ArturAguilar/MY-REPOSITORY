import numpy as np  # Importando a biblioteca NumPy para operações vetoriais

# Definindo os vetores a e b
a = np.array([1, 2, 3])  # Vetor 'a' no espaço R^3
b = np.array([4, 5, 6])  # Vetor 'b' no espaço R^3

# Calculando o produto vetorial entre 'a' e 'b'
produto_vetorial = np.cross(a, b)  # O produto vetorial é calculado usando np.cross()
# O produto vetorial em R^3 resulta em um vetor perpendicular aos vetores 'a' e 'b'

# Exibindo o resultado
print("Produto vetorial de a e b:", produto_vetorial)