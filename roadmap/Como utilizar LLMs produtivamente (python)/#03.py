# Definindo uma frase
frase = "isso é uma frase"

# Contando o número de palavras na frase
n_palavras = len(frase.split())
print(f"Quantidade de palavras: {n_palavras}")

# Estimando o número de tokens (uma média de 0.75 palavras por token)
n_tokens = int(n_palavras / 0.75)
print(f"Quantidade de tokens: {n_tokens}")