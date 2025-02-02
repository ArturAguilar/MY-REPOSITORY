# Função para criar uma matriz identidade de tamanho n
def matriz_identidade(n):
    """
    Cria uma matriz identidade de tamanho n x n.
    A matriz identidade é uma matriz quadrada onde os elementos
    da diagonal principal são 1 e os demais são 0.
    """
    identidade = []  # Lista que armazenará as linhas da matriz identidade
    for i in range(n):
        linha = []  # Inicializa uma nova linha
        for j in range(n):
            if i == j:
                linha.append(1)  # Insere 1 na diagonal principal
            else:
                linha.append(0)  # Insere 0 fora da diagonal
        identidade.append(linha)  # Adiciona a linha à matriz
    return identidade

# Exemplo de uso: Criando uma matriz identidade 3x3
matriz_id = matriz_identidade(3)

# Exibindo a matriz identidade
print("Matriz Identidade 3x3:")
for linha in matriz_id:
    print(linha)


# Função para criar uma matriz nula de tamanho n x m
def matriz_nula(n, m):
    """
    Cria uma matriz nula de tamanho n x m.
    A matriz nula é composta inteiramente por zeros.
    """
    # Compreensão de listas para criar a matriz com 0 em todas as posições
    nula = [[0 for _ in range(m)] for _ in range(n)]
    return nula

# Exemplo de uso: Criando uma matriz nula 3x3
matriz_n = matriz_nula(3, 3)

# Exibindo a matriz nula
print("\nMatriz Nula 3x3:")
for linha in matriz_n:
    print(linha)


# Função para criar uma matriz diagonal
def matriz_diagonal(lista):
    """
    Cria uma matriz diagonal onde os elementos da diagonal principal
    correspondem aos valores da lista fornecida. Os elementos fora da
    diagonal principal são 0.
    """
    n = len(lista)  # O tamanho da matriz será igual ao tamanho da lista
    diagonal = []  # Lista que armazenará as linhas da matriz diagonal
    for i in range(n):
        linha = [0] * n  # Inicializa uma linha com todos os elementos iguais a 0
        linha[i] = lista[i]  # Insere o elemento da lista na diagonal principal
        diagonal.append(linha)  # Adiciona a linha à matriz
    return diagonal

# Exemplo de uso: Criando uma matriz diagonal com os valores [4, 5, 6]
matriz_diag = matriz_diagonal([4, 5, 6])

# Exibindo a matriz diagonal
print("\nMatriz Diagonal com elementos [4, 5, 6]:")
for linha in matriz_diag:
    print(linha)