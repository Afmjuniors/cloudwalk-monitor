from datetime import datetime
from sklearn.ensemble import IsolationForest
import numpy as np

from utils.helper import transform_date_timestamp_to_str


class TransactionBusiness:

    def __init__(self, transaction_database, send_email):
        self.transaction_database = transaction_database
        self.send_email = send_email

    # Internal method toCalculate  mean and standard deviation
    def _analyze_historical_data(self):
        # Retrieve historical data from the database
        historical_data = self.transaction_database.get_all_transactions()

        # Separate the data by transaction type
        failed_transactions = []
        denied_transactions = []
        reversed_transactions = []
        processing_transactions = []

        for transaction in historical_data:
            if transaction[2] == 'failed':
                failed_transactions.append(transaction[3])
            elif transaction[2] == 'denied':
                denied_transactions.append(transaction[3])
            elif transaction[2] == 'reversed' or transaction[2] == 'backend_reversed':
                reversed_transactions.append(transaction[3])
            elif transaction[2] == 'processing':
                processing_transactions.append(transaction[3])

        # Calculate  mean and standard deviation for each transaction type
        threshold_failed = np.mean(failed_transactions) + np.std(failed_transactions)
        threshold_denied = np.mean(denied_transactions) + np.std(denied_transactions)
        threshold_reversed = np.mean(reversed_transactions) + np.std(reversed_transactions)
        threshold_processing = np.mean(processing_transactions) + np.std(processing_transactions)

        # Return the calculated adaptive thresholds
        return threshold_failed, threshold_denied, threshold_reversed, threshold_processing

    # Intern function to analyze data by rule base
    # Internal function to analyze data by rule base
    # Internal function to analyze data by rule base
    def _analyze_transactions(self,
                              total_transactions,
                              total_failed,
                              total_denied,
                              total_reversed,
                              total_processing
                              ):

        threshold_denied, threshold_reversed, threshold_failed, threshold_processing = self._analyze_historical_data()

        if total_reversed >= threshold_reversed:
            self._send_alert('Number of reversed operations exceeds the threshold')

        if total_denied >= threshold_denied:
            self._send_alert('Number of denied operations exceeds the threshold')

        if total_failed >= threshold_failed:
            self._send_alert('Number of failed operations exceeds the threshold')

        if total_processing >= threshold_processing:
            self._send_alert('Number of processing operations exceeds the threshold')

    # Internal function to analyze data by machine learning (score-based)
    def _analyze_transactions_machine_learning(self):
        pass

    # Internal function to send a message to equipment
    def _send_alert(self, message):
        email_receiver = 'afmjuniors@gmail.com'
        self.send_email.send_email(message, email_receiver)

    # Method to receive data to analyze in DataFrame format
    def transaction_business(self, df):
        total_transactions = 0
        total_failed = 0
        total_denied = 0
        total_reversed = 0
        total_approved = 0
        total_processing = 0

        for index, row in df.iterrows():
            self.transaction_database.insert_transaction(row['time'], row['status'], row['count'])
            if row['status'] == 'failed':
                total_failed = row['count']
            elif row['status'] == 'denied':
                total_denied = row['count']
            elif row['status'] == 'reversed' or row['status'] == 'backend_reversed':
                total_reversed += row['count']
            elif row['status'] == 'approved' or row['status'] == 'refunded':
                total_approved += row['count']
            else:
                total_processing += row['count']

            total_transactions += row['count']

        self._analyze_transactions(total_transactions, total_failed, total_denied, total_reversed, total_processing)

    def get_data(self, date_str: str, freq: int):
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")

        # Get the timestamp in seconds
        timestamp = int(date_obj.timestamp())

        results = self.transaction_database.get_data_by_date(date_str, freq)

        transformed_results = []
        timestamp_i = timestamp
        timestamp_f = timestamp_i + (freq - 1) * 60

        for row in results:
            interval_start, interval_end, status, count = row
            # Transform datetime into timestamp
            print(interval_start)
            interval_start = interval_start.timestamp()
            interval_end = interval_end.timestamp()

            # Use the same initial time and final time for data inside the group
            if interval_start > timestamp_f:
                timestamp_i = timestamp_f + 60
                timestamp_f = timestamp_i + (freq - 1) * 60
            # Create a dictionary based on the tuple from the database
            result_dict = {
                "interval_start": transform_date_timestamp_to_str(timestamp_i),
                "interval_end": transform_date_timestamp_to_str(timestamp_f),
                "status": status,
                "count": count
            }
            transformed_results.append(result_dict)

        return transformed_results
