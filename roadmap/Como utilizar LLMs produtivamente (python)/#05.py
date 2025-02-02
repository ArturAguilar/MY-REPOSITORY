from openai import OpenAI  # Importa a biblioteca OpenAI para interação com a API

client = OpenAI(api_key='')  # Cria um cliente da OpenAI usando a chave da API (deve ser substituída por uma chave válida)

# Chama a função chat.completions.create para gerar uma resposta com o modelo GPT-4
response = client.chat.completions.create(
    model="gpt-4-1106-preview",  # Especifica o modelo GPT-4 para usar
    messages=[  # A conversa será construída com uma lista de mensagens
        {"role": "user", "content": "crie 4 perguntas para uma entrevista de cientista de dados com foco em NLP."}  # A mensagem do usuário pedindo para gerar perguntas sobre NLP
    ]
)

# Exibe a resposta gerada pelo modelo
print(response.choices[0].message.content)  # A resposta gerada é extraída e exibida