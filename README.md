# Sistema Bancário

Este é um sistema bancário simples que gerencia clientes (pessoas físicas e jurídicas) com operações básicas de saque e extrato.

## Requisitos

- Python 3.8 ou superior
- SQLite3

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
.
├── database/
│   └── init_db.py       # Script de inicialização do banco de dados
├── models/
│   └── cliente.py       # Classes de modelo (PessoaFisica e PessoaJuridica)
├── controllers/
│   └── cliente_controller.py  # Controlador para operações com clientes
├── tests/
│   └── test_cliente_controller.py  # Testes unitários
├── main.py              # Programa principal
└── requirements.txt     # Dependências do projeto
```

## Funcionalidades

- Criação de clientes (pessoas físicas e jurídicas)
- Listagem de clientes
- Operações de saque
- Geração de extrato

### Regras de Negócio

- Pessoas físicas têm limite de saque menor que pessoas jurídicas
- O saldo não pode ficar negativo após um saque

## Executando o Sistema

1. Inicialize o banco de dados:
```bash
python database/init_db.py
```

2. Execute o programa principal:
```bash
python main.py
```

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
6. 
