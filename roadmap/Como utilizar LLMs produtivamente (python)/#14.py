# Importa as bibliotecas necessárias para se conectar à API do OpenAI e para contar tokens
from openai import OpenAI
import tiktoken

# Inicializa o cliente da API do OpenAI com a chave da API
client = OpenAI(api_key = '')

# Texto de exemplo de uma certidão de imóvel que será analisada
texto = """
A presente escritura confirma que João Carlos Silva, CPF 123.456.789-00, adquiriu legalmente o terreno de registro número 4567-AB, no ano de 2021. Avaliado em R$ 350.000,00, este terreno possui uma área total de 500 metros quadrados, situado na Rua das Acácias, nº 200, Bairro Jardim Florido, São Paulo, SP. A propriedade tem topografia plana, frente de 20 metros para a rua principal e está livre de ônus e restrições. Regularizado junto às autoridades municipais, com todos os impostos quitados até a presente data, este documento, registrado no Cartório de Imóveis da Região, atesta a propriedade e os direitos de João Carlos Silva sobre o terreno.
"""

# Define a persona do modelo, que será um analista imobiliário
persona = "você é um analista do setor imobiliário com vasta experiência no setor"

# Definição do prompt com a tarefa a ser realizada: extrair dados específicos da certidão do imóvel
prompt = f"""
você receberá uma certidão de um imóvel. sua tarefa consiste em extrair as informações listadas e responder esses topícos
* nome do proprietario
* ano do registro
* número do registro
* valor do terreno
* localização do terreno
* metragem do terreno

escritura a ser analisada:{texto}
"""

# Chama a API do OpenAI para realizar a tarefa de extração das informações
response = client.chat.completions.create(
    model = "gpt-3.5-turbo",  # Utiliza o modelo gpt-3.5-turbo para gerar a resposta
    messages = [
        {"role": "system", "content": persona},  # Define o papel do assistente como analista imobiliário
        {"role": "user", "content": prompt}     # Passa a tarefa com o texto da escritura
    ],
    temperature = 0  # Temperatura 0 significa respostas mais consistentes e determinísticas
)

# Exibe a resposta gerada pelo modelo
print(response.choices[0].message.content)

# Utiliza o tiktoken para contar o número de tokens no prompt e na resposta gerada
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

n_tokens_input = len(enc.encode(prompt))  # Conta os tokens no prompt
n_tokens_output = len(enc.encode(response.choices[0].message.content))  # Conta os tokens na resposta gerada

# Define os custos por token de entrada e saída para o modelo gpt-3.5-turbo
custo_por_token = {
    "gpt-3.5-turbo": {
        "input": 0.001,  # Custo por token de entrada
        "output": 0.002  # Custo por token de saída
    }
}

# Calcula o custo total dos tokens de entrada e saída
custo_tokens_input = 5 * (custo_por_token.get("gpt-3.5-turbo").get('input') * n_tokens_input) / 1000
custo_tokens_output = 5 * (custo_por_token.get("gpt-3.5-turbo").get('output') * n_tokens_output) / 1000

# Exibe o custo total da tarefa em reais
print(f"custo total da tarefa: R${custo_tokens_input + custo_tokens_output}")  # R$