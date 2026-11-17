
"""Clase para administrar los clientes."""

from models.entidad import Entidad
from models.excepciones import (
    DatosInvalidosError,
    ParametroFaltanteError
)


class Cliente(Entidad):
    """Representa un cliente del sistema Software FJ."""

    def __init__(self, id_entidad, nombre, identificacion, correo, telefono):

        # Validar el nombre obligatorio.
        if not isinstance(nombre, str) or not nombre.strip():
            raise ParametroFaltanteError("El nombre es obligatorio.")

        super().__init__(id_entidad, nombre)

        # Validar la identificacion.
        if identificacion is None or identificacion == "":
            raise ParametroFaltanteError(
                "La identificacion es obligatoria."
            )

        if not isinstance(identificacion, str) or not identificacion.isdigit():
            raise DatosInvalidosError(
                "La identificacion debe contener solo numeros."
            )

        # Validar el correo.
        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise DatosInvalidosError("El correo no es valido.")

        # Validar el telefono.
        if not isinstance(telefono, str) or not telefono.isdigit():
            raise DatosInvalidosError(
                "El telefono debe contener solo numeros."
            )

        # Guardar los atributos encapsulados.
        self.__identificacion = identificacion
        self.__correo = correo.strip()
        self.__telefono = telefono

    def obtener_identificacion(self):
        """Consulta la identificacion del cliente."""
        return self.__identificacion

    def obtener_nombre(self):
        """Consulta el nombre heredado de Entidad."""
        return self.nombre

    def obtener_correo(self):
        """Consulta el correo del cliente."""
        return self.__correo

    def obtener_telefono(self):
        """Consulta el telefono del cliente."""
        return self.__telefono

    def describir(self):
        """Devuelve una descripcion del cliente."""
        return f"Cliente: {self.nombre}"

    def mostrar_informacion(self):
        """Muestra la informacion del cliente."""
        print("Nombre:", self.nombre)
        print("Identificacion:", self.__identificacion)
        print("Correo:", self.__correo)
        print("Telefono:", self.__telefono)
