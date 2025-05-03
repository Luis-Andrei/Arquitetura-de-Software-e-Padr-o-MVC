import sqlite3
from typing import List, Dict, Any, Optional
from src.models.cliente import PessoaFisica, PessoaJuridica

class ClienteController:
    def __init__(self, conn: Optional[sqlite3.Connection] = None):
        self.conn = conn or sqlite3.connect('database/banco.db')

    def criar_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo: str,
                           celular: str, email: str, categoria: str, saldo: float = 0.0) -> bool:
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO pessoa_fisica 
                (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (renda_mensal, idade, nome_completo, celular, email, categoria, saldo))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar pessoa física: {e}")
            return False

    def criar_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia: str,
                            celular: str, email_corporativo: str, categoria: str, saldo: float = 0.0) -> bool:
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO pessoa_juridica 
                (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar pessoa jurídica: {e}")
            return False

    def listar_pessoas_fisicas(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pessoa_fisica')
        return [dict(zip([column[0] for column in cursor.description], row))
               for row in cursor.fetchall()]

    def listar_pessoas_juridicas(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pessoa_juridica')
        return [dict(zip([column[0] for column in cursor.description], row))
               for row in cursor.fetchall()]

    def buscar_pessoa_fisica(self, id: int) -> Optional[PessoaFisica]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pessoa_fisica WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            dados = dict(zip([column[0] for column in cursor.description], row))
            return PessoaFisica(
                id=dados['id'],
                renda_mensal=dados['renda_mensal'],
                idade=dados['idade'],
                nome_completo=dados['nome_completo'],
                celular=dados['celular'],
                email=dados['email'],
                categoria=dados['categoria'],
                saldo=dados['saldo'],
                conn=self.conn
            )
        return None

    def buscar_pessoa_juridica(self, id: int) -> Optional[PessoaJuridica]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pessoa_juridica WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            dados = dict(zip([column[0] for column in cursor.description], row))
            return PessoaJuridica(
                id=dados['id'],
                faturamento=dados['faturamento'],
                idade=dados['idade'],
                nome_fantasia=dados['nome_fantasia'],
                celular=dados['celular'],
                email_corporativo=dados['email_corporativo'],
                categoria=dados['categoria'],
                saldo=dados['saldo'],
                conn=self.conn
            )
        return None

    def transferir(self, origem_id: int, destino_id: int, valor: float,
                  origem_tipo: str = 'PessoaFisica', destino_tipo: str = 'PessoaFisica') -> bool:
        try:
            # Buscar clientes
            origem = (self.buscar_pessoa_fisica(origem_id) if origem_tipo == 'PessoaFisica'
                     else self.buscar_pessoa_juridica(origem_id))
            destino = (self.buscar_pessoa_fisica(destino_id) if destino_tipo == 'PessoaFisica'
                      else self.buscar_pessoa_juridica(destino_id))

            if not origem or not destino:
                raise ValueError("Cliente de origem ou destino não encontrado")

            # Realizar transferência
            origem.sacar(valor)
            destino.depositar(valor)

            # Registrar transações
            origem.registrar_transacao('TRANSFERENCIA_SAIDA', valor,
                                     f"Transferência para {destino_tipo} ID {destino_id}")
            destino.registrar_transacao('TRANSFERENCIA_ENTRADA', valor,
                                      f"Transferência de {origem_tipo} ID {origem_id}")

            return True
        except Exception as e:
            print(f"Erro ao transferir: {e}")
            return False 