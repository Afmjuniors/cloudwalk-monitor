import csv
from datetime import datetime, timedelta
from database.base_database import connect_to_database

conn = connect_to_database()
cursor = conn.cursor()

date_yesterday = datetime.now().date() - timedelta(days=1)
# Insira os dados na tabela 'transactions'
query = "INSERT INTO transactions (time, status, count) VALUES (%s, %s, %s)"
with open('monitor/transactions_1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time = row['time']
        status = row['status']
        count = int(row['f0_'])
        timestamp = datetime.combine(date_yesterday, datetime.strptime(time, "%Hh %M").time()).isoformat()

        cursor.execute(query, (timestamp, status, count))

# Faça o commit das alterações no banco de dados
conn.commit()

# Feche a conexão com o banco de dados
cursor.close()
conn.close()
