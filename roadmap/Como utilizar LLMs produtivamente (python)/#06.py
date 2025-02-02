from openai import OpenAI  # Importa a biblioteca OpenAI para interação com a API
import tiktoken  # Biblioteca para codificação e contagem de tokens

client = OpenAI(api_key='')  # Cria um cliente da OpenAI usando a chave da API (deve ser substituída por uma chave válida)

# Lê todo o conteúdo do arquivo para uma única variável de string
with open('arquivo.txt', 'r', encoding='latin-1') as arquivo:  # Abre o arquivo para leitura (a codificação latin-1 é utilizada para lidar com caracteres especiais)
    conteudo = arquivo.read()  # Lê o conteúdo completo do arquivo

# Limita o conteúdo para os primeiros 40.000 caracteres, caso o arquivo seja muito grande
conteudo = conteudo[0:40000]  # Para evitar que o arquivo seja maior que a janela de contexto, limitamos a 40.000 caracteres

# Conta o número de tokens do texto
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")  # Cria um codificador específico para o modelo GPT-3.5-Turbo

# Utiliza o codificador para contar o número de tokens no conteúdo
n_tokens_tiktoken = len(enc.encode(conteudo))  # O método encode transforma o texto em tokens e a função len conta o número de tokens

print(f"número de tokens: {n_tokens_tiktoken}")  # Exibe a quantidade de tokens no texto

# Envia a requisição para o modelo GPT-4 com o conteúdo do arquivo e pede para identificar o tema principal
response = client.chat.completions.create(
    model="gpt-4",  # Modelo GPT-4
    messages=[  # Mensagem do usuário pedindo o tema principal do texto
        {"role": "user", "content": f"qual o principal tema do texto a seguir: {conteudo}"}
    ]
)

# Exibe a resposta gerada pelo modelo
print(response.choices[0].message.content)

# Envia uma nova requisição para o modelo GPT-4-1106-preview, com o mesmo conteúdo, mas pedindo a resposta em português
response = client.chat.completions.create(
    model="gpt-4-1106-preview",  # Modelo GPT-4-1106-preview
    messages=[  # Mensagem do usuário pedindo o tema principal do texto e especificando que a resposta deve ser em português
        {"role": "user", "content": f"qual o principal tema do texto a seguir: {conteudo}. responda em português"}
    ]
)

# Exibe a resposta gerada pelo modelo
print(response.choices[0].message.content)