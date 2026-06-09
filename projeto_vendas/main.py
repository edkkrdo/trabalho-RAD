from banco import connect_db
from dados import inserir_dados
from tabelas import criar_tabelas

from consultas import (
    imprimir_produtos_ativos,
    imprimir_veiculos,
    imprimir_historico_cliente,
    imprimir_top_produto,
    imprimir_desempenho_regional
)


def main() -> None:
    conn = connect_db()

    # Cria as tabelas
    criar_tabelas(conn)

    # Insere os dados
    inserir_dados(conn)

    # Consultas básicas
    imprimir_produtos_ativos(conn)
    imprimir_veiculos(conn)

    # Consulta média
    imprimir_historico_cliente(conn, "Lohhana Pinheiro")

    # Consultas avançadas
    imprimir_top_produto(conn)
    imprimir_desempenho_regional(conn)

    conn.close()


if __name__ == "__main__":
    main()