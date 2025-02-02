import sqlite3

# Função que verifica se o usuário tem permissão para inserir dados
def verificar_permissao(usuario):
    # Verifica se o usuário é 'admin' e retorna True para permissão, caso contrário False
    if usuario == 'admin':
        return True
    return False

# Função para inserir um produto se o usuário tiver permissão
def inserir_produto(nome_produto, preco_produto, usuario):
    # Verifica se o usuário tem permissão
    if not verificar_permissao(usuario):
        print(f"Usuário {usuario} não tem permissão para inserir dados!")  # Exibe mensagem de erro
        return
    # Conecta ao banco de dados
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    # Insere os dados do produto na tabela Produtos
    cursor.execute('''
    INSERT INTO Produtos (Nome_Produto, Preco_Produto)
    VALUES (?, ?)
    ''', (nome_produto, preco_produto))  # Substitui os valores pelos parâmetros passados
    # Salva as mudanças
    conn.commit()
    # Fecha a conexão
    conn.close()
    # Exibe mensagem de sucesso
    print(f"Produto {nome_produto} inserido com sucesso!")

# Função para criar uma view que mostre os clientes e seus produtos
def criar_view():
    # Conecta ao banco de dados
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    # Cria uma view que junta as tabelas Clientes, Produtos e Pedidos
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS View_Cliente_Produto AS
    SELECT Clientes.Nome_Cliente, Produtos.Nome_Produto, Produtos.Preco_Produto
    FROM Pedidos
    JOIN Clientes ON Pedidos.ID_Cliente = Clientes.ID_Cliente
    JOIN Produtos ON Pedidos.ID_Produto = Produtos.ID_Produto;
    ''')  # A consulta SQL junta as tabelas Clientes e Produtos através da tabela Pedidos
    # Salva as mudanças
    conn.commit()
    # Fecha a conexão
    conn.close()
    # Exibe mensagem de sucesso
    print("View criada com sucesso!")

# Função para consultar dados da view
def consultar_view():
    # Conecta ao banco de dados
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    # Consulta todos os dados da view
    cursor.execute('SELECT * FROM View_Cliente_Produto')
    resultados = cursor.fetchall()  # Obtém todos os resultados da consulta
    # Exibe os resultados
    for resultado in resultados:
        print(resultado)
    # Fecha a conexão
    conn.close()

# Teste de inserção de dados com permissão
usuario = 'admin'  # Mude para testar o acesso
inserir_produto('Camiseta', 49.99, usuario)  # Chama a função para inserir o produto

# Criando a view
criar_view()  # Chama a função para criar a view

# Consultando os dados da view
consultar_view()  # Chama a função para consultar os dados da view