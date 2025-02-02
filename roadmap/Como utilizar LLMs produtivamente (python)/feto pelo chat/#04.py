import openai

# Configuração da chave da API (substitua "sua-chave-de-api" pela sua chave real)
openai.api_key = "sua-chave-de-api"

# Função para responder perguntas de clientes com a ajuda da API do OpenAI
def responder_pergunta(pergunta):
    # Definindo o prompt com um exemplo de perguntas e respostas
    prompt = f"""
    Você é um assistente virtual para uma loja online. Responda à pergunta abaixo de forma clara e eficiente.

    Exemplo de pergunta e resposta:
    1. Pergunta: "Como rastrear meu pedido?"
       Resposta: "Olá! Acesse nosso portal de rastreamento e insira o número do pedido para verificar o status."
    2. Pergunta: "Posso devolver um produto?"
       Resposta: "Claro! Você pode iniciar o processo de devolução em nossa página de devoluções. Certifique-se de que está dentro do prazo de 30 dias após a entrega."

    Agora, responda à seguinte pergunta:
    "{pergunta}"
    """

    # Chamada à API do OpenAI para gerar a resposta com base no prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Usando o modelo mais avançado "text-davinci-003"
        prompt=prompt,  # Passando o prompt gerado anteriormente
        max_tokens=100,  # Limita o número de tokens (palavras) na resposta
        temperature=0.7  # Controla a criatividade da resposta (valor entre 0 e 1)
    )

    # Retorna a resposta gerada, removendo espaços extras no início ou fim
    return response.choices[0].text.strip()

# Exemplo de pergunta do cliente
pergunta_cliente = "Quais são as formas de pagamento disponíveis?"

# Chamando a função para obter a resposta
resposta = responder_pergunta(pergunta_cliente)

# Exibindo a pergunta e a resposta
print(f"Pergunta: {pergunta_cliente}")
print(f"Resposta: {resposta}")