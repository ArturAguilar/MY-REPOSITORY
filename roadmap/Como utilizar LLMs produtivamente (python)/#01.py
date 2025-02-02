import openai

# Configuração da chave da API (substitua 'sua-chave-de-api' pela sua chave real)
openai.api_key = 'sua-chave-de-api'

# Exemplo 1: Chamamos a função chat completions.create da biblioteca openai para iniciar uma interação com o modelo GPT-3.5 Turbo.

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Usando o modelo GPT-3.5-turbo
    messages=[  # Passando as mensagens que formarão o contexto da interação
        {'role': 'user', 'content': 'A capital da França é'}  # Pergunta do usuário
    ]
)

# Exibindo a resposta do modelo
print(response['choices'][0]['message']['content'])