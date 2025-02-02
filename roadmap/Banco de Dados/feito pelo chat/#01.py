import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Criando e conectando ao banco de dados SQLite
# O banco será criado automaticamente se não existir
conn = sqlite3.connect('meu_banco_de_dados.db')  # Conecta-se ao banco de dados (ou cria um novo)
cursor = conn.cursor()  # Cria um cursor para executar comandos SQL

# Criando a tabela de clientes, se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  # Identificador único para cada cliente
        nome TEXT NOT NULL,  # Nome do cliente
        email TEXT NOT NULL  # E-mail do cliente
    )
''')

# Inserindo dados na tabela de clientes
# Utiliza o método executemany para inserir múltiplos registros ao mesmo tempo
cursor.executemany('''
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
''', [
    ('João Silva', 'joao.silva@email.com'),
    ('Maria Oliveira', 'maria.oliveira@email.com'),
    ('Carlos Souza', 'carlos.souza@email.com')
])

# Consultando dados da tabela para exibir os clientes inseridos
print("Clientes inseridos:")
cursor.execute('SELECT * FROM clientes')  # Comando SELECT para buscar todos os clientes
clientes = cursor.fetchall()  # Obtém todos os resultados da consulta
for cliente in clientes:
    print(cliente)  # Exibe cada cliente encontrado

# Atualizando o email de João Silva
cursor.execute('''
    UPDATE clientes
    SET email = ?  # Alterando o e-mail do cliente
    WHERE nome = ?  # Condição para buscar o cliente com nome 'João Silva'
''', ('joao.novoemail@email.com', 'João Silva'))

# Consultando novamente após a atualização
print("\nApós atualização do email de João Silva:")
cursor.execute('SELECT * FROM clientes')
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)  # Exibe os dados atualizados

# Deletando o cliente Carlos Souza
cursor.execute('''
    DELETE FROM clientes
    WHERE nome = ?  # Condição para excluir o cliente com nome 'Carlos Souza'
''', ('Carlos Souza',))

# Consultando novamente após a exclusão
print("\nApós exclusão de Carlos Souza:")
cursor.execute('SELECT * FROM clientes')
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)  # Exibe os dados após a exclusão de Carlos Souza

# Consultando clientes cujo nome começa com 'Maria'
print("\nClientes cujo nome começa com 'Maria':")
cursor.execute('''
    SELECT * FROM clientes
    WHERE nome LIKE 'Maria%'  # Filtra os clientes cujo nome começa com 'Maria'
''')
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)  # Exibe os clientes filtrados

# Verificando o tamanho do banco de dados (tamanho do arquivo)
import os  # Importa o módulo os para manipulação de arquivos
print(f"\nTamanho do banco de dados: {os.path.getsize('meu_banco_de_dados.db')} bytes")  # Exibe o tamanho do banco de dados em bytes

# Remover a tabela de clientes (opcional)
cursor.execute('DROP TABLE IF EXISTS clientes')  # Exclui a tabela clientes, caso exista

# Commit e fechar a conexão
conn.commit()  # Aplica todas as mudanças feitas no banco de dados
conn.close()  # Fecha a conexão com o banco de dados