import sqlite3

def conectar():
    return sqlite3.connect("lanchonete.db")

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produtos (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pedidos (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        data_pedido TEXT NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ItensPedido (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
        FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
    )
    """)

    conexao.commit()
    conexao.close()

# Inserir cliente
def adicionar_cliente(nome, email, telefone):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Clientes (nome, email, telefone) VALUES (?, ?, ?)",
                   (nome, email, telefone))
    conexao.commit()
    conexao.close()

# Listar clientes
def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conexao.close()
    return clientes

