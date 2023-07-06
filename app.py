from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/api/transactions', methods=['POST'])
def receive_transaction():
    csv_file = request.files['file']  # Obtém o arquivo CSV do corpo da solicitação
    df = pd.read_csv(csv_file)
    # Acesse os valores das colunas do DataFrame e processe os dados conforme necessário
    for index, row in df.iterrows():
        status = row['status']
        print(status)
        # ... lógica adicional ...

    # Exemplo: retorne uma recomendação para alertar ou não a anomalia
    if status == 'denied':
        recommendation = 'Alerta! Transação negada.'
    else:
        recommendation = 'Transação aprovada.'

    return jsonify({'recommendation': recommendation})


if __name__ == '__main__':
    app.run()
