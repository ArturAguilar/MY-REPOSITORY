# Importação da biblioteca OpenAI para interagir com a API
import openai

# Configuração da chave de API (substitua "sua-chave-de-api" pela sua chave real)
openai.api_key = "sua-chave-de-api"

# Solicitação para o modelo GPT gerar um texto baseado no prompt fornecido
response = openai.Completion.create(
    engine="text-davinci-003",  # Modelo de IA usado (pode usar "gpt-3.5-turbo" para uma opção mais econômica)
    prompt="Escreva uma introdução sobre o impacto da inteligência artificial na sociedade.",  # Texto inicial para o modelo gerar uma resposta
    max_tokens=100  # Limite de tokens (palavras) para a resposta gerada (ajustável conforme a necessidade)
)

# Exibir o resultado gerado, acessando o primeiro texto da lista de escolhas (caso haja várias)
print(response.choices[0].text.strip())  # .strip() remove espaços extras no início ou fim do texto