from openai import OpenAI  # Importa a biblioteca OpenAI para interação com a API

client = OpenAI(api_key='')  # Cria um cliente da OpenAI usando a chave da API (substitua por uma chave válida)

# O parâmetro 'messages' define a troca de mensagens entre o usuário e o modelo de IA. As mensagens podem ter diferentes papéis:
# 'system': Define instruções ou o contexto inicial para o modelo (exemplo: o modelo se comportando como um professor).
# 'user': Representa a entrada do usuário, ou seja, a pergunta ou pedido que será feito ao modelo.
# 'assistant': Pode ser usada para representar uma mensagem do modelo (geralmente não é fornecida diretamente, mas o modelo a gera em resposta ao 'user').

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Primeira mensagem do sistema definindo o contexto para o modelo
        {"role": "system", "content": "você é um professor de uma escola infantil."},  # Define que o modelo deve agir como um professor de escola infantil

        # Segunda mensagem do usuário pedindo para criar uma mensagem de boas-vindas aos alunos
        {"role": "user", "content": "crie uma mensagem de boas-vindas aos alunos, com cerca de 50 palavras."}  # Pedido do usuário
    ]
)

# Exibe a resposta gerada pelo modelo com base nas mensagens fornecidas
print(response.choices[0].message.content)