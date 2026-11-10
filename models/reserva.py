from models.excepciones import ReservaInvalidaError

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado == "Cancelada":
            raise ReservaInvalidaError("No se puede confirmar")

        self.estado = "Confirmada"
        print("Reserva confirmada")

    def cancelar(self):
        self.estado = "Cancelada"
        print("Reserva cancelada")

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo()
            print("Costo de la reserva:", costo)

        except ReservaInvalidaError as error:
            print("Error:", error)

        finally:
            print("Proceso terminado")
