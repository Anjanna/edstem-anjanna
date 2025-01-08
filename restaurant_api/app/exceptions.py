class ValidationException(Exception):
    def __init__(self, message="Invalid input data"):
        self.message = message
        self.status_code = 400
        super().__init__(self.message)