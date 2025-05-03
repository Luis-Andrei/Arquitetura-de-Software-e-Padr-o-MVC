import sqlite3
import os

def init_db():
    # Criar diretório database se não existir
    if not os.path.exists('database'):
        os.makedirs('database')
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('database/banco.db')
    cursor = conn.cursor()

    # Limpar tabelas existentes
    cursor.execute('DROP TABLE IF EXISTS transacao')
    cursor.execute('DROP TABLE IF EXISTS pessoa_fisica')
    cursor.execute('DROP TABLE IF EXISTS pessoa_juridica')

    # Criar tabela pessoa_fisica
    cursor.execute('''
    CREATE TABLE pessoa_fisica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        renda_mensal REAL,
        idade INTEGER,
        nome_completo TEXT,
        celular TEXT,
        email TEXT,
        categoria TEXT,
        saldo REAL
    )
    ''')

    # Criar tabela pessoa_juridica
    cursor.execute('''
    CREATE TABLE pessoa_juridica (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        faturamento REAL,
        idade INTEGER,
        nome_fantasia TEXT,
        celular TEXT,
        email_corporativo TEXT,
        categoria TEXT,
        saldo REAL
    )
    ''')

    # Criar tabela transacao
    cursor.execute('''
    CREATE TABLE transacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,
        valor REAL NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        cliente_id INTEGER NOT NULL,
        cliente_tipo TEXT NOT NULL,
        descricao TEXT
    )
    ''')

    # Inserir dados iniciais para pessoa_fisica
    cursor.executemany('''
    INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', [
        (5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00),
        (4000.00, 45, 'Maria Oliveira', '7777-6666', 'maria@example.com', 'Categoria B', 15000.00),
        (6000.00, 28, 'Pedro Santos', '5555-4444', 'pedro@example.com', 'Categoria C', 8000.00)
    ])

    # Inserir dados iniciais para pessoa_juridica
    cursor.executemany('''
    INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', [
        (100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00),
        (80000.00, 5, 'Empresa ABC', '3333-4444', 'contato@abc.com', 'Categoria B', 70000.00),
        (120000.00, 8, 'Empresa 123', '5555-6666', 'contato@123.com', 'Categoria C', 90000.00)
    ])

    # Commit e fechar conexão
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db() 