from flask import Flask
from threading import Thread

from controller.TransactionsController import TransactionsController
from business.TransactionsBusiness import TransactionBusiness
from database.TransactionsDatabase import TransactionsDatabase
from alert.SendAlert import SendAlert
from monitor.realtime_monitor import create_real_time_line_graph

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# =============================================
# All Methods and functions initiated by '_' is internal ONLY
# ==============================================

# Dependency Injections
transaction_database = TransactionsDatabase()
send_alert = SendAlert()
transaction_business = TransactionBusiness(transaction_database, send_alert)
transaction_controller = TransactionsController(transaction_business)

# ENDPOINT to insert new data, at the moment must be a CSV file, named "file", later this can be changed
app.route('/api/transactions', methods=['POST'])(transaction_controller.receive_transaction)

# ENDPOINT to request data for analysis, it can receive queries to indicate limit and frequency time
app.route('/api/transactions', methods=['GET'])(transaction_controller.get_data)

# ENDPOINT to request current Threshold
app.route('/api/threshold', methods=['GET'])(transaction_controller.get_threshold)


def run_flask_server():
    app.run()


if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = Thread(target=run_flask_server)
    flask_thread.start()
    # app.run()

    # Start the real-time monitor
    create_real_time_line_graph()
