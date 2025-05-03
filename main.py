from database.init_db import init_db
from src.cli import CLI

def main():
    # Inicializar banco de dados
    init_db()
    
    # Iniciar interface de linha de comando
    cli = CLI()
    cli.menu_principal()

if __name__ == '__main__':
    main() 