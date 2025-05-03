# Sistema Bancário

Um sistema bancário simples implementado em Python, com suporte a pessoas físicas e jurídicas, operações de depósito e saque, transferências entre contas e histórico de transações.

## Funcionalidades

- Gerenciamento de clientes (pessoas físicas e jurídicas)
- Operações de depósito e saque
- Transferências entre contas
- Histórico de transações
- Interface de linha de comando (CLI)
- Geração de extrato

### Regras de Negócio

- Pessoas físicas têm limite de saque menor que pessoas jurídicas
- O saldo não pode ficar negativo após um saque

## Requisitos

- Python 3.8 ou superior
- SQLite3

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Luis-Andrei/Arquitetura-de-Software-e-Padr-o-MVC.git
cd Arquitetura-de-Software-e-Padr-o-MVC
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

## Estrutura do Projeto

```
.
├── database/
│   └── init_db.py       # Script de inicialização do banco de dados
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
├── main.py              # Programa principal
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

## Executando o Sistema

1. Inicialize o banco de dados:
```bash
python database/init_db.py
```

2. Execute o sistema:
```bash
python main.py
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

## Executando os Testes

Para executar os testes unitários:
```bash
pytest tests/
```

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
