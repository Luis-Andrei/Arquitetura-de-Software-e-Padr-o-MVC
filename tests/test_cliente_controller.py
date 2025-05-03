import pytest
import sqlite3
import os
from controllers.cliente_controller import ClienteController
from models.cliente import PessoaFisica, PessoaJuridica

@pytest.fixture(scope="function")
def setup_database():
    # Criar banco de dados temporário para testes
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Criar tabelas
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

    cursor.execute('''
        CREATE TABLE transacao (
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
    cursor.execute('''
        INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        VALUES (5000.00, 35, 'João da Silva', '9999-8888', 'joao@example.com', 'Categoria A', 10000.00)
    ''')

    cursor.execute('''
        INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        VALUES (6000.00, 28, 'Maria Oliveira', '8888-7777', 'maria@example.com', 'Categoria B', 15000.00)
    ''')

    cursor.execute('''
        INSERT INTO pessoa_fisica (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        VALUES (4000.00, 42, 'Pedro Santos', '7777-6666', 'pedro@example.com', 'Categoria C', 8000.00)
    ''')

    cursor.execute('''
        INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        VALUES (100000.00, 10, 'Empresa XYZ', '1111-2222', 'contato@empresa.com', 'Categoria A', 50000.00)
    ''')

    cursor.execute('''
        INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        VALUES (150000.00, 15, 'Empresa ABC', '2222-3333', 'contato@abc.com', 'Categoria B', 75000.00)
    ''')

    cursor.execute('''
        INSERT INTO pessoa_juridica (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        VALUES (80000.00, 8, 'Empresa 123', '3333-4444', 'contato@123.com', 'Categoria C', 40000.00)
    ''')

    conn.commit()
    yield conn
    conn.close()

def test_criar_pessoa_fisica(setup_database):
    controller = ClienteController(setup_database)
    controller.criar_pessoa_fisica(
        renda_mensal=5000.00,
        idade=35,
        nome_completo="João da Silva",
        celular="9999-8888",
        email="joao@example.com",
        categoria="Categoria A",
        saldo=10000.00
    )
    clientes = controller.listar_pessoas_fisicas()
    assert len(clientes) == 4  # 3 iniciais + 1 novo
    assert clientes[-1]['nome_completo'] == "João da Silva"

def test_criar_pessoa_juridica(setup_database):
    controller = ClienteController(setup_database)
    controller.criar_pessoa_juridica(
        faturamento=100000.00,
        idade=10,
        nome_fantasia="Empresa XYZ",
        celular="1111-2222",
        email_corporativo="contato@empresa.com",
        categoria="Categoria A",
        saldo=50000.00
    )
    clientes = controller.listar_pessoas_juridicas()
    assert len(clientes) == 4  # 3 iniciais + 1 novo
    assert clientes[-1]['nome_fantasia'] == "Empresa XYZ"

def test_listar_pessoas_fisicas(setup_database):
    controller = ClienteController(setup_database)
    clientes = controller.listar_pessoas_fisicas()
    assert len(clientes) == 3
    assert clientes[0]['nome_completo'] == "João da Silva"
    assert clientes[1]['nome_completo'] == "Maria Oliveira"
    assert clientes[2]['nome_completo'] == "Pedro Santos"

def test_listar_pessoas_juridicas(setup_database):
    controller = ClienteController(setup_database)
    clientes = controller.listar_pessoas_juridicas()
    assert len(clientes) == 3
    assert clientes[0]['nome_fantasia'] == "Empresa XYZ"
    assert clientes[1]['nome_fantasia'] == "Empresa ABC"
    assert clientes[2]['nome_fantasia'] == "Empresa 123"

def test_buscar_pessoa_fisica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_fisica(1)
    assert cliente is not None
    assert cliente.extrato()['nome_completo'] == "João da Silva"

def test_buscar_pessoa_juridica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_juridica(1)
    assert cliente is not None
    assert cliente.extrato()['nome_fantasia'] == "Empresa XYZ"

def test_saque_pessoa_fisica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_fisica(1)
    saldo_inicial = cliente.extrato()['saldo']
    cliente.sacar(500.00)
    assert cliente.extrato()['saldo'] == saldo_inicial - 500.00

def test_saque_pessoa_juridica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_juridica(1)
    saldo_inicial = cliente.extrato()['saldo']
    cliente.sacar(2000.00)
    assert cliente.extrato()['saldo'] == saldo_inicial - 2000.00

def test_limite_saque_pessoa_fisica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_fisica(1)
    with pytest.raises(ValueError):
        cliente.sacar(1500.00)  # Limite é 1000.00

def test_limite_saque_pessoa_juridica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_juridica(1)
    with pytest.raises(ValueError):
        cliente.sacar(6000.00)  # Limite é 5000.00

def test_deposito_pessoa_fisica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_fisica(1)
    saldo_inicial = cliente.extrato()['saldo']
    cliente.depositar(1000.00)
    assert cliente.extrato()['saldo'] == saldo_inicial + 1000.00

def test_deposito_pessoa_juridica(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_juridica(1)
    saldo_inicial = cliente.extrato()['saldo']
    cliente.depositar(5000.00)
    assert cliente.extrato()['saldo'] == saldo_inicial + 5000.00

def test_deposito_valor_invalido(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_fisica(1)
    with pytest.raises(ValueError):
        cliente.depositar(-100.00)

def test_historico_transacoes(setup_database):
    controller = ClienteController(setup_database)
    cliente = controller.buscar_pessoa_fisica(1)
    
    # Realizar algumas operações
    cliente.depositar(1000.00)
    cliente.sacar(500.00)
    
    historico = cliente.historico_transacoes()
    assert len(historico) == 2
    assert historico[0]['tipo'] == 'SAQUE'
    assert historico[0]['valor'] == 500.00
    assert historico[1]['tipo'] == 'DEPOSITO'
    assert historico[1]['valor'] == 1000.00

def test_transferencia(setup_database):
    controller = ClienteController(setup_database)
    
    # Transferir de pessoa física para pessoa jurídica
    assert controller.transferir(1, 1, 1000.00, 'PessoaFisica', 'PessoaJuridica')
    
    # Verificar saldos
    pf = controller.buscar_pessoa_fisica(1)
    pj = controller.buscar_pessoa_juridica(1)
    
    assert pf.extrato()['saldo'] == 9000.00  # 10000 - 1000
    assert pj.extrato()['saldo'] == 51000.00  # 50000 + 1000

def test_transferencia_saldo_insuficiente(setup_database):
    controller = ClienteController(setup_database)
    with pytest.raises(ValueError):
        controller.transferir(1, 1, 20000.00, 'PessoaFisica', 'PessoaJuridica') 