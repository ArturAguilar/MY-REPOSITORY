import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('loja.db')
cursor = conn.cursor()

# Criar a tabela Produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos (
    ID_Produto INTEGER PRIMARY KEY,      -- ID único do produto, chave primária
    Nome_Produto TEXT NOT NULL,          -- Nome do produto (não pode ser nulo)
    Preco_Produto REAL NOT NULL          -- Preço do produto (não pode ser nulo)
);
''')

# Inserir dados na tabela Produtos
cursor.execute('''
INSERT INTO Produtos (Nome_Produto, Preco_Produto)
VALUES
    ('Camiseta', 49.99),
    ('Calça', 89.99),
    ('Tênis', 120.00),
    ('Jaqueta', 150.00),
    ('Meia', 10.00)
''')  # Insere cinco produtos na tabela

# Criar um índice na coluna Preco_Produto para acelerar buscas por preço
cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_preco_produto ON Produtos (Preco_Produto);
''')  # Cria um índice na coluna Preco_Produto para acelerar consultas com base no preço

# Consultar produtos com preço superior a 50.00 (isso será acelerado com o índice)
cursor.execute('''
SELECT * FROM Produtos WHERE Preco_Produto > 50;
''')  # Consulta todos os produtos com preço superior a 50.00

resultados = cursor.fetchall()  # Pega todos os resultados da consulta
print("Produtos com preço superior a 50:")
for resultado in resultados:  # Exibe cada produto encontrado
    print(resultado)

# Criar um índice composto (ID_Produto, Nome_Produto)
cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_id_nome_produto ON Produtos (ID_Produto, Nome_Produto);
''')  # Cria um índice composto (utilizando duas colunas: ID_Produto e Nome_Produto)

# Consultar produtos usando o índice composto (isso será mais rápido)
cursor.execute('''
SELECT * FROM Produtos WHERE ID_Produto = 3 AND Nome_Produto = 'Tênis';
''')  # Consulta o produto com ID 3 e nome 'Tênis' usando o índice composto

resultado = cursor.fetchone()  # Pega o primeiro (e único) resultado da consulta
print("\nProduto consultado com índice composto:")
print(resultado)  # Exibe o produto encontrado

# Fechar a conexão
conn.commit()  # Salva as mudanças no banco de dados
conn.close()  # Fecha a conexão com o banco de dados