# Importa a biblioteca necessária para se conectar à API do OpenAI
from openai import OpenAI

# Inicializa o cliente do OpenAI com a chave da API
client = OpenAI(api_key = '')

# Sentença de exemplo que contém um erro gramatical
sentenca = "a selessão brasileira foi campeão 5 vezes na copa do mundo ganhando o título 5 vezes"

# Descrição da tarefa com exemplos de como corrigir sentenças
descricao_com_exemplos = f"""
Sua tarefa é corrigir uma sentença. Para executar a tarefa com sucesso, siga os passos abaixo:

Corrija erros gramaticais, ortográficos e de pontuação.
Torne a sentença mais concisa.
Abaixo, seguem dois exemplos para guiar suas respostas:
Exemplo 1:
<input> A seleção argentina foi campeão três vezes na copa do mundo ganhando em 3 ocasiões.
<output> ('correcao': 'A seleção argentina foi campeã da Copa do Mundo três vezes.', 'erros': 'sim')

Exemplo 2:
<input> A seleção francesa foi campeã da Copa do Mundo três vezes.
<output> ('correcao': 'A seleção francesa foi campeã da Copa do Mundo três vezes.', 'erros': 'não')

Sentença a ser corrigida:
<input> {sentenca}
"""

# Envia a solicitação de correção para a API do OpenAI, utilizando o modelo "gpt-3.5-turbo"
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "você é um revisor de textos profissional."},  # Definindo o perfil do assistente
        {"role": "user", "content": descricao_com_exemplos}  # Passando a tarefa junto com os exemplos
    ],
    temperature = 0  # Configuração de "temperatura" para controlar a aleatoriedade (0 para respostas mais consistentes)
)

# Exibe a resposta gerada pelo modelo
print(response.choices[0].message.content)