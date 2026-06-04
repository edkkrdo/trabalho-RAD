import sqlite3

conn = sqlite3.connect("vendas8.bd")
cursor = conn.cursor()

# Produto, Cliente, Região, Vendedor, Veiculo // Tabelas Independentes
# Nota_Fiscal, Item_Nota_Fiscal, Ponto_Estrategico, Utilizacao_Veiculo // Tabelas Dependentes

# nf = Nota Fiscal

# --
cursor.execute("""
CREATE TABLE Produto(
    cod_produto INTEGER PRIMARY KEY,
    nome_produto VARCHAR(100),
    indicador_produto BOOLEAN NOT NULL,
    preco_produto REAL NOT NULL
    )""")

# --
cursor.execute("""
CREATE TABLE Cliente(
    cod_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente VARCHAR(20) NOT NULL)""")

cursor.execute("""
CREATE TABLE Nota_Fiscal(
    num_nf INTEGER PRIMARY KEY,
    cod_cliente INTEGER NOT NULL,
    cod_vendedor INTEGER NOT NULL,

    FOREIGN KEY (cod_cliente)
    REFERENCES Cliente (cod_cliente),

    FOREIGN KEY (cod_vendedor)
    REFERENCES Vendedor (cod_vendedor)
    )""")

cursor.execute("""
CREATE TABLE Item_da_Nota_Fiscal(
    num_item_da_nf INTEGER PRIMARY KEY AUTOINCREMENT,
    num_nf INTEGER NOT NULL,
    cod_produto INTEGER NOT NULL,
    qnt_produto INTEGER NOT NULL,

    FOREIGN KEY (num_nf)
    REFERENCES Nota_Fiscal (num_nf),

    FOREIGN KEY (cod_produto)
    REFERENCES Produto (cod_produto)
    )""")

# --
cursor.execute("""
CREATE TABLE Regiao(
    cod_regiao CHAR(3) PRIMARY KEY,
    nome_regiao VARCHAR (30)
    )""")

# --
cursor.execute("""
CREATE TABLE Vendedor(
    cod_vendedor CHAR(5) PRIMARY KEY,
    nome_vendedor VARCHAR(50),
    cod_vendedor_regiao CHAR(3) NOT NULL
    )""")

cursor.execute("""
CREATE TABLE Ponto_Estrategico(
    cod_pt_estrategico INTEGER PRIMARY KEY,
    cod_regiao INTEGER NOT NULL,

    FOREIGN KEY (cod_regiao)
    REFERENCES Regiao (cod_regiao)
    )""")

# --
cursor.execute("""
CREATE TABLE Veiculo(
    cod_veiculo CHAR(4) PRIMARY KEY,
    num_placa_veiculo CHAR(7) NOT NULL
    )""")

cursor.execute("""
CREATE TABLE Utilizacao_Veiculo(
    cod_veiculo INTEGER NOT NULL,
    data_utilizacao_veiculo DATE NOT NULL,
    cod_vendedor INTEGER,

    FOREIGN KEY (cod_veiculo)
    REFERENCES Veiculo (cod_veiculo),

    FOREIGN KEY (cod_vendedor)
    REFERENCES Vendedor (cod_vendedor)
    )""")

# Inserindo dados
# lista de tuplas da tabela Clientes
clientes = [
    ('Lohhana Pinheiro',),
    ('Eleonor Maria',),
    ('Armando Mendonça',),
    ('Leticia Solano',)
]

cursor.executemany("""
INSERT INTO Cliente (nome_cliente)
VALUES (?)
""", clientes)

# lista de tuplas da tabela Produtos
produtos = [
    (1, 'Geladeira', 1, 3200.00),
    (2, 'Fogão', 1, 1200.00),
    (3, 'Micro-ondas', 0, 800.00),
    (4, 'Máquina de Lavar', 1, 2800.00),
    (5, 'Aspirador de Pó', 1, 450.00),
    (6, 'Liquidificador', 0, 220.00),
    (7, 'Ventilador', 1, 180.00),
    (8, 'Televisor', 1, 2500.00)
]

cursor.executemany("""
INSERT INTO Produto (cod_produto, nome_produto, indicador_produto, preco_produto)
VALUES (?, ?, ?, ?)
""", produtos)

# add direto com insert into
cursor.execute("""
INSERT INTO Produto (cod_produto, nome_produto, indicador_produto, preco_produto)
VALUES (?, ?, ?, ?)
""", (9, 'Sanduicheira', 1, 70.00))

# lista de tuplas da tabela Regiao
regioes = [
    ('N01', 'Região Norte'),
    ('S01', 'Região Sul'),
    ('L01', 'Região Leste'),
    ('O01', 'Região Oeste'),
    ('C01', 'Região Central')
]

cursor.executemany("""
INSERT INTO Regiao (cod_regiao, nome_regiao)
VALUES (?, ?)
""", regioes)

# lista de tuplas de Vendedor
vendedor = [
    ('NV059', 'Larissa Maia', 'N01'),
    ('SV708', 'Jorge Silva', 'S01'),
    ('LV562', 'Maria Nogueira', 'L01'),
    ('OV002', 'Antônio Almeida', 'O01'),
    ('CV895', 'Thamires Lima', 'C01'),
    ('NV562', 'Linda Maria', 'N01'),
    ('SV066', 'Mariana Correa', 'S01'),
    ('LV401', 'Floriano da Silva', 'L01'),
    ('OV012', 'Agostinho Carrara', 'O01')
]

cursor.executemany("""
INSERT INTO Vendedor (cod_vendedor, nome_vendedor, cod_vendedor_regiao)
VALUES (?, ?, ?)""", vendedor)

# lista de tuplas Veiculo
veiculo = [
    ('VE01', 'ABC1234'),
    ('VE02', 'DEF5678'),
    ('VE03', 'GHI9101'),
    ('VE04', 'JKL1213')
]

cursor.executemany("""
INSERT INTO Veiculo (cod_veiculo, num_placa_veiculo)
VALUES (?, ?)
""", veiculo)

#PAREI AQUI, INSERINDO DADOS NAS TABELAS DEPENDENTES 💋
cursor.execute("""
INSERT INTO Nota_Fiscal (cod_cliente, cod_vendedor)
VALUES (?, ?, ?)""", ()) 

conn.commit()
conn.close()