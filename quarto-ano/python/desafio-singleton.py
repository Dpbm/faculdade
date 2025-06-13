from abc import ABC, abstractmethod
from enum import Enum

class Bancos(Enum):
    MySQL="mysql"
    PostgreSQL="postgres"
    SQLServer="sqlserver"


class DB(ABC):
    @abstractmethod
    def connectar(self, string_conexao):
        pass

class MySQL(DB):
    def connectar(self, string_conexao):
        print(f"Conectando MySQL: {string_conexao}")

class PostgreSQL(DB):
    def connectar(self, string_conexao):
        print(f"Conectando PostgreSQL: {string_conexao}")

class SQLServer(DB):
    def connectar(self, string_conexao):
        print(f"Conectando SQL Server: {string_conexao}")


class DBFactory:
    def criar_banco(self, banco):
        print(vars(Bancos))

DBFactory().criar_banco("postgre")