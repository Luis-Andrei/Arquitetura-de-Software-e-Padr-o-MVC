import sqlite3
import os

def init_db():
    # Criar diretório database se não existir
    os.makedirs('database', exist_ok=True)
    
    # Conectar ao banco de dados
    conn = sqlite3.connect('database/banco.db')
    
    # Criar tabelas
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pessoa_fisica (
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
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pessoa_juridica (
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
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS transacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT,
            valor REAL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            cliente_id INTEGER,
            cliente_tipo TEXT,
            descricao TEXT
        )
    ''')
    
    # Inserir dados iniciais
    conn.execute('''
        INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        VALUES (5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00)
    ''')
    
    conn.execute('''
        INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        VALUES (6000.00, 28, 'Maria Oliveira', '8888-7777', 'maria@example.com', 'Categoria B', 15000.00)
    ''')
    
    conn.execute('''
        INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        VALUES (4000.00, 42, 'Pedro Santos', '7777-6666', 'pedro@example.com', 'Categoria C', 8000.00)
    ''')
    
    conn.execute('''
        INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        VALUES (100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00)
    ''')
    
    conn.execute('''
        INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        VALUES (150000.00, 15, 'Empresa ABC', '2222-3333', 'contato@abc.com', 'Categoria B', 75000.00)
    ''')
    
    conn.execute('''
        INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        VALUES (80000.00, 8, 'Empresa 123', '3333-4444', 'contato@123.com', 'Categoria C', 40000.00)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db() 