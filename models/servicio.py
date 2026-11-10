from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def describir(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, cantidad):
        return self.precio * cantidad

    def describir(self):
        return "Reserva de sala"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, cantidad):
        return self.precio + cantidad

    def describir(self):
        return "Alquiler de equipos"


class Asesoria(Servicio):

    def calcular_costo(self, cantidad):
        return self.precio * cantidad

    def describir(self):
        return "Asesoria especializada"
