import csv
from datetime import datetime, timedelta
from database.base_database import connect_to_database

conn = connect_to_database()
cursor = conn.cursor()

# ====================Code to insert rows into database by csv file=====================================

date_yesterday = datetime.now().date() - timedelta(days=2)
# Insert the data into the 'transactions' table
query = "INSERT INTO transactions (time, status, count) VALUES (%s, %s, %s)"
with open('monitor/transactions_1.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        time = row['time']
        status = row['status']
        count = int(row['f0_'])  # ATENTION!!!! THIS COLUMN MUST HAVE THE SAME NAME AS IN THE FILE
        timestamp = datetime.combine(date_yesterday, datetime.strptime(time, "%Hh %M").time())

        cursor.execute(query, (timestamp, status, count))

# Commit the changes to the database
conn.commit()

# Close the database connection
cursor.close()
conn.close()
