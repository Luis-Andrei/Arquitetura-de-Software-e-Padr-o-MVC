import sys
import sqlite3
from typing import Optional
from controllers.cliente_controller import ClienteController
from models.cliente import PessoaFisica, PessoaJuridica

class CLI:
    def __init__(self):
        self.conn = sqlite3.connect('database/banco.db')
        self.controller = ClienteController(self.conn)

    def menu_principal(self):
        while True:
            print("\n=== Sistema Bancário ===")
            print("1. Gerenciar Pessoas Físicas")
            print("2. Gerenciar Pessoas Jurídicas")
            print("3. Realizar Transferência")
            print("0. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.menu_pessoa_fisica()
            elif opcao == "2":
                self.menu_pessoa_juridica()
            elif opcao == "3":
                self.menu_transferencia()
            elif opcao == "0":
                print("Saindo do sistema...")
                self.conn.close()
                sys.exit(0)
            else:
                print("Opção inválida!")

    def menu_pessoa_fisica(self):
        while True:
            print("\n=== Gerenciamento de Pessoas Físicas ===")
            print("1. Criar Pessoa Física")
            print("2. Listar Pessoas Físicas")
            print("3. Buscar Pessoa Física")
            print("4. Realizar Depósito")
            print("5. Realizar Saque")
            print("6. Ver Extrato")
            print("7. Ver Histórico de Transações")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.criar_pessoa_fisica()
            elif opcao == "2":
                self.listar_pessoas_fisicas()
            elif opcao == "3":
                self.buscar_pessoa_fisica()
            elif opcao == "4":
                self.realizar_deposito("PessoaFisica")
            elif opcao == "5":
                self.realizar_saque("PessoaFisica")
            elif opcao == "6":
                self.ver_extrato("PessoaFisica")
            elif opcao == "7":
                self.ver_historico("PessoaFisica")
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def menu_pessoa_juridica(self):
        while True:
            print("\n=== Gerenciamento de Pessoas Jurídicas ===")
            print("1. Criar Pessoa Jurídica")
            print("2. Listar Pessoas Jurídicas")
            print("3. Buscar Pessoa Jurídica")
            print("4. Realizar Depósito")
            print("5. Realizar Saque")
            print("6. Ver Extrato")
            print("7. Ver Histórico de Transações")
            print("0. Voltar")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.criar_pessoa_juridica()
            elif opcao == "2":
                self.listar_pessoas_juridicas()
            elif opcao == "3":
                self.buscar_pessoa_juridica()
            elif opcao == "4":
                self.realizar_deposito("PessoaJuridica")
            elif opcao == "5":
                self.realizar_saque("PessoaJuridica")
            elif opcao == "6":
                self.ver_extrato("PessoaJuridica")
            elif opcao == "7":
                self.ver_historico("PessoaJuridica")
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    def menu_transferencia(self):
        print("\n=== Realizar Transferência ===")
        
        print("\nTipo do Cliente de Origem:")
        print("1. Pessoa Física")
        print("2. Pessoa Jurídica")
        tipo_origem = input("Escolha uma opção: ")
        
        if tipo_origem not in ["1", "2"]:
            print("Opção inválida!")
            return
        
        id_origem = input("ID do Cliente de Origem: ")
        
        print("\nTipo do Cliente de Destino:")
        print("1. Pessoa Física")
        print("2. Pessoa Jurídica")
        tipo_destino = input("Escolha uma opção: ")
        
        if tipo_destino not in ["1", "2"]:
            print("Opção inválida!")
            return
        
        id_destino = input("ID do Cliente de Destino: ")
        valor = float(input("Valor da Transferência: "))
        
        tipo_origem = "PessoaFisica" if tipo_origem == "1" else "PessoaJuridica"
        tipo_destino = "PessoaFisica" if tipo_destino == "1" else "PessoaJuridica"
        
        try:
            if self.controller.transferir(id_origem, id_destino, valor, tipo_origem, tipo_destino):
                print("Transferência realizada com sucesso!")
            else:
                print("Não foi possível realizar a transferência.")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def criar_pessoa_fisica(self):
        print("\n=== Criar Pessoa Física ===")
        renda_mensal = float(input("Renda Mensal: "))
        idade = int(input("Idade: "))
        nome_completo = input("Nome Completo: ")
        celular = input("Celular: ")
        email = input("Email: ")
        categoria = input("Categoria: ")
        saldo = float(input("Saldo Inicial: "))
        
        try:
            self.controller.criar_pessoa_fisica(
                renda_mensal=renda_mensal,
                idade=idade,
                nome_completo=nome_completo,
                celular=celular,
                email=email,
                categoria=categoria,
                saldo=saldo
            )
            print("Pessoa física criada com sucesso!")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def criar_pessoa_juridica(self):
        print("\n=== Criar Pessoa Jurídica ===")
        faturamento = float(input("Faturamento: "))
        idade = int(input("Idade: "))
        nome_fantasia = input("Nome Fantasia: ")
        celular = input("Celular: ")
        email_corporativo = input("Email Corporativo: ")
        categoria = input("Categoria: ")
        saldo = float(input("Saldo Inicial: "))
        
        try:
            self.controller.criar_pessoa_juridica(
                faturamento=faturamento,
                idade=idade,
                nome_fantasia=nome_fantasia,
                celular=celular,
                email_corporativo=email_corporativo,
                categoria=categoria,
                saldo=saldo
            )
            print("Pessoa jurídica criada com sucesso!")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def listar_pessoas_fisicas(self):
        print("\n=== Lista de Pessoas Físicas ===")
        clientes = self.controller.listar_pessoas_fisicas()
        for cliente in clientes:
            print(f"\nID: {cliente['id']}")
            print(f"Nome: {cliente['nome_completo']}")
            print(f"Email: {cliente['email']}")
            print(f"Saldo: R${cliente['saldo']:.2f}")

    def listar_pessoas_juridicas(self):
        print("\n=== Lista de Pessoas Jurídicas ===")
        clientes = self.controller.listar_pessoas_juridicas()
        for cliente in clientes:
            print(f"\nID: {cliente['id']}")
            print(f"Empresa: {cliente['nome_fantasia']}")
            print(f"Email: {cliente['email_corporativo']}")
            print(f"Saldo: R${cliente['saldo']:.2f}")

    def buscar_pessoa_fisica(self):
        id_cliente = input("\nID da Pessoa Física: ")
        cliente = self.controller.buscar_pessoa_fisica(id_cliente)
        
        if cliente:
            dados = cliente.extrato()
            print(f"\nNome: {dados['nome_completo']}")
            print(f"Email: {dados['email']}")
            print(f"Saldo: R${dados['saldo']:.2f}")
        else:
            print("Pessoa física não encontrada!")

    def buscar_pessoa_juridica(self):
        id_cliente = input("\nID da Pessoa Jurídica: ")
        cliente = self.controller.buscar_pessoa_juridica(id_cliente)
        
        if cliente:
            dados = cliente.extrato()
            print(f"\nEmpresa: {dados['nome_fantasia']}")
            print(f"Email: {dados['email_corporativo']}")
            print(f"Saldo: R${dados['saldo']:.2f}")
        else:
            print("Pessoa jurídica não encontrada!")

    def realizar_deposito(self, tipo_cliente: str):
        id_cliente = input(f"\nID do Cliente ({tipo_cliente}): ")
        valor = float(input("Valor do Depósito: "))
        
        try:
            if tipo_cliente == "PessoaFisica":
                cliente = self.controller.buscar_pessoa_fisica(id_cliente)
            else:
                cliente = self.controller.buscar_pessoa_juridica(id_cliente)
            
            if cliente:
                cliente.depositar(valor)
                print("Depósito realizado com sucesso!")
            else:
                print("Cliente não encontrado!")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def realizar_saque(self, tipo_cliente: str):
        id_cliente = input(f"\nID do Cliente ({tipo_cliente}): ")
        valor = float(input("Valor do Saque: "))
        
        try:
            if tipo_cliente == "PessoaFisica":
                cliente = self.controller.buscar_pessoa_fisica(id_cliente)
            else:
                cliente = self.controller.buscar_pessoa_juridica(id_cliente)
            
            if cliente:
                if cliente.sacar(valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Não foi possível realizar o saque.")
            else:
                print("Cliente não encontrado!")
        except ValueError as e:
            print(f"Erro: {str(e)}")

    def ver_extrato(self, tipo_cliente: str):
        id_cliente = input(f"\nID do Cliente ({tipo_cliente}): ")
        
        if tipo_cliente == "PessoaFisica":
            cliente = self.controller.buscar_pessoa_fisica(id_cliente)
        else:
            cliente = self.controller.buscar_pessoa_juridica(id_cliente)
        
        if cliente:
            dados = cliente.extrato()
            print("\n=== Extrato ===")
            if tipo_cliente == "PessoaFisica":
                print(f"Nome: {dados['nome_completo']}")
                print(f"Email: {dados['email']}")
            else:
                print(f"Empresa: {dados['nome_fantasia']}")
                print(f"Email: {dados['email_corporativo']}")
            print(f"Saldo: R${dados['saldo']:.2f}")
        else:
            print("Cliente não encontrado!")

    def ver_historico(self, tipo_cliente: str):
        id_cliente = input(f"\nID do Cliente ({tipo_cliente}): ")
        
        if tipo_cliente == "PessoaFisica":
            cliente = self.controller.buscar_pessoa_fisica(id_cliente)
        else:
            cliente = self.controller.buscar_pessoa_juridica(id_cliente)
        
        if cliente:
            historico = cliente.historico_transacoes()
            print("\n=== Histórico de Transações ===")
            for transacao in historico:
                print(f"\nTipo: {transacao['tipo']}")
                print(f"Valor: R${transacao['valor']:.2f}")
                print(f"Data: {transacao['data']}")
                if transacao['descricao']:
                    print(f"Descrição: {transacao['descricao']}")
        else:
            print("Cliente não encontrado!")

def main():
    cli = CLI()
    cli.menu_principal()

if __name__ == '__main__':
    main() 