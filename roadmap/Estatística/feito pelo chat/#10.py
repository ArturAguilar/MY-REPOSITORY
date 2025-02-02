import math

# Função para calcular permutações
def permutacoes(n, *repeticoes):
    # Se não houver repetições, usamos a fórmula simples n!
    if not repeticoes:
        return math.factorial(n)
    else:
        # Caso haja repetições, usamos a fórmula com divisões pelos fatoriais das repetições
        resultado = math.factorial(n)
        for r in repeticoes:
            resultado //= math.factorial(r)
        return resultado

# Função para calcular combinações
def combinacoes(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Função para calcular arranjos
def arranjos(n, r):
    return math.factorial(n) // math.factorial(n - r)

# Exemplos
print("Exemplo 1 - Permutações da palavra 'CACHORRO' (com repetições):")
print(permutacoes(8, 2, 2))  # 8! / 2!2!

print("\nExemplo 2 - Combinações de 3 pessoas a partir de 10:")
print(combinacoes(10, 3))  # C(10, 3)

print("\nExemplo 3 - Arranjos de 3 livros a partir de 5:")
print(arranjos(5, 3))  # A(5, 3)