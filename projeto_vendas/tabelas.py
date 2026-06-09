from sqlite3 import Connection


def criar_tabelas(conn: Connection) -> None:
    """Cria todas as tabelas do banco de dados."""
    cursor = conn.cursor()

    # ==========================================================
    # LIMPEZA DO BANCO
    # Remove as tabelas existentes para evitar erros ao executar
    # o programa várias vezes durante os testes.
    # ==========================================================
    cursor.execute("PRAGMA foreign_keys = OFF;")

    cursor.execute("DROP TABLE IF EXISTS Utilizacao_Veiculo;")
    cursor.execute("DROP TABLE IF EXISTS Ponto_Estrategico;")
    cursor.execute("DROP TABLE IF EXISTS Item_da_Nota_Fiscal;")
    cursor.execute("DROP TABLE IF EXISTS Nota_Fiscal;")
    cursor.execute("DROP TABLE IF EXISTS Vendedor;")
    cursor.execute("DROP TABLE IF EXISTS Veiculo;")
    cursor.execute("DROP TABLE IF EXISTS Regiao;")
    cursor.execute("DROP TABLE IF EXISTS Cliente;")
    cursor.execute("DROP TABLE IF EXISTS Produto;")

    cursor.execute("PRAGMA foreign_keys = ON;")

    # ==========================================================
    # TABELA PRODUTO
    # Armazena os produtos vendidos pela empresa.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Produto(
            cod_produto INTEGER PRIMARY KEY,
            nome_produto VARCHAR(100),
            indicador_produto BOOLEAN NOT NULL,
            preco_produto REAL NOT NULL
        )
        """
    )

    # ==========================================================
    # TABELA CLIENTE
    # Armazena os clientes cadastrados.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Cliente(
            cod_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente VARCHAR(20) NOT NULL
        )
        """
    )

    # ==========================================================
    # TABELA REGIAO
    # Define as regiões de atuação da empresa.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Regiao(
            cod_regiao CHAR(3) PRIMARY KEY,
            nome_regiao VARCHAR(30)
        )
        """
    )

    # ==========================================================
    # TABELA VEICULO
    # Armazena os veículos da frota.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Veiculo(
            cod_veiculo CHAR(4) PRIMARY KEY,
            num_placa_veiculo VARCHAR(10) NOT NULL
        )
        """
    )

    # ==========================================================
    # TABELA VENDEDOR
    # Cada vendedor pertence a uma região.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Vendedor(
            cod_vendedor CHAR(5) PRIMARY KEY,
            nome_vendedor VARCHAR(50),
            cod_vendedor_regiao CHAR(3) NOT NULL,
            FOREIGN KEY (cod_vendedor_regiao)
                REFERENCES Regiao(cod_regiao)
        )
        """
    )

    # ==========================================================
    # TABELA NOTA_FISCAL
    # Registra as vendas realizadas.
    # Relaciona cliente e vendedor.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Nota_Fiscal(
            num_nf INTEGER PRIMARY KEY,
            cod_cliente INTEGER NOT NULL,
            cod_vendedor CHAR(5) NOT NULL,
            FOREIGN KEY (cod_cliente)
                REFERENCES Cliente(cod_cliente),
            FOREIGN KEY (cod_vendedor)
                REFERENCES Vendedor(cod_vendedor)
        )
        """
    )

    # ==========================================================
    # TABELA ITEM_DA_NOTA_FISCAL
    # Armazena os produtos vendidos em cada nota fiscal.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Item_da_Nota_Fiscal(
            num_item_da_nf INTEGER PRIMARY KEY AUTOINCREMENT,
            num_nf INTEGER NOT NULL,
            cod_produto INTEGER NOT NULL,
            qnt_produto INTEGER NOT NULL,
            FOREIGN KEY (num_nf)
                REFERENCES Nota_Fiscal(num_nf),
            FOREIGN KEY (cod_produto)
                REFERENCES Produto(cod_produto)
        )
        """
    )

    # ==========================================================
    # TABELA PONTO_ESTRATEGICO
    # Representa pontos estratégicos vinculados às regiões.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Ponto_Estrategico(
            cod_pt_estrategico INTEGER PRIMARY KEY,
            cod_regiao CHAR(3) NOT NULL,
            FOREIGN KEY (cod_regiao)
                REFERENCES Regiao(cod_regiao)
        )
        """
    )

    # ==========================================================
    # TABELA UTILIZACAO_VEICULO
    # Controla qual vendedor utilizou determinado veículo
    # e em qual data.
    # ==========================================================
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Utilizacao_Veiculo(
            cod_veiculo CHAR(4) NOT NULL,
            data_utilizacao_veiculo DATE NOT NULL,
            cod_vendedor CHAR(5),
            FOREIGN KEY (cod_veiculo)
                REFERENCES Veiculo(cod_veiculo),
            FOREIGN KEY (cod_vendedor)
                REFERENCES Vendedor(cod_vendedor)
        )
        """
    )

    # Salva a estrutura criada
    conn.commit()