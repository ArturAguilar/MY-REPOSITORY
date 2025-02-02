import numpy as np  # Importando a biblioteca NumPy para operações matriciais

# Definindo os vetores v1 e v2
v1 = np.array([1, 2])  # Vetor v1 no espaço R^2
v2 = np.array([2, 4])  # Vetor v2 no espaço R^2

# Empilhando os vetores em uma matriz
vetores = np.array([v1, v2]).T  # Transposta para criar colunas. Agora a matriz tem v1 e v2 como colunas

# Calculando o posto da matriz (rank)
rank = np.linalg.matrix_rank(vetores)  # O posto da matriz indica o número de vetores linearmente independentes

# Exibindo o posto da matriz
print("Posto da matriz (rank):", rank)  # O posto da matriz representa a quantidade de vetores linearmente independentes

# Se o posto for igual ao número de vetores, eles são linearmente independentes
if rank == len(v1):  # Verifica se o posto é igual ao número de vetores (se eles são independentes)
    print("Os vetores são linearmente independentes e formam uma base.")
else:
    print("Os vetores são linearmente dependentes.")  # Caso contrário, os vetores são linearmente dependentes