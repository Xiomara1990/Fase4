"""Clase abstracta base para las entidades de Software FJ."""

from abc import ABC, abstractmethod

from models.excepciones import DatosInvalidosError


class Entidad(ABC):
    """Define los datos y comportamientos comunes de las entidades."""

    def __init__(self, id_entidad, nombre):
        """Valida y guarda el identificador y el nombre."""

        # El identificador debe ser un entero positivo, no un booleano.
        if type(id_entidad) is not int or id_entidad <= 0:
            raise DatosInvalidosError(
                "El identificador debe ser un numero entero positivo."
            )

        # Comprobamos el tipo antes de utilizar métodos de texto.
        if not isinstance(nombre, str):
            raise DatosInvalidosError(
                "El nombre debe ser un texto."
            )

        # Quitamos espacios sobrantes al principio y al final.
        nombre_limpio = nombre.strip()

        # Un nombre formado solo por espacios tampoco es válido.
        if not nombre_limpio:
            raise DatosInvalidosError(
                "El nombre no puede estar vacio."
            )

        # Guardamos los datos después de superar las validaciones.
        self.__id_entidad = id_entidad
        self.__nombre = nombre_limpio

    @property
    def id_entidad(self):
        """Permite consultar el identificador de la entidad."""
        return self.__id_entidad

    @property
    def nombre(self):
        """Permite consultar el nombre de la entidad."""
        return self.__nombre

    @abstractmethod
    def describir(self):
        """Exige que cada entidad implemente su propia descripción."""
        pass
