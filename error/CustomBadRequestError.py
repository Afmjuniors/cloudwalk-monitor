from error.CustomError import CustomError


class CustomBadRequestError(CustomError):
    def __init__(self, message):
        super().__init__(message, 400)
