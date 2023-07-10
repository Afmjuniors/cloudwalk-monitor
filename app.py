from flask import Flask


from controller.TransactionsController import TransactionsController
from business.TransactionsBusiness import TransactionBusiness
from database.TransactionsDatabase import TransactionsDatabase
from alert.SendEmail import SendEmail

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Dependency Injections
transaction_database = TransactionsDatabase()
send_email = SendEmail()
transaction_business = TransactionBusiness(transaction_database, send_email)
transaction_controller = TransactionsController(transaction_business)

# ENDPOINT to insert new data, at the moment must be a CSV file, named "file", later this can be changed
app.route('/api/transactions', methods=['POST'])(transaction_controller.receive_transaction)

# ENDPOINT to request data for analysis, it can receive queries to indicate limit and frequency time
app.route('/api/transactions', methods=['GET'])(transaction_controller.get_data)

if __name__ == '__main__':
    app.run()
