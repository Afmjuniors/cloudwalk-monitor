from flask import request
from datetime import datetime, timedelta

from utils.helper import request_to_dataframe


class TransactionsController:
    def __init__(self, transaction_business):
        self.transaction_business = transaction_business

    # ENDPOINT to insert new data, at the moment must be a CSV file named 'file', later this can be changed
    def receive_transaction(self):
        # Send the request to the helper so that the file format (CSV, JSON, or body)
        # can be transformed into a DataFrame format
        df = request_to_dataframe(request)

        self.transaction_business.transaction_business(df)

        return 'Sent transaction successfully', 201

    # ENDPOINT to request data for analysis, it can receive queries to indicate limit and frequency time
    def get_data(self):
        # Santander date is yesterday
        date_yesterday = datetime.now() - timedelta(days=1)
        date_yesterday_str = date_yesterday.strftime("%d/%m/%Y")
        # Receive queries
        date_str = request.args.get('date', date_yesterday_str)
        freq = int(request.args.get('freq', 10))

        output = self.transaction_business.get_data(date_str, freq)

        return {
            "length": len(output),
            "data": output
        }

    def get_threshold(self):
        output = self.transaction_business.get_threshold()

        return output
