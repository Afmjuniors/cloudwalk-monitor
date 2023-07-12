from datetime import datetime
import pandas as pd
from error.CustomBadRequestError import CustomBadRequestError


def str_to_timestamp(time_str: str) -> datetime:
    return datetime.combine(datetime.now().date(), datetime.strptime(time_str, "%Hh %M").time())


def transform_date_timestamp_to_str(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    hora_minuto = dt.strftime("%H:%M")
    return hora_minuto


def request_to_dataframe(request):
    try:
        df = None
        if 'file' in request.files:
            file = request.files['file']
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.mimetype == 'application/json':
                df = pd.read_json(file)
        else:
            df = pd.DataFrame(request.json)

        if df is None:
            raise CustomBadRequestError("Invalid file format or request data.")

        return df
    except Exception as e:
        raise CustomBadRequestError(f"Error converting request data to DataFrame: {e}")

