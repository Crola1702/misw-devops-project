class ApiError(Exception):
    code: int
    description: str

class FieldFormatError(ApiError):
    code = 400
    description = "Field format error"

class InvalidTokenError(ApiError):
    code = 401
    description = "Invalid or expired token"

class NotAuthorizedError(ApiError):
    code = 403
    description = "Not authorized"

class NotFoundError(ApiError):
    code = 404
    description = "Not found"

class InvalidExpirationDateError(ApiError):
    code = 412
    # TODO: Reportar en el curso que el mensaje de error no es el mismo que el del enunciado
    description = "La fecha expiración no es válida"
