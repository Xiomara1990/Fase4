
"""Excepciones personalizadas del sistema Software FJ."""


class ErrorSistemaFJ(Exception):
    """Representa un error general de la aplicación."""
    pass


class DatosInvalidosError(ErrorSistemaFJ):
    """Indica que un dato no cumple las validaciones."""
    pass


class ParametroFaltanteError(ErrorSistemaFJ):
    """Indica que no se proporcionó un dato obligatorio."""
    pass


class OperacionNoPermitidaError(ErrorSistemaFJ):
    """Indica que una acción no está permitida."""
    pass


class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Indica que el servicio solicitado no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistemaFJ):
    """Indica que una reserva no cumple las condiciones necesarias."""
    pass


class CalculoInconsistenteError(ErrorSistemaFJ):
    """Indica que un cálculo de costo produjo un resultado inválido."""
    pass
