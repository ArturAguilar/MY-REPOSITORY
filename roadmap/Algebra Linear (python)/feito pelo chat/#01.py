# Criando uma matriz simples (uma lista de listas em Python).
# Cada sublista representa uma linha da matriz.
matriz = [
    [1, 2, 3],  # Linha 1
    [4, 5, 6],  # Linha 2
    [7, 8, 9]   # Linha 3
]

# Exibindo toda a matriz como está armazenada (uma lista de listas)
print("Matriz completa:")
print(matriz)

# Acessando um elemento específico na matriz.
# No exemplo, estamos acessando o elemento na linha 2, coluna 3.
# Em Python, os índices começam do 0, então a linha 2 é `matriz[1]` e a coluna 3 é `[2]`.
elemento = matriz[1][2]
print("\nElemento na linha 2, coluna 3:", elemento)

# Iterando pela matriz e exibindo cada linha.
print("\nElementos linha por linha:")
for linha in matriz:
    print(linha)

# Iterando pela matriz e exibindo os elementos individualmente.
print("\nElementos individualmente:")
for linha in matriz:  # Itera sobre cada linha na matriz
    for elemento in linha:  # Itera sobre cada elemento dentro da linha
        print(elemento, end=" ")  # Exibe os elementos lado a lado, separados por espaço