
# Administracion de reservas

from models.excepciones import ReservaInvalidaError
from Services.registro_logs import registrar_evento, registrar_error


class GestionReservas:

    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):

        try:
            if reserva is None:
                raise ReservaInvalidaError("La reserva no es valida")

            self.reservas.append(reserva)

            registrar_evento("Reserva registrada correctamente")
            print("Reserva registrada correctamente")

        except ReservaInvalidaError as error:
            registrar_error(f"Error al registrar reserva: {error}")
            raise

    def mostrar_reservas(self):

        registrar_evento("Consulta del listado de reservas")

        for reserva in self.reservas:
            print(
                "Cliente:", reserva.cliente.obtener_nombre(),
                "| Servicio:", reserva.servicio.nombre,
                "| Estado:", reserva.estado
            )

    def cancelar_reserva(self, reserva):

        try:
            if reserva not in self.reservas:
                raise ReservaInvalidaError("La reserva no existe")

            reserva.cancelar()

            registrar_evento("Reserva cancelada correctamente")

        except ReservaInvalidaError as error:
            registrar_error(f"Error al cancelar reserva: {error}")
            raise
