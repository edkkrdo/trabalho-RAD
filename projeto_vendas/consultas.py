from sqlite3 import Connection


# ==========================
# CONSULTA 1 - CATÁLOGO ATIVO
# ==========================

def buscar_produtos_ativos(conn: Connection):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT cod_produto, nome_produto
        FROM Produto
        WHERE indicador_produto = 1
    """)

    return cursor.fetchall()


def imprimir_produtos_ativos(conn: Connection) -> None:
    produtos = buscar_produtos_ativos(conn)

    print("\n=== PRODUTOS ATIVOS ===")

    if produtos:
        for cod_produto, nome_produto in produtos:
            print(f"{cod_produto}: {nome_produto}")
    else:
        print("Nenhum produto ativo encontrado.")


# ==========================
# CONSULTA 2 - INVENTÁRIO DE FROTA
# ==========================

def buscar_veiculos(conn: Connection):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT num_placa_veiculo
        FROM Veiculo
    """)

    return cursor.fetchall()


def imprimir_veiculos(conn: Connection) -> None:
    veiculos = buscar_veiculos(conn)

    print("\n=== INVENTÁRIO DE FROTA ===")

    for (placa,) in veiculos:
        print(placa)


# ==========================
# CONSULTA 3 - HISTÓRICO DO CLIENTE
# ==========================

def buscar_historico_cliente(conn: Connection, nome_cliente: str):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT nf.cod_vendedor
        FROM Nota_Fiscal nf
        JOIN Cliente c
            ON nf.cod_cliente = c.cod_cliente
        WHERE c.nome_cliente = ?
    """, (nome_cliente,))

    return cursor.fetchall()


def imprimir_historico_cliente(conn: Connection, nome_cliente: str) -> None:
    vendedores = buscar_historico_cliente(conn, nome_cliente)

    print(f"\n=== HISTÓRICO DO CLIENTE: {nome_cliente} ===")

    if vendedores:
        for (cod_vendedor,) in vendedores:
            print(cod_vendedor)
    else:
        print("Nenhum vendedor encontrado.")


# ==========================
# CONSULTA 4 - TOP PRODUTO
# ==========================

def buscar_top_produto(conn: Connection):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.nome_produto,
            SUM(i.qnt_produto) AS total_vendido
        FROM Produto p
        JOIN Item_da_Nota_Fiscal i
            ON p.cod_produto = i.cod_produto
        GROUP BY p.cod_produto
        ORDER BY total_vendido DESC
        LIMIT 1
    """)

    return cursor.fetchone()


def imprimir_top_produto(conn: Connection) -> None:
    resultado = buscar_top_produto(conn)

    print("\n=== PRODUTO MAIS VENDIDO ===")

    if resultado:
        nome_produto, total = resultado
        print(f"{nome_produto} - {total} unidades vendidas")
    else:
        print("Nenhum produto encontrado.")


# ==========================
# CONSULTA 5 - DESEMPENHO REGIONAL
# ==========================

def buscar_desempenho_regional(conn: Connection):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            r.nome_regiao,
            COUNT(nf.num_nf) AS total_notas
        FROM Nota_Fiscal nf
        JOIN Vendedor v
            ON nf.cod_vendedor = v.cod_vendedor
        JOIN Regiao r
            ON v.cod_vendedor_regiao = r.cod_regiao
        GROUP BY r.cod_regiao
        ORDER BY total_notas DESC
    """)

    return cursor.fetchall()


def imprimir_desempenho_regional(conn: Connection) -> None:
    regioes = buscar_desempenho_regional(conn)

    print("\n=== DESEMPENHO REGIONAL ===")

    for regiao, total in regioes:
        print(f"{regiao}: {total} nota(s) fiscal(is)")