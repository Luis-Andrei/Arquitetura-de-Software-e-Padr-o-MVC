import sqlite3
from typing import List, Dict, Any
from models.cliente import PessoaFisica, PessoaJuridica

class ClienteController:
    def __init__(self, conn=None):
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

    def buscar_pessoa_fisica(self, id: int) -> PessoaFisica:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pessoa_fisica WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            return PessoaFisica(*row, conn=self.conn)
        return None

    def buscar_pessoa_juridica(self, id: int) -> PessoaJuridica:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM pessoa_juridica WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            return PessoaJuridica(*row, conn=self.conn)
        return None 