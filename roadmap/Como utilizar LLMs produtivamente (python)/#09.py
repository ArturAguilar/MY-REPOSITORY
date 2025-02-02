from openai import OpenAI  # Importa a biblioteca OpenAI para interação com a API

client = OpenAI(api_key='')  # Cria um cliente da OpenAI utilizando a chave de API (substitua por uma chave válida)

# Primeira solicitação: o modelo deve gerar uma mensagem de boas-vindas com aproximadamente 30 tokens
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Mensagem do sistema para definir o contexto do modelo
        {"role": "system", "content": "você é o diretor do conselho de universidade de finanças mundialmente renomado."},
        
        # Mensagem do usuário pedindo para gerar uma mensagem de boas-vindas com aproximadamente 30 tokens
        {"role": "user", "content": "crie uma mensagem de boas-vindas aos alunos. sua mensagem deve conter aproximadamente 30 tokens."}
    ]
)

# Exibe a resposta gerada pelo modelo com base na solicitação
print(response.choices[0].message.content)

# Segunda solicitação: aqui o parâmetro `max_tokens` limita o número máximo de tokens que o modelo pode gerar
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Mensagem do sistema para definir o contexto do modelo
        {"role": "system", "content": "você é o diretor do conselho de universidade de finanças mundialmente renomado."},
        
        # Mensagem do usuário pedindo para gerar uma mensagem de boas-vindas aos alunos
        {"role": "user", "content": "crie uma mensagem de boas-vindas aos alunos."}
    ],
    max_tokens=30  # Limita a resposta a no máximo 30 tokens
)

# Exibe a resposta gerada pelo modelo com a limitação de tokens
print(response.choices[0].message.content)