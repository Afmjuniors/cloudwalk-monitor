from error.CustomError import CustomError


class DatabaseError(CustomError):
    def __init__(self, message):
        super().__init__(message, 500)
