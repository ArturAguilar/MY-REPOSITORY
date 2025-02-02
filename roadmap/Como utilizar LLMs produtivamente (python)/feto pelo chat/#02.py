import openai

# Configuração da API
openai.api_key = "sua-chave-de-api"

# Configuração do GPT com parâmetros ajustados
response = openai.chat.completions.create(
    engine="text-davinci-003",  # Modelo
    prompt="Explique o que é aprendizado de máquina de forma simples.",
    max_tokens=100,            # Limite de tokens na resposta
    temperature=0.7,           # Criatividade
    top_p=0.9,                 # Amostra por núcleo
    frequency_penalty=0.2,     # Penaliza repetições
    presence_penalty=0.3       # Incentiva tópicos novos
)

# Resultado gerado
print(response.choices[0].text.strip())
