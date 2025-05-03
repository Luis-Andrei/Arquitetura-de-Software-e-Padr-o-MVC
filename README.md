# Sistema Bancário

Um sistema bancário simples implementado em Python, com suporte a pessoas físicas e jurídicas, operações de depósito e saque, transferências entre contas e histórico de transações.

## Funcionalidades

- Gerenciamento de clientes (pessoas físicas e jurídicas)
- Operações de depósito e saque
- Transferências entre contas
- Histórico de transações
- Interface de linha de comando (CLI)

## Requisitos

- Python 3.8 ou superior
- SQLite3

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-bancario.git
cd sistema-bancario
```

2. Crie um ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências e configure o pre-commit:
```bash
make install
```

## Executando o Sistema

1. Inicialize o banco de dados:
```bash
python database/init_db.py
```

2. Execute o sistema:
```bash
python main.py
```

## Estrutura do Projeto

```
sistema-bancario/
├── database/
│   └── init_db.py
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── cliente_controller.py
│   └── models/
│       ├── __init__.py
│       └── cliente.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_cliente_controller.py
├── main.py
├── Makefile
├── requirements.txt
├── setup.py
├── pyproject.toml
├── .pre-commit-config.yaml
├── .flake8
├── .isort.cfg
├── mypy.ini
└── README.md
```

## Comandos Úteis

- `make install`: Instala as dependências e configura o pre-commit
- `make test`: Executa os testes com cobertura
- `make lint`: Executa as verificações de código (flake8 e mypy)
- `make format`: Formata o código (black e isort)
- `make clean`: Remove arquivos temporários e caches

## Ferramentas de Desenvolvimento

O projeto utiliza as seguintes ferramentas para garantir a qualidade do código:

- **pytest**: Framework de testes
- **black**: Formatador de código
- **isort**: Ordenador de imports
- **flake8**: Linter
- **mypy**: Verificador de tipos
- **pre-commit**: Hooks de pré-commit

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 