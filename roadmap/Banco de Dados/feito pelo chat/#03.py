import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('loja_normalizada.db')  # Conecta ao banco de dados, criando-o caso não exista
cursor = conn.cursor()  # Cria um cursor para executar comandos SQL

# Criar tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    ID_Cliente INTEGER PRIMARY KEY,  # Identificador único para cada cliente
    Nome_Cliente TEXT,               # Nome do cliente
    Endereco_Cliente TEXT            # Endereço do cliente
)
''')

# Criar tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos (
    ID_Produto INTEGER PRIMARY KEY,  # Identificador único para cada produto
    Produto TEXT,                    # Nome do produto
    Preco_Unitario DECIMAL(10, 2)    # Preço unitário do produto
)
''')

# Criar tabela de pedidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos (
    ID_Pedido INTEGER PRIMARY KEY,   # Identificador único para cada pedido
    ID_Cliente INTEGER,               # Chave estrangeira referenciando o cliente
    Data_Pedido DATE,                 # Data do pedido
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)  # Relacionamento com a tabela Clientes
)
''')

# Criar tabela de pedidos_produtos (relacionamento N:M entre Pedidos e Produtos)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos_Produtos (
    ID_Pedido INTEGER,                # Chave estrangeira referenciando a tabela Pedidos
    ID_Produto INTEGER,               # Chave estrangeira referenciando a tabela Produtos
    Quantidade INTEGER,               # Quantidade do produto no pedido
    PRIMARY KEY (ID_Pedido, ID_Produto),  # Chave primária composta (relacionamento muitos-para-muitos)
    FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),  # Relacionamento com Pedidos
    FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)  # Relacionamento com Produtos
)
''')

# Inserir dados na tabela de clientes
clientes = [
    (1, 'João Silva', 'Rua A, 123'),  # Dados de exemplo para a tabela Clientes
    (2, 'Maria Oliveira', 'Rua B, 456')
]
cursor.executemany('''
INSERT INTO Clientes (ID_Cliente, Nome_Cliente, Endereco_Cliente)
VALUES (?, ?, ?)
''', clientes)  # Inserir múltiplos registros na tabela Clientes

# Inserir dados na tabela de produtos
produtos = [
    (1, 'Camiseta', 50.00),  # Dados de exemplo para a tabela Produtos
    (2, 'Boné', 30.00),
    (3, 'Tênis', 200.00)
]
cursor.executemany('''
INSERT INTO Produtos (ID_Produto, Produto, Preco_Unitario)
VALUES (?, ?, ?)
''', produtos)  # Inserir múltiplos registros na tabela Produtos

# Inserir dados na tabela de pedidos
pedidos = [
    (1, 1, '2025-01-15'),  # Dados de exemplo para a tabela Pedidos
    (2, 2, '2025-01-16')
]
cursor.executemany('''
INSERT INTO Pedidos (ID_Pedido, ID_Cliente, Data_Pedido)
VALUES (?, ?, ?)
''', pedidos)  # Inserir múltiplos registros na tabela Pedidos

# Inserir dados na tabela de pedidos_produtos
pedidos_produtos = [
    (1, 1, 2),  # Pedido 1 tem 2 camisetas
    (1, 2, 1),  # Pedido 1 tem 1 boné
    (2, 1, 3)   # Pedido 2 tem 3 camisetas
]
cursor.executemany('''
INSERT INTO Pedidos_Produtos (ID_Pedido, ID_Produto, Quantidade)
VALUES (?, ?, ?)
''', pedidos_produtos)  # Inserir múltiplos registros na tabela Pedidos_Produtos

# Salvar (commit) as mudanças no banco de dados
conn.commit()

# Consultar e exibir os dados normalizados

# Consultar dados da tabela Clientes
cursor.execute('SELECT * FROM Clientes')
clientes_db = cursor.fetchall()  # Busca todos os registros da tabela Clientes
print("Clientes:")
for cliente in clientes_db:
    print(cliente)  # Exibe cada cliente retornado na consulta

# Consultar dados da tabela Produtos
cursor.execute('SELECT * FROM Produtos')
produtos_db = cursor.fetchall()  # Busca todos os registros da tabela Produtos
print("\nProdutos:")
for produto in produtos_db:
    print(produto)  # Exibe cada produto retornado na consulta

# Consultar dados da tabela Pedidos
cursor.execute('SELECT * FROM Pedidos')
pedidos_db = cursor.fetchall()  # Busca todos os registros da tabela Pedidos
print("\nPedidos:")
for pedido in pedidos_db:
    print(pedido)  # Exibe cada pedido retornado na consulta

# Consultar dados da tabela Pedidos_Produtos (relacionamento N:M)
cursor.execute('SELECT * FROM Pedidos_Produtos')
pedidos_produtos_db = cursor.fetchall()  # Busca todos os registros da tabela Pedidos_Produtos
print("\nPedidos_Produtos:")
for pp in pedidos_produtos_db:
    print(pp)  # Exibe cada item retornado na consulta

# Fechar a conexão com o banco de dados
conn.close()  # Fecha a conexão ao banco de dados para liberar recursos