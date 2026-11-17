
"""Clases para administrar los servicios de Software FJ."""

from abc import ABC, abstractmethod

from models.excepciones import (
    DatosInvalidosError,
    ServicioNoDisponibleError,
    CalculoInconsistenteError
)


class Servicio(ABC):
    """Clase abstracta que define las caracteristicas de un servicio."""

    def __init__(self, nombre, precio):
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if (
            not isinstance(precio, (int, float))
            or isinstance(precio, bool)
            or precio <= 0
        ):
            raise DatosInvalidosError(
                "El precio debe ser mayor que cero."
            )

        self.nombre = nombre.strip()
        self.precio = precio
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve la descripcion del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, cantidad, impuesto, descuento):
        """Valida los parametros necesarios para calcular el costo."""
        pass

    def validar_impuesto_descuento(self, impuesto, descuento):
        """Comprueba que impuesto y descuento sean validos."""

        if (
            not isinstance(impuesto, (int, float))
            or isinstance(impuesto, bool)
            or not isinstance(descuento, (int, float))
            or isinstance(descuento, bool)
        ):
            raise CalculoInconsistenteError(
                "Impuesto y descuento deben ser numeros."
            )

        if impuesto < 0 or descuento < 0 or descuento > 50:
            raise CalculoInconsistenteError(
                "El impuesto no puede ser negativo y el descuento maximo es 50 por ciento."
            )

    def validar_disponibilidad(self):
        """Comprueba que el servicio este disponible."""

        if not self.disponible:
            raise ServicioNoDisponibleError(
                "El servicio no esta disponible."
            )

    def aplicar_ajuste(self, costo, impuesto, descuento):
        """Aplica el impuesto y el descuento al costo."""

        costo = costo + (costo * impuesto / 100)
        costo = costo - (costo * descuento / 100)

        if costo < 0:
            raise CalculoInconsistenteError(
                "El costo no puede ser negativo."
            )

        return costo


class ReservaSala(Servicio):
    """Servicio de reserva de salas por horas."""

    def validar_parametros(self, cantidad, impuesto, descuento):
        self.validar_impuesto_descuento(impuesto, descuento)

        if (
            not isinstance(cantidad, (int, float))
            or isinstance(cantidad, bool)
            or cantidad <= 0
            or cantidad > 12
        ):
            raise DatosInvalidosError(
                "La sala se reserva entre 1 y 12 horas."
            )

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad, impuesto, descuento)

        costo = self.precio * cantidad
        return self.aplicar_ajuste(costo, impuesto, descuento)

    def describir(self):
        return "Reserva de salas"


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos por dias."""

    def validar_parametros(self, cantidad, impuesto, descuento):
        self.validar_impuesto_descuento(impuesto, descuento)

        if (
            not isinstance(cantidad, (int, float))
            or isinstance(cantidad, bool)
            or cantidad <= 0
            or cantidad > 30
        ):
            raise DatosInvalidosError(
                "El equipo se alquila entre 1 y 30 dias."
            )

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad, impuesto, descuento)

        costo = self.precio * cantidad
        return self.aplicar_ajuste(costo, impuesto, descuento)

    def describir(self):
        return "Alquiler de equipos"


class Asesoria(Servicio):
    """Servicio de asesoria especializada."""

    def validar_parametros(self, cantidad, impuesto, descuento):
        self.validar_impuesto_descuento(impuesto, descuento)

        if (
            not isinstance(cantidad, (int, float))
            or isinstance(cantidad, bool)
            or cantidad <= 0
        ):
            raise DatosInvalidosError(
                "La cantidad de horas de asesoria debe ser mayor que cero."
            )

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad, impuesto, descuento)

        costo = self.precio * cantidad
        return self.aplicar_ajuste(costo, impuesto, descuento)

    def describir(self):
        return "Asesoria especializada"
