from datetime import datetime
from database.base_database import connect_to_database
from error.DatabaseError import DatabaseError


class TransactionsDatabase:
    def __init__(self):
        self._conn = connect_to_database()

    def get_all_transactions(self):
        try:
            cursor = self._conn.cursor()
            query = "SELECT * FROM transactions"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results

        except Exception as e:
          raise DatabaseError(f"Error retrieving transactions: {e}")

    def get_data_by_date(self, date_str, freq):
        try:
            # Convert the date string to a datetime object
            date = datetime.strptime(date_str, "%d/%m/%Y")

            # Calculate the start and end of the day in timestamp format
            start_time = date.replace(hour=0, minute=0, second=0)
            end_time = date.replace(hour=23, minute=59, second=59)

            # ATENTION TO TIME ZONE
            cursor = self._conn.cursor()
            query = f"""
                SELECT
                    MIN(time AT TIME ZONE 'America/Sao_Paulo') AS interval_start,
                    MAX(time AT TIME ZONE 'America/Sao_Paulo') AS interval_end,
                    status,
                    SUM(count) AS count
                FROM
                    transactions
                WHERE
                    time AT TIME ZONE 'America/Sao_Paulo' >= TIMESTAMP '{start_time}' AND
                    time AT TIME ZONE 'America/Sao_Paulo' <= TIMESTAMP '{end_time}'
                GROUP BY
                    FLOOR(EXTRACT(EPOCH FROM time AT TIME ZONE 'America/Sao_Paulo') / (60 * {freq})),
                    status
                ORDER BY
                    interval_start
            """
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results

        except Exception as e:
            raise DatabaseError(f"Error retrieving transactions: {e}")

    def insert_transaction(self, time_str, status, count):
        try:
            timestamp = datetime.combine(datetime.now().date(), datetime.strptime(time_str, "%Hh %M").time())
            cursor = self._conn.cursor()
            query = "INSERT INTO transactions (time, status, count) VALUES (%s, %s, %s)"
            values = (timestamp, status, count)
            cursor.execute(query, values)
            self._conn.commit()
            cursor.close()
        except Exception as e:
            raise DatabaseError(f"Error retrieving transactions: {e}")

    def get_transactions_by_status(self, status):
        try:
            cursor = self._conn.cursor()
            query = "SELECT * FROM transactions WHERE status = %s"
            cursor.execute(query, (status,))
            results = cursor.fetchall()
            cursor.close()
            return results

        except Exception as e:
            raise DatabaseError(f"Error retrieving transactions: {e}")

    def update_transaction_count(self, transaction_id, new_count):
        try:
            cursor = self._conn.cursor()
            query = "UPDATE transactions SET count = %s WHERE id = %s"
            values = (new_count, transaction_id)
            cursor.execute(query, values)
            self._conn.commit()
            cursor.close()
        except Exception as e:
            raise DatabaseError(f"Error retrieving transactions: {e}")

    def delete_transaction(self, transaction_id):
        try:
            cursor = self._conn.cursor()
            query = "DELETE FROM transactions WHERE id = %s"
            cursor.execute(query, (transaction_id,))
            self._conn.commit()
            cursor.close()
        except Exception as e:
            raise DatabaseError(f"Error retrieving transactions: {e}")
