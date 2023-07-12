class CustomError(Exception):
    def __init__(self, message, http_status_code):
        self.message = message
        self.http_status_code = http_status_code
        super().__init__(self.message)

    def get_http_status(self):
        return self.http_status_code
