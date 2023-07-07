from flask import Flask, request, jsonify
import pandas as pd

from business.transaction_business import TransactionBusiness

app = Flask(__name__)

transaction = TransactionBusiness()


@app.route('/api/transactions', methods=['POST'])
def receive_transaction():
    csv_file = request.files['file']  # Obtém o arquivo CSV do corpo da solicitação
    df = pd.read_csv(csv_file)

    recommendation = transaction.transaction_business(df)

    return 'Sent transaction with sucess'


if __name__ == '__main__':
    app.run()
