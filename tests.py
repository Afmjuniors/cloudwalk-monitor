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


select_test()
# delete_database()

# print(str_to_timestamp('00h 10'))
