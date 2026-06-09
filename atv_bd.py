import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("vendas8.db")
cursor = conn.cursor()

# Habilitar o suporte a chaves estrangeiras no SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# ==============================================================================
# 1. CRIAÇÃO DAS TABELAS INDEPENDENTES (E AS QUE SÃO PAIS DE OUTRAS)
# ==============================================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Produto(
    cod_produto INTEGER PRIMARY KEY,
    nome_produto VARCHAR(100),
    indicador_produto BOOLEAN NOT NULL,
    preco_produto REAL NOT NULL
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente(
    cod_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente VARCHAR(20) NOT NULL
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Regiao(
    cod_regiao CHAR(3) PRIMARY KEY,
    nome_regiao VARCHAR (30)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Veiculo(
    cod_veiculo CHAR(4) PRIMARY KEY,
    num_placa_veiculo VARCHAR(10) NOT NULL
)""")

# ==============================================================================
# 2. CRIAÇÃO DAS TABELAS DEPENDENTES
# ==============================================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS Vendedor(
    cod_vendedor CHAR(5) PRIMARY KEY,
    nome_vendedor VARCHAR(50),
    cod_vendedor_regiao CHAR(3) NOT NULL,
    FOREIGN KEY (cod_vendedor_regiao) REFERENCES Regiao(cod_regiao)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Nota_Fiscal(
    num_nf INTEGER PRIMARY KEY,
    cod_cliente INTEGER NOT NULL,
    cod_vendedor CHAR(5) NOT NULL,

    FOREIGN KEY (cod_cliente)
    REFERENCES Cliente(cod_cliente),

    FOREIGN KEY (cod_vendedor)
    REFERENCES Vendedor(cod_vendedor)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Item_da_Nota_Fiscal(
    num_item_da_nf INTEGER PRIMARY KEY AUTOINCREMENT,
    num_nf INTEGER NOT NULL,
    cod_produto INTEGER NOT NULL,
    qnt_produto INTEGER NOT NULL,
    FOREIGN KEY (num_nf) REFERENCES Nota_Fiscal (num_nf),
    FOREIGN KEY (cod_produto) REFERENCES Produto (cod_produto)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Ponto_Estrategico(
    cod_pt_estrategico INTEGER PRIMARY KEY,
    cod_regiao CHAR(3) NOT NULL,
    FOREIGN KEY (cod_regiao) REFERENCES Regiao(cod_regiao)
)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Utilizacao_Veiculo(
    cod_veiculo CHAR(4) NOT NULL,
    data_utilizacao_veiculo DATE NOT NULL,
    cod_vendedor CHAR(5),
    FOREIGN KEY (cod_veiculo) REFERENCES Veiculo(cod_veiculo),
    FOREIGN KEY (cod_vendedor) REFERENCES Vendedor(cod_vendedor)
)""")

# ==============================================================================
# 3. INSERÇÃO DOS DADOS
# ==============================================================================

# --- Tabelas Pai / Independentes Primeiro ---

# 1. Clientes
clientes = [
    ('Lohhana Pinheiro',),
    ('Eduardo Augusto',),
    ('Layse Pimenta',),
    ('Maria Leticia',)
]
cursor.executemany("INSERT INTO Cliente (nome_cliente) VALUES (?)", clientes)

# 2. Produtos
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
cursor.executemany("INSERT INTO Produto (cod_produto, nome_produto, indicador_produto, preco_produto) VALUES (?, ?, ?, ?)", produtos)

# Produto extra
cursor.execute("INSERT INTO Produto (cod_produto, nome_produto, indicador_produto, preco_produto) VALUES (?, ?, ?, ?)", (9, 'Sanduicheira', 1, 70.00))

# 3. Regiões
regioes = [
    ('N01', 'Região Norte'),
    ('S01', 'Região Sul'),
    ('L01', 'Região Leste'),
    ('O01', 'Região Oeste'),
    ('C01', 'Região Central')
]
cursor.executemany("INSERT INTO Regiao (cod_regiao, nome_regiao) VALUES (?, ?)", regioes)

# 4. Veículos
veiculo = [
    ('VE01', 'ABC1234'),
    ('VE02', 'DEF5678'),
    ('VE03', 'GHI9101'),
    ('VE04', 'JKL1213')
]
cursor.executemany("INSERT INTO Veiculo (cod_veiculo, num_placa_veiculo) VALUES (?, ?)", veiculo)


# --- Tabelas Filhas / Dependentes Depois ---

# 5. Vendedores (Depende de Regiao)
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
cursor.executemany("INSERT INTO Vendedor (cod_vendedor, nome_vendedor, cod_vendedor_regiao) VALUES (?, ?, ?)", vendedor)

# 6. Notas Fiscais (Depende de Cliente e Vendedor)
notas_fiscais = [
    (1001, 1, 'NV059'),
    (1002, 2, 'SV708'),
    (1003, 1, 'NV562'),
    (1004, 3, 'OV002'),
    (1005, 4, 'CV895')
]
cursor.executemany("INSERT INTO Nota_Fiscal (num_nf, cod_cliente, cod_vendedor) VALUES (?, ?, ?)", notas_fiscais)

# 7. Itens das Notas Fiscais (Depende de Nota_Fiscal e Produto)
itens_nf = [
    (1001, 1, 2),
    (1001, 2, 1),
    (1002, 1, 3),
    (1002, 5, 4),
    (1003, 4, 2),
    (1003, 8, 1),
    (1004, 1, 1),
    (1004, 7, 5),
    (1005, 8, 2),
    (1005, 2, 3)
]
cursor.executemany("INSERT INTO Item_da_Nota_Fiscal (num_nf, cod_produto, qnt_produto) VALUES (?, ?, ?)", itens_nf)

# 8. Pontos Estratégicos (Depende de Regiao)
pontos = [
    (1, 'N01'),
    (2, 'S01'),
    (3, 'L01'),
    (4, 'O01'),
    (5, 'C01')
]
cursor.executemany("INSERT INTO Ponto_Estrategico (cod_pt_estrategico, cod_regiao) VALUES (?, ?)", pontos)

# 9. Utilização dos Veículos (Depende de Veiculo e Vendedor)
utilizacao = [
    ('VE01', '2025-01-10', 'NV059'),
    ('VE02', '2025-01-12', 'SV708'),
    ('VE03', '2025-01-15', 'OV002'),
    ('VE04', '2025-01-18', 'CV895'),
    ('VE01', '2025-01-20', 'NV562')
]
cursor.executemany("INSERT INTO Utilizacao_Veiculo (cod_veiculo, data_utilizacao_veiculo, cod_vendedor) VALUES (?, ?, ?)", utilizacao)

# ==============================================================================
# 4. CONSULTA E VALIDAÇÃO
# ==============================================================================

print("Produtos ativos (indicador = 1):")
cursor.execute("""
SELECT cod_produto, nome_produto
FROM Produto
WHERE indicador_produto = 1
""")
print(cursor.fetchall())

# Salvando e fechando
conn.commit()
conn.close()
