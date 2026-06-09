import sqlite3
from sqlite3 import Connection


def connect_db(db_name: str = "vendas8.db") -> Connection:
    """Cria uma conexão SQLite com suporte a chaves estrangeiras."""
    conn = sqlite3.connect(db_name)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
