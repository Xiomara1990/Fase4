# Administracion de reservas

from models.excepciones import ReservaInvalidaError


class GestionReservas:

    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):

        if reserva is None:
            raise ReservaInvalidaError("La reserva no es valida")

        self.reservas.append(reserva)
        print("Reserva registrada correctamente")

    def mostrar_reservas(self):

        for reserva in self.reservas:
            print(
                "Cliente:", reserva.cliente.obtener_nombre(),
                "| Servicio:", reserva.servicio.nombre,
                "| Estado:", reserva.estado
            )

    def cancelar_reserva(self, reserva):

        if reserva not in self.reservas:
            raise ReservaInvalidaError("La reserva no existe")

        reserva.cancelar()
