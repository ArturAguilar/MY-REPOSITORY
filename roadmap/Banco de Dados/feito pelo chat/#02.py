import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('loja_online.db')  # Conecta ao banco de dados 'loja_online.db', ou cria um novo se não existir
cursor = conn.cursor()  # Cria um cursor para executar comandos SQL

# Criar a tabela 'Clientes'
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    ID_Cliente INTEGER PRIMARY KEY,  # Identificador único para cada cliente
    Nome VARCHAR(255),               # Nome do cliente
    Email VARCHAR(255),              # Email do cliente
    Telefone VARCHAR(20),            # Telefone do cliente
    Endereco TEXT                    # Endereço do cliente
)
''')

# Criar a tabela 'Produtos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produtos (
    ID_Produto INTEGER PRIMARY KEY,  # Identificador único para cada produto
    Nome VARCHAR(255),               # Nome do produto
    Preco DECIMAL(10, 2),            # Preço do produto
    Quantidade_em_estoque INTEGER   # Quantidade de produtos disponíveis em estoque
)
''')

# Criar a tabela 'Pedidos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos (
    ID_Pedido INTEGER PRIMARY KEY,   # Identificador único para cada pedido
    ID_Cliente INTEGER,               # Chave estrangeira que referencia a tabela Clientes
    Data_Pedido DATE,                 # Data do pedido
    Status VARCHAR(50),               # Status do pedido (exemplo: 'Em Processamento', 'Concluído')
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)  # Relacionamento com a tabela 'Clientes'
)
''')

# Criar a tabela 'Pagamentos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pagamentos (
    ID_Pagamento INTEGER PRIMARY KEY,  # Identificador único para cada pagamento
    ID_Pedido INTEGER,                 # Chave estrangeira que referencia a tabela Pedidos
    Valor DECIMAL(10, 2),              # Valor do pagamento
    Data_Pagamento DATE,               # Data do pagamento
    FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido)  # Relacionamento com a tabela 'Pedidos'
)
''')

# Criar a tabela 'Pedidos_Produtos' para relacionamento N:M
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pedidos_Produtos (
    ID_Pedido INTEGER,                # Chave estrangeira que referencia a tabela Pedidos
    ID_Produto INTEGER,               # Chave estrangeira que referencia a tabela Produtos
    Quantidade INTEGER,               # Quantidade do produto no pedido
    Preco DECIMAL(10, 2),             # Preço do produto no momento do pedido
    PRIMARY KEY (ID_Pedido, ID_Produto),  # Chave composta para garantir que um produto não seja duplicado no mesmo pedido
    FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),  # Relacionamento com a tabela 'Pedidos'
    FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)  # Relacionamento com a tabela 'Produtos'
)
''')

# Inserir dados na tabela 'Clientes'
clientes = [
    (1, 'João Silva', 'joao@email.com', '1234-5678', 'Rua A, 123'),
    (2, 'Maria Oliveira', 'maria@email.com', '2345-6789', 'Rua B, 456'),
    (3, 'Carlos Souza', 'carlos@email.com', '3456-7890', 'Rua C, 789')
]
cursor.executemany('''
INSERT INTO Clientes (ID_Cliente, Nome, Email, Telefone, Endereco)
VALUES (?, ?, ?, ?, ?)
''', clientes)  # Insere vários registros de clientes ao mesmo tempo

# Inserir dados na tabela 'Produtos'
produtos = [
    (1, 'Camiseta', 50.00, 100),
    (2, 'Tênis', 200.00, 50),
    (3, 'Boné', 30.00, 200)
]
cursor.executemany('''
INSERT INTO Produtos (ID_Produto, Nome, Preco, Quantidade_em_estoque)
VALUES (?, ?, ?, ?)
''', produtos)  # Insere vários produtos de uma vez

# Inserir dados na tabela 'Pedidos'
pedidos = [
    (1, 1, '2025-01-15', 'Concluído'),
    (2, 2, '2025-01-16', 'Em Processamento'),
    (3, 3, '2025-01-17', 'Concluído')
]
cursor.executemany('''
INSERT INTO Pedidos (ID_Pedido, ID_Cliente, Data_Pedido, Status)
VALUES (?, ?, ?, ?)
''', pedidos)  # Insere vários pedidos

# Inserir dados na tabela 'Pagamentos'
pagamentos = [
    (1, 1, 50.00, '2025-01-15'),
    (2, 2, 200.00, '2025-01-16'),
    (3, 3, 30.00, '2025-01-17')
]
cursor.executemany('''
INSERT INTO Pagamentos (ID_Pagamento, ID_Pedido, Valor, Data_Pagamento)
VALUES (?, ?, ?, ?)
''', pagamentos)  # Insere vários pagamentos

# Inserir dados na tabela 'Pedidos_Produtos'
pedidos_produtos = [
    (1, 1, 2, 50.00),  # Pedido 1 tem 2 camisetas
    (2, 2, 1, 200.00),  # Pedido 2 tem 1 tênis
    (3, 3, 3, 30.00)    # Pedido 3 tem 3 bonés
]
cursor.executemany('''
INSERT INTO Pedidos_Produtos (ID_Pedido, ID_Produto, Quantidade, Preco)
VALUES (?, ?, ?, ?)
''', pedidos_produtos)  # Insere a relação de pedidos e produtos

# Salvar (commit) as mudanças no banco de dados
conn.commit()

# Consultar e exibir os dados de clientes
cursor.execute('SELECT * FROM Clientes')
clientes_db = cursor.fetchall()  # Recupera todos os dados da tabela 'Clientes'
print("Clientes:")
for cliente in clientes_db:
    print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Telefone: {cliente[3]}, Endereço: {cliente[4]}")

# Consultar e exibir os dados de pedidos
cursor.execute('SELECT * FROM Pedidos')
pedidos_db = cursor.fetchall()  # Recupera todos os dados da tabela 'Pedidos'
print("\nPedidos:")
for pedido in pedidos_db:
    print(f"ID: {pedido[0]}, Cliente ID: {pedido[1]}, Data: {pedido[2]}, Status: {pedido[3]}")

# Consultar e exibir os dados de pagamentos
cursor.execute('SELECT * FROM Pagamentos')
pagamentos_db = cursor.fetchall()  # Recupera todos os dados da tabela 'Pagamentos'
print("\nPagamentos:")
for pagamento in pagamentos_db:
    print(f"ID: {pagamento[0]}, Pedido ID: {pagamento[1]}, Valor: {pagamento[2]:.2f}, Data: {pagamento[3]}")

# Consultar e exibir os produtos no pedido
cursor.execute('SELECT * FROM Pedidos_Produtos')
pedidos_produtos_db = cursor.fetchall()  # Recupera todos os dados da tabela 'Pedidos_Produtos'
print("\nProdutos no Pedido:")
for pp in pedidos_produtos_db:
    print(f"Pedido ID: {pp[0]}, Produto ID: {pp[1]}, Quantidade: {pp[2]}, Preço: {pp[3]:.2f}")

# Fechar a conexão com o banco de dados
conn.close()  # Fecha a conexão com o banco de dados