# engenharia de prompt (DESCRIÇÂO DA TAREFA)

# descrição da tarefa: é a instrução ou objetivo específico que guia o modelo a realizar uma ação ou responder a uma solicitação de forma alinhada às expectativas do usuário.

from openai import OpenAI

client = OpenAI(api_key = '')

# Este código exemplifica a engenharia de prompt, onde a forma como a tarefa é descrita impacta diretamente na qualidade e precisão da resposta gerada pelo modelo de linguagem.

# Passo 1: Definindo a sentença a ser corrigida.
sentenca = "a selessão brasileira foi campeão quatro vezes na copa do mundo ganhando o título 4 vezes"

# Exemplo 1: Sentença com descrição ruim (vaga).
# O modelo apenas recebe a instrução de corrigir a sentença, mas sem especificações detalhadas.
descricao_ruim = f"corrija essa sentença {sentenca}"

# Chamada da API para corrigir a sentença, mas o modelo pode gerar uma correção simples sem muita refinamento.
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": descricao_ruim}],
    temperature = 1
)

print(response.choices[0].message.content)


# Exemplo 2: Sentença com descrição melhorada (detalhada).
# A descrição da tarefa inclui instruções claras, como corrigir erros gramaticais e remover redundâncias.
descricao_melhor_1 = f"""sua tarefa é reescrever uma sentença. para executar a tarefa com sucesso, siga os 2 passos abaixo:
1) corrija erros gramaticais, ortográficos e de pontuação.
2) remova redundâncias.

sentença: 
{sentenca}
"""

# Chamada da API com uma instrução mais detalhada, o que ajuda o modelo a se concentrar nas correções específicas e melhorar a qualidade da resposta.
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": descricao_melhor_1}],
    temperature = 1
)

print(response.choices[0].message.content)


# Exemplo 3: Sentença com descrição mais detalhada e especializada (adicionando a persona).
# A descrição agora envolve duas etapas: corrigir erros e verificar a veracidade das informações, e o modelo adota a persona de um especialista em história do futebol.
descricao_piorada = f"""
sua tarefa é corrigir uma sentença. a correção deve ser feita em duas etapas:
etapa 1:
    - corrija erros gramaticais, ortográficos e de pontuação.
    - torne a sentença mais concisa.
etapa 2:
    - verifique se as informações contidas na frase são verdadeiras.

sentença: 
{sentenca}
"""

# Chamada da API com uma descrição ainda mais detalhada, que direciona o modelo a ser mais preciso e focado em detalhes históricos, como a veracidade da frase.
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "você é um revisor de textos profisional e especilista em história do futebol"},
        {"role": "user", "content": descricao_piorada}
    ],
    temperature = 1
)

print(response.choices[0].message.content)


# Exemplo 4: A mesma tarefa de correção, mas utilizando o modelo GPT-4, que pode ter uma capacidade maior para realizar tarefas mais detalhadas.
response = client.chat.completions.create(
    model = "gpt-4",
    messages = [
        {"role": "system", "content": "você é um revisor de textos profisional e especilista em história do futebol"},
        {"role": "user", "content": descricao_piorada}
    ],
    temperature = 1
)

print(response.choices[0].message.content)