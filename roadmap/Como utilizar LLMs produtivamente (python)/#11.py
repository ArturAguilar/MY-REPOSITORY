from openai import OpenAI  # Importa a biblioteca OpenAI para interagir com a API

client = OpenAI(api_key='')  # Cria um cliente OpenAI usando a chave de API (substitua pela sua chave válida)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Definindo a persona do sistema
        {"role": "system", "content": "você é o diretor do conselho de universidade de finanças mundialmente renomado."},  # Contextualiza a persona do modelo

        # Solicitação do usuário para o modelo de linguagem
        {"role": "user", "content": "crie uma mensagem de boas vindas aos alunos. sua mensagem deve conter aproximadamente 50 palavras."}
    ]
)

# Exibe a resposta gerada com a personalidade definida pela persona
print(response.choices[0].message.content)