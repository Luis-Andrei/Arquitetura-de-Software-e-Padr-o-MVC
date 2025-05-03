from abc import ABC, abstractmethod
import sqlite3
from typing import List, Dict, Any

class Cliente(ABC):
    def __init__(self, conn=None):
        self.conn = conn or sqlite3.connect('database/banco.db')

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def depositar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def extrato(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def transferir(self, destino: 'Cliente', valor: float) -> bool:
        pass

    def historico_transacoes(self) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM transacao 
            WHERE cliente_id = ? AND cliente_tipo = ?
            ORDER BY data DESC
        ''', (self.id, self.__class__.__name__))
        return [dict(zip([column[0] for column in cursor.description], row))
               for row in cursor.fetchall()]

class PessoaFisica(Cliente):
    def __init__(self, id: int = None, renda_mensal: float = 0, idade: int = 0,
                 nome_completo: str = "", celular: str = "", email: str = "",
                 categoria: str = "", saldo: float = 0, conn=None):
        super().__init__(conn)
        self.id = id
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo
        self.limite_saque = 1000.00  # Limite menor para pessoa física

    def sacar(self, valor: float) -> bool:
        if valor > self.limite_saque:
            raise ValueError(f"Valor excede o limite de saque de R$ {self.limite_saque}")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE pessoa_fisica 
                SET saldo = saldo - ? 
                WHERE id = ?
            ''', (valor, self.id))
            
            cursor.execute('''
                INSERT INTO transacao (tipo, valor, cliente_id, cliente_tipo, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', ('saque', valor, self.id, self.__class__.__name__, 'Saque em conta'))
            
            self.conn.commit()
            self.saldo -= valor
            return True
        except Exception as e:
            print(f"Erro ao sacar: {e}")
            return False

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE pessoa_fisica 
                SET saldo = saldo + ? 
                WHERE id = ?
            ''', (valor, self.id))
            
            cursor.execute('''
                INSERT INTO transacao (tipo, valor, cliente_id, cliente_tipo, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', ('deposito', valor, self.id, self.__class__.__name__, 'Depósito em conta'))
            
            self.conn.commit()
            self.saldo += valor
            return True
        except Exception as e:
            print(f"Erro ao depositar: {e}")
            return False

    def transferir(self, destino: Cliente, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        
        try:
            self.sacar(valor)
            destino.depositar(valor)
            return True
        except Exception as e:
            print(f"Erro na transferência: {e}")
            return False

    def extrato(self) -> Dict[str, Any]:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM pessoa_fisica WHERE id = ?
        ''', (self.id,))
        row = cursor.fetchone()
        if row:
            return dict(zip([column[0] for column in cursor.description], row))
        return {}

class PessoaJuridica(Cliente):
    def __init__(self, id: int = None, faturamento: float = 0, idade: int = 0,
                 nome_fantasia: str = "", celular: str = "", email_corporativo: str = "",
                 categoria: str = "", saldo: float = 0, conn=None):
        super().__init__(conn)
        self.id = id
        self.faturamento = faturamento
        self.idade = idade
        self.nome_fantasia = nome_fantasia
        self.celular = celular
        self.email_corporativo = email_corporativo
        self.categoria = categoria
        self.saldo = saldo
        self.limite_saque = 5000.00  # Limite maior para pessoa jurídica

    def sacar(self, valor: float) -> bool:
        if valor > self.limite_saque:
            raise ValueError(f"Valor excede o limite de saque de R$ {self.limite_saque}")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE pessoa_juridica 
                SET saldo = saldo - ? 
                WHERE id = ?
            ''', (valor, self.id))
            
            cursor.execute('''
                INSERT INTO transacao (tipo, valor, cliente_id, cliente_tipo, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', ('saque', valor, self.id, self.__class__.__name__, 'Saque em conta'))
            
            self.conn.commit()
            self.saldo -= valor
            return True
        except Exception as e:
            print(f"Erro ao sacar: {e}")
            return False

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE pessoa_juridica 
                SET saldo = saldo + ? 
                WHERE id = ?
            ''', (valor, self.id))
            
            cursor.execute('''
                INSERT INTO transacao (tipo, valor, cliente_id, cliente_tipo, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', ('deposito', valor, self.id, self.__class__.__name__, 'Depósito em conta'))
            
            self.conn.commit()
            self.saldo += valor
            return True
        except Exception as e:
            print(f"Erro ao depositar: {e}")
            return False

    def transferir(self, destino: Cliente, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        
        try:
            self.sacar(valor)
            destino.depositar(valor)
            return True
        except Exception as e:
            print(f"Erro na transferência: {e}")
            return False

    def extrato(self) -> Dict[str, Any]:
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM pessoa_juridica WHERE id = ?
        ''', (self.id,))
        row = cursor.fetchone()
        if row:
            return dict(zip([column[0] for column in cursor.description], row))
        return {} 