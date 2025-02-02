# Importação da biblioteca OpenAI para interagir com a API
import openai

# Configuração da chave de API (substitua "sua-chave-de-api" pela sua chave real)
openai.api_key = "sua-chave-de-api"

# Prompt bem estruturado, especificando a pergunta e o formato desejado para a resposta
prompt = """
Você é um assistente especializado em história. Responda à seguinte questão de forma clara, organizada e em tópicos:

Pergunta: Quais foram os principais motivos que levaram à Revolução Industrial?

Formato esperado:
1. Motivo
   - Descrição
2. Motivo
   - Descrição
"""

# Chamando o modelo GPT para gerar uma resposta de acordo com o prompt fornecido
response = openai.Completion.create(
    engine="text-davinci-003",  # Modelo da OpenAI a ser utilizado
    prompt=prompt,  # O prompt que define a pergunta e o formato esperado
    max_tokens=150,  # Limite de tokens (palavras) para a resposta
    temperature=0.7,  # Controla a criatividade da resposta (valores entre 0 e 1)
    top_p=0.9,  # Controla a diversidade das respostas (valor mais alto resulta em maior diversidade)
    frequency_penalty=0.2,  # Penaliza palavras repetidas
    presence_penalty=0.3  # Penaliza a presença de palavras que já apareceram na resposta
)

# Exibindo a resposta gerada pelo modelo (retirando espaços extras no início ou fim)
print(response.choices[0].text.strip())