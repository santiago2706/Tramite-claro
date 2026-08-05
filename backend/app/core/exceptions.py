class AppExceptions(Exceptions):
    def _init__(self, message: str):
        self.message = message
