from datetime import datetime, timedelta


def str_to_timestamp(time_str: str) -> datetime:
    return datetime.combine(datetime.now().date(), datetime.strptime(time_str, "%Hh %M").time()).isoformat()



