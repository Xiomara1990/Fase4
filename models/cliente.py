# Clase para administrar los clientes

from models.entidad import Entidad
from models.excepciones import DatosInvalidosError
from models.excepciones import ParametroFaltanteError


class Cliente(Entidad):

    def __init__(self, nombre, identificacion, correo, telefono):

        if not nombre or not nombre.strip():
            raise ParametroFaltanteError("El nombre es obligatorio")

        if identificacion is None:
            raise ParametroFaltanteError("La identificacion es obligatoria")

        if not isinstance(identificacion, str) or not identificacion.isdigit():
            raise DatosInvalidosError("La identificacion debe contener numeros")

        if not correo or "@" not in correo:
            raise DatosInvalidosError("El correo no es valido")

        if not telefono or not telefono.isdigit():
            raise DatosInvalidosError("El telefono debe contener numeros")

        self.__nombre = nombre.strip()
        self.__identificacion = identificacion
        self.__correo = correo
        self.__telefono = telefono

    # Consultar identificacion
    def obtener_identificacion(self):
        return self.__identificacion

    # Consultar nombre
    def obtener_nombre(self):
        return self.__nombre

    # Mostrar informacion del cliente
    def describir(self):
        return f"Cliente: {self.__nombre}"

    def mostrar_informacion(self):
        print("Nombre:", self.__nombre)
        print("Identificacion:", self.__identificacion)
        print("Correo:", self.__correo)
        print("Telefono:", self.__telefono)
