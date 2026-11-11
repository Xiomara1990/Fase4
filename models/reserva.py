# Clase para administrar las reservas

from models.excepciones import ReservaInvalidaError
from models.excepciones import OperacionNoPermitidaError
from models.excepciones import CalculoInconsistenteError
from models.excepciones import ErrorSistemaFJ


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if cliente is None or servicio is None:
            raise ReservaInvalidaError("Debe indicar cliente y servicio")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaInvalidaError("La duracion debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes"
            )

        self.servicio.validar_disponibilidad()
        self.estado = "Confirmada"
        print("Reserva confirmada")

    def cancelar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya esta cancelada"
            )

        self.estado = "Cancelada"
        print("Reserva cancelada")

    def procesar(self, impuesto=0, descuento=0):

        if self.estado != "Confirmada":
            raise ReservaInvalidaError(
                "La reserva debe estar confirmada"
            )

        try:
            costo = self.servicio.calcular_costo(
                self.duracion, impuesto, descuento
            )

        except CalculoInconsistenteError as error:
            raise ErrorSistemaFJ(
                "No fue posible calcular el costo de la reserva"
            ) from error

        except Exception as error:
            raise ErrorSistemaFJ(
                "Ocurrio un error al procesar la reserva"
            ) from error

        else:
            print("Costo de la reserva:", costo)
            return costo

        finally:
            print("Finalizo el intento de procesamiento")

