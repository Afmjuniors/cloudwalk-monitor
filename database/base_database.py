import psycopg2


# Função para estabelecer a conexão com o banco de dados
def connect_to_database():
    try:
        # Estabeleça a conexão com o banco de dados
        conn = psycopg2.connect(
            host='localhost',
            port='5432',
            database='monitor',
            user='postgres',
            password='123456'
        )
        return conn

    except psycopg2.Error as e:
        # Se ocorrer algum erro na conexão, imprima a mensagem de erro
        print("Ocorreu um erro ao conectar ao banco de dados:", e)


