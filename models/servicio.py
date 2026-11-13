# Clases para administrar los servicios

from abc import ABC, abstractmethod
from models.excepciones import DatosInvalidosError
from models.excepciones import ServicioNoDisponibleError
from models.excepciones import CalculoInconsistenteError


class Servicio(ABC):

    def __init__(self, nombre, precio):
        if not isinstance(nombre, str) or not nombre.strip():
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
    @abstractmethod
    
    def validar_parametros(self, cantidad, impuesto, descuento):
        pass
    
    def validar_impuesto_descuento(self, impuesto, descuento):
        if not isinstance(impuesto, (int, float)) or not isinstance(descuento, (int, float)):
            raise CalculoInconsistenteError("Impuesto y descuento deben ser numeros")
        
        if impuesto < 0 or descuento < 0 or descuento > 50:
            raise CalculoInconsistenteError("El descuento maximo es 50 por ciento")

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError("El servicio no esta disponible")
    def aplicar_ajuste(self, costo, impuesto, descuento):
        costo = costo + (costo * impuesto / 100)
        Costo = costo - (costo * descuento / 100)

        if costo < 0:
            raise CalculoInconsistenteError("El costo no puede ser negativo")

        return costo

class ReservaSala(Servicio):

    def validar_parametros(self, cantidad, impuesto, descuento):
        self.validar_impuesto_descuento(impuesto, descuento)

        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad > 12:
            raise DatosInvalidosError("La sala se reserva entre 1 y 12 horas")

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad,impuesto, descuento)

        costo = self.precio * cantidad
        return self.aplicar_ajuste(costo, impuesto, descuento)

    def describir(self):
        return "Reserva de salas"


class AlquilerEquipo(Servicio):
    
    def validar_parametros(self, cantidad, impuesto, descuento):
        self.validar_impuesto_descuento(impuesto, descuento)

        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad > 30:
            raise DatosInvalidosError("El equipo se alquila entre 1 y 30 dias")

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
