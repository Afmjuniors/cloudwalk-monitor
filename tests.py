from database.base_database import connect_to_database
from utils.helper import str_to_timestamp

conn = connect_to_database()


def select_test():
    cursor = conn.cursor()

    # Execute a consulta SELECT
    query = "SELECT * FROM transactions"
    cursor.execute(query)

    # Obtenha todos os resultados da consulta
    results = cursor.fetchall()

    # Exiba os resultados
    for row in results:
        print(row)

    # Feche o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()


def drop_table():
    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Executar a instrução DROP TABLE
    query = "DROP TABLE transactions"
    cursor.execute(query)

    # Confirmar a exclusão dos dados
    conn.commit()

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()


def delete_database():
    cursor = conn.cursor()

    # Executar a instrução DELETE
    query = "DELETE FROM transactions"
    cursor.execute(query)

    # Confirmar a exclusão dos dados
    conn.commit()

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()


def create_table():
    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir a instrução SQL para criar a tabela
    query = """
    CREATE TABLE transactions (
      id SERIAL PRIMARY KEY,
      time TIMESTAMP,
      status VARCHAR(20),
      count INTEGER
    )
    """

    # Executar a instrução para criar a tabela
    cursor.execute(query)

    # Confirmar a criação da tabela
    conn.commit()

    # Fechar o cursor e a conexão com o banco de dados
    cursor.close()
    conn.close()


# Chamar a função create_table() para criar a tabela
# create_table()

# select_test()
# drop_table()
# delete_database()

# print(str_to_timestamp('00h 10'))
