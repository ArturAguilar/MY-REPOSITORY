from openai import OpenAI  # Importa a biblioteca OpenAI para interação com a API

client = OpenAI(api_key='')  # Cria um cliente da OpenAI utilizando a chave de API (substitua por uma chave válida)

# Primeira solicitação com temperatura 2
# temperatura é um parâmetro que controla a aleatoriedade da resposta gerada.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Mensagem do usuário pedindo 5 sugestões de nome para um fundo de investimentos
        {"role": "user", "content": "dê 5 sugestões de nome para um fundo de investimentos baseado em inteligência artificial."}
    ],
    temperature=2  # A temperatura 2 aumenta a aleatoriedade, tornando as respostas mais variadas
)

# Exibe a resposta gerada com maior aleatoriedade
print(response.choices[0].message.content)

# Segunda solicitação com temperatura 0
# temperatura 0 reduz a aleatoriedade, gerando respostas mais determinísticas e consistentes.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Mensagem do usuário pedindo 5 sugestões de nome para um fundo de investimentos
        {"role": "user", "content": "dê 5 sugestões de nome para um fundo de investimentos baseado em inteligência artificial."}
    ],
    temperature=0  # A temperatura 0 diminui a aleatoriedade, tornando as respostas mais consistentes
)

# Exibe a resposta gerada com baixa aleatoriedade
print(response.choices[0].message.content)

# Seed: garante a consistência da resposta para uma semente específica, permitindo respostas iguais se a mesma semente for usada.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Define o modelo a ser usado (GPT-3.5-Turbo)
    messages=[
        # Mensagem do usuário pedindo 5 sugestões de nome para um fundo de investimentos
        {"role": "user", "content": "dê 5 sugestões de nome para um fundo de investimentos baseado em inteligência artificial."}
    ],
    temperature=0,  # Mantém a temperatura baixa para respostas consistentes
    seed=0  # Especifica uma semente para garantir que as respostas sejam consistentes
)

# Exibe a resposta gerada com a semente 0 (para consistência nas respostas)
print(response.choices[0].message.content)