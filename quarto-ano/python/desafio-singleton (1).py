from abc import ABC, abstractmethod
from enum import Enum

class Bancos(Enum):
    MySQL="mysql"
    PostgreSQL="postgres"
    SQLServer="sqlserver"


class DB(ABC):
    def __init__(self):
        self._string_conexao = ""

    def set_string_conexao(self, string_conexao:str):
        self._string_conexao = string_conexao

    @abstractmethod
    def conectar(self):
        pass

class MySQL(DB):
    def __init__(self):
        super().__init__()

    def conectar(self):
        print(f"Conectando MySQL: {self._string_conexao}")

class PostgreSQL(DB):
    def __init__(self):
        super().__init__()

    def conectar(self):
        print(f"Conectando PostgreSQL: {self._string_conexao}")

class SQLServer(DB):
    def __init__(self):
        super().__init__()

    def conectar(self):
        print(f"Conectando SQL Server: {self._string_conexao}")

class DBFactory:
    @staticmethod
    def create_db(db:Bancos) -> DB:
        if(db == Bancos.MySQL):
            return MySQL()
        elif(db == Bancos.PostgreSQL):
            return PostgreSQL()
        elif (db == Bancos.SQLServer):
            return SQLServer()
        else:
            raise ValueError("Banco invalido")


class ConnectionString:
    @staticmethod
    @abstractmethod
    def get_string(host:str, user:str, password:str, database:str) -> str:
        pass

class MySQLString:
    @staticmethod
    def get_string(host:str, user:str, password:str, database:str) -> str:
        return f"server={host};uid={user};pwd={password};database={database}"


class PostgreSQLString:
    @staticmethod
    def get_string(host:str, user:str, password:str, database:str) -> str:
        return f"postgres://{user}:{password}@{host}:5432/{database}"
    
class SQLServerString:
    @staticmethod
    def get_string(host:str, user:str, password:str, database:str) -> str:
        return f"Server={host};Database={database};User Id={user};Password={password};"

class ConnectionStringFactory:
    @staticmethod
    def get_connection_string(db:str) -> ConnectionString:
        if(db == Bancos.MySQL):
            return MySQLString()
        elif(db == Bancos.PostgreSQL):
            return PostgreSQLString()
        elif (db == Bancos.SQLServer):
            return SQLServerString()
        else:
            raise ValueError("Banco invalido para a string de conexao")

class DBConnectionFactory:
    __instances = {}


    @classmethod
    def get_conexao(cls,db:str, host:str, user:str, password:str, database:str) -> DB:

        if cls.__instances.get(db) is not None:
            return cls.__instances[db]

        banco = DBFactory.create_db(db)
        string = ConnectionStringFactory.get_connection_string(db).get_string(host, user, password, database)
        banco.set_string_conexao(string)
        cls.__instances[db] = banco
        return banco

db1 = DBConnectionFactory.get_conexao(Bancos.MySQL, "localhost", "test", "test", "test")
db2 = DBConnectionFactory.get_conexao(Bancos.MySQL, "localhost", "test2", "test2", "test2")
db3 = DBConnectionFactory.get_conexao(Bancos.PostgreSQL, "localhost", "test3", "test3", "test3")
db4 = DBConnectionFactory.get_conexao(Bancos.PostgreSQL, "localhost", "test4", "test4", "test4")

print("Testing DB instance 1")
db1.conectar()
print("Testing DB instance 2")
db2.conectar()
print("Testing DB instance 3")
db3.conectar()
print("Testing DB instance 4")
db4.conectar()


