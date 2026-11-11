# Clases para administrar los servicios

from abc import ABC, abstractmethod
from models.excepciones import DatosInvalidosError
from models.excepciones import ServicioNoDisponibleError
from models.excepciones import CalculoInconsistenteError


class Servicio(ABC):

    def __init__(self, nombre, precio):
        if not nombre or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio")

        if not isinstance(precio, (int, float)) or precio <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero")

        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError("El servicio no esta disponible")


class ReservaSala(Servicio):

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()

        costo = self.precio * cantidad
        costo = costo + (costo * impuesto / 100)
        costo = costo - (costo * descuento / 100)

        if costo < 0:
            raise CalculoInconsistenteError("El costo no puede ser negativo")

        return costo

    def describir(self):
        return "Reserva de salas"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()

        costo = self.precio * cantidad
        costo = costo + (costo * impuesto / 100)
        costo = costo - (costo * descuento / 100)

        if costo < 0:
            raise CalculoInconsistenteError("El costo no puede ser negativo")

        return costo

    def describir(self):
        return "Alquiler de equipos"


class Asesoria(Servicio):

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()

        costo = self.precio * cantidad
        costo = costo + (costo * impuesto / 100)
        costo = costo - (costo * descuento / 100)

        if costo < 0:
            raise CalculoInconsistenteError("El costo no puede ser negativo")

        return costo

    def describir(self):
        return "Asesoria especializada"
