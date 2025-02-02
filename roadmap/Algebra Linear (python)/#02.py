import numpy as np  # Importando a biblioteca NumPy para operações com matrizes

# Definindo a matriz a (3x3)
a = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Exibindo a matriz original
print("Essa é a matriz:\n", a, "\n")

# Calculando a matriz transposta (trocando as linhas por colunas)
trans = a.T  # A matriz transposta de 'a' é obtida com o atributo .T
print("Essa é a matriz transposta de A: \n", trans, "\n")

# Tentando calcular a matriz inversa
# Para que uma matriz seja invertível, ela precisa ser quadrada e ter um determinante diferente de zero
try:
    inv = np.linalg.inv(a)  # A função np.linalg.inv() calcula a matriz inversa
    print("Essa é a matriz inversa de A:\n", inv, "\n")
except np.linalg.LinAlgError:
    print("A matriz não é invertível (determinante é zero).\n")

# Calculando a matriz identidade (A * A_inv = I)
ident = np.dot(a, inv)  # O produto de A e A_inv deve resultar na matriz identidade
print("Essa é a matriz identidade:\n", ident, "\n")

# Criando a matriz identidade 3x3 diretamente usando np.identity()
i = np.identity(3)  # A função np.identity(n) cria uma matriz identidade de ordem n
print("Matriz identidade 3x3:\n", i)