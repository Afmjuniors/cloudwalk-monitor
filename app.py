from flask import Flask, request, jsonify
import pandas as pd

from business.transaction_business import TransactionBusiness

app = Flask(__name__)

transaction_business = TransactionBusiness()

# comentar
@app.route('/api/transactions', methods=['POST'])
def receive_transaction():
    csv_file = request.files['file']  # Obtém o arquivo CSV do corpo da solicitação
    df = pd.read_csv(csv_file)

    recommendation = transaction_business.transaction_business(df)

    return 'Sent transaction with sucess'


@app.route('/api/transactions', methods=['GET'])
def receive_transaction():
    output = None
    # output = transaction.transaction_business(df)

    return output


if __name__ == '__main__':
    app.run()
