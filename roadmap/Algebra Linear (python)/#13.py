import numpy as np

# Definindo a matriz A
A = np.array([[6, -1], 
              [2, 3]])

# Calculando os autovalores e autovetores de A
autovalores, autovetores = np.linalg.eig(A)

# Criando a matriz diagonal com os autovalores
matriz_diagonal = np.diag(autovalores)

# Imprimindo os resultados
print("\nAutovalores:")
print(autovalores)  # Exibe os autovalores da matriz A
print("\nAutovetores:")
print(autovetores)  # Exibe os autovetores da matriz A

# Mostrando a matriz diagonal com os autovalores
print("\nMatriz diagonal:\n", matriz_diagonal)

# BONUS - Reconstruindo a matriz A através da decomposição espectral
# A decomposição espectral é dada por A = V * D * V⁻¹, onde V são os autovetores e D é a matriz diagonal com os autovalores

reconstruida = autovetores @ matriz_diagonal @ np.linalg.inv(autovetores)  # Reconstrução de A
print("\nMatriz original:\n", reconstruida)  # Exibe a matriz reconstruída