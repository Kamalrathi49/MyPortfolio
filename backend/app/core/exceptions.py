class AppException(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundError(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__("NOT_FOUND", message, 404)


class ConflictError(AppException):
    def __init__(self, message: str):
        super().__init__("CONFLICT", message, 409)


class UnauthorizedError(AppException):
    def __init__(self, message: str = "Invalid or missing credentials"):
        super().__init__("UNAUTHORIZED", message, 401)


class RateLimitError(AppException):
    def __init__(self, message: str = "Too many requests. Try again later."):
        super().__init__("RATE_LIMITED", message, 429)
