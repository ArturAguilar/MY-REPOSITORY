import openai

# Definir chave da API
openai.api_key = 'sua-chave-de-api'  # Substitua pela sua chave da API real

# Definimos o texto do review a ser analisado
review = "o novo smartphone da marca x é incrivel, com uma bateria de longa duração e uma câmera de alta qualidade."

# Chamamos a função chat completions.create
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Usando o modelo GPT-3.5-turbo
    messages=[
        {"role": "user", "content": f"quais são os principais pontos positivos elencados pelo cliente na seguinte review de um produto: {review}"}
    ]
)

# Exibimos a resposta
print(response['choices'][0]['message']['content'])