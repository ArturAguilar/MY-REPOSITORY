import numpy as np  # Importando a biblioteca NumPy para operações matriciais

# Definindo a matriz A
A = np.array([[4, 1],   # Primeira linha da matriz A
              [2, 3]])  # Segunda linha da matriz A

# Calculando os autovalores e autovetores da matriz A
autovalores, autovetores = np.linalg.eig(A)  # A função eig() retorna autovalores e autovetores

# Exibindo os autovalores
print("Autovalores:")
print(autovalores)  # Os autovalores são os valores escalares associados à matriz

# Exibindo os autovetores
print("\nAutovetores:")
print(autovetores)  # Os autovetores são as colunas da matriz retornada, onde cada coluna corresponde ao autovetor