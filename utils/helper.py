from datetime import datetime
import pandas as pd


def str_to_timestamp(time_str: str) -> datetime:
    return datetime.combine(datetime.now().date(), datetime.strptime(time_str, "%Hh %M").time())


def transform_date_timestamp_to_str(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    hora_minuto = dt.strftime("%H:%M")
    return hora_minuto


def request_to_dataframe(request):
    df = None
    if 'file' in request.files:
        file = request.files['file']
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.mimetype == 'application/json':
        df = pd.read_json(file)
    else:
        df = pd.DataFrame(request.json)

    return df
