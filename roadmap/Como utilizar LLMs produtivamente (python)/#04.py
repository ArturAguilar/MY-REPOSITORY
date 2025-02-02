import tiktoken  # Importa a biblioteca tiktoken para manipulação e contagem de tokens

# Define a codificação do modelo GPT-3.5
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Solicita que o usuário digite uma frase
frase = input("digite uma frase: ")

# Conta o número de tokens da frase
n_tokens_tiktoken = len(enc.encode(frase))  # A função 'encode' divide a frase em tokens e 'len' conta quantos tokens existem

# Exibe o número de tokens
print(f"Quantidade de tokens: {n_tokens_tiktoken}")