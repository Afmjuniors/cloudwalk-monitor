from database.base_database import connect_to_database

conn = connect_to_database()


def insert_transaction(time, status, count):
    cursor = conn.cursor()
    query = "INSERT INTO transactions (time, status, count) VALUES (%s, %s, %s)"
    values = (time, status, count)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()


def get_all_transactions():
    cursor = conn.cursor()
    query = "SELECT * FROM transactions"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def get_transactions_by_status(status):
    cursor = conn.cursor()
    query = "SELECT * FROM transactions WHERE status = %s"
    cursor.execute(query, (status,))
    results = cursor.fetchall()
    cursor.close()
    return results


def update_transaction_count(transaction_id, new_count):
    cursor = conn.cursor()
    query = "UPDATE transactions SET count = %s WHERE id = %s"
    values = (new_count, transaction_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()


def delete_transaction(transaction_id):
    cursor = conn.cursor()
    query = "DELETE FROM transactions WHERE id = %s"
    cursor.execute(query, (transaction_id,))
    conn.commit()
    cursor.close()
