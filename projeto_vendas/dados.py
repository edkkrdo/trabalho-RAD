from sqlite3 import Connection


def inserir_dados(conn: Connection) -> None:
    """Insere os dados de exemplo nas tabelas já criadas."""
    cursor = conn.cursor()

    # ==========================================================
    # CLIENTES
    # ==========================================================
    clientes = [
        ('Lohhana Pinheiro',),
        ('Eduardo Augusto',),
        ('Layse Pimenta',),
        ('Maria Leticia',)
    ]

    cursor.executemany(
        "INSERT INTO Cliente (nome_cliente) VALUES (?)",
        clientes,
    )

    # ==========================================================
    # PRODUTOS
    # ==========================================================
    produtos = [
        (1, 'Geladeira', 1, 3200.00),
        (2, 'Fogão', 1, 1200.00),
        (3, 'Micro-ondas', 0, 800.00),
        (4, 'Máquina de Lavar', 1, 2800.00),
        (5, 'Aspirador de Pó', 1, 450.00),
        (6, 'Liquidificador', 0, 220.00),
        (7, 'Ventilador', 1, 180.00),
        (8, 'Televisor', 1, 2500.00),
    ]

    cursor.executemany(
        "INSERT INTO Produto (cod_produto, nome_produto, indicador_produto, preco_produto) VALUES (?, ?, ?, ?)",
        produtos,
    )

    # Produto adicional
    cursor.execute(
        "INSERT INTO Produto (cod_produto, nome_produto, indicador_produto, preco_produto) VALUES (?, ?, ?, ?)",
        (9, 'Sanduicheira', 1, 70.00),
    )

    # ==========================================================
    # REGIÕES
    # ==========================================================
    regioes = [
        ('N01', 'Região Norte'),
        ('S01', 'Região Sul'),
        ('L01', 'Região Leste'),
        ('O01', 'Região Oeste'),
        ('C01', 'Região Central'),
    ]

    cursor.executemany(
        "INSERT INTO Regiao (cod_regiao, nome_regiao) VALUES (?, ?)",
        regioes,
    )

    # ==========================================================
    # VEÍCULOS
    # ==========================================================
    veiculos = [
        ('VE01', 'ABC1234'),
        ('VE02', 'DEF5678'),
        ('VE03', 'GHI9101'),
        ('VE04', 'JKL1213'),
    ]

    cursor.executemany(
        "INSERT INTO Veiculo (cod_veiculo, num_placa_veiculo) VALUES (?, ?)",
        veiculos,
    )

    # ==========================================================
    # VENDEDORES
    # ==========================================================
    vendedores = [
        ('NV059', 'Larissa Maia', 'N01'),
        ('SV708', 'Jorge Silva', 'S01'),
        ('LV562', 'Maria Nogueira', 'L01'),
        ('OV002', 'Antônio Almeida', 'O01'),
        ('CV895', 'Thamires Lima', 'C01'),
        ('NV562', 'Linda Maria', 'N01'),
        ('SV066', 'Mariana Correa', 'S01'),
        ('LV401', 'Floriano da Silva', 'L01'),
        ('OV012', 'Agostinho Carrara', 'O01'),
    ]

    cursor.executemany(
        "INSERT INTO Vendedor (cod_vendedor, nome_vendedor, cod_vendedor_regiao) VALUES (?, ?, ?)",
        vendedores,
    )

    # ==========================================================
    # NOTAS FISCAIS
    # ==========================================================
    notas_fiscais = [
        (1001, 1, 'NV059'),
        (1002, 2, 'SV708'),
        (1003, 1, 'NV562'),
        (1004, 3, 'OV002'),
        (1005, 4, 'CV895'),
    ]

    cursor.executemany(
        "INSERT INTO Nota_Fiscal (num_nf, cod_cliente, cod_vendedor) VALUES (?, ?, ?)",
        notas_fiscais,
    )

    # ==========================================================
    # ITENS DAS NOTAS FISCAIS
    # Cada tupla representa:
    # (num_nf, cod_produto, quantidade)
    # ==========================================================
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
        (1005, 2, 3),
    ]

    cursor.executemany(
        "INSERT INTO Item_da_Nota_Fiscal (num_nf, cod_produto, qnt_produto) VALUES (?, ?, ?)",
        itens_nf,
    )

    # ==========================================================
    # PONTOS ESTRATÉGICOS
    # ==========================================================
    pontos = [
        (1, 'N01'),
        (2, 'S01'),
        (3, 'L01'),
        (4, 'O01'),
        (5, 'C01'),
    ]

    cursor.executemany(
        "INSERT INTO Ponto_Estrategico (cod_pt_estrategico, cod_regiao) VALUES (?, ?)",
        pontos,
    )

    # ==========================================================
    # UTILIZAÇÃO DOS VEÍCULOS
    # ==========================================================
    utilizacoes = [
        ('VE01', '2025-01-10', 'NV059'),
        ('VE02', '2025-01-12', 'SV708'),
        ('VE03', '2025-01-15', 'OV002'),
        ('VE04', '2025-01-18', 'CV895'),
        ('VE01', '2025-01-20', 'NV562'),
    ]

    cursor.executemany(
        "INSERT INTO Utilizacao_Veiculo (cod_veiculo, data_utilizacao_veiculo, cod_vendedor) VALUES (?, ?, ?)",
        utilizacoes,
    )

    # Salva todas as inserções realizadas
    conn.commit()