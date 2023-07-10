from utils.helper import str_to_timestamp


class TypeTransaction:
    def __init__(self, time_str: str, status: str, value: int):
        self._time = str_to_timestamp(time_str)
        self._status = status
        self._value = int(value)

    @property
    def time(self):
        return self._time

    @property
    def status(self):
        return self._status

    @property
    def value(self):
        return self._value
