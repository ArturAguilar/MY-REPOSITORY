from openai import OpenAI  # Importa a biblioteca OpenAI para interação com a API

client = OpenAI(api_key='')  # Cria um cliente da OpenAI usando a chave da API (substitua por uma chave válida)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Mensagem do sistema que define o contexto para o modelo. Aqui, o modelo deve agir como o diretor de um conselho universitário.
        {"role": "system", "content": "você é o diretor do conselho de universidade de finanças mundialmente renomado."},

        # Mensagem do usuário pedindo para criar uma mensagem de boas-vindas aos alunos, com a condição de que tenha cerca de 50 palavras
        {"role": "user", "content": "crie uma mensagem de boas-vindas aos alunos. sua mensagem deve conter aproximadamente 50 palavras."}
    ]
)

# Exibe a resposta gerada pelo modelo com base nas mensagens fornecidas
print(response.choices[0].message.content)