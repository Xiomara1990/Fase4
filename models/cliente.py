# Clase para administrar los clientes

from models.entidad import Entidad
from models.excepciones import DatosInvalidosError
from models.excepciones import ParametroFaltanteError


""" Se realiza un ajuste para que el cliente use la clase Entidad y no se reviente
si por ejemplo el correo o el telefono no son texto"""
class Cliente(Entidad):

    def __init__(self, id_entidad, nombre, identificacion, correo, telefono):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ParametroFaltanteError("El nombre es obligatorio")

        super().__init__(id_entidad, nombre) # Se utiliza super() para llamar al constructor de la clase padre y enviar los parametros id_entidad y nombre

        if identificacion is None:
            raise ParametroFaltanteError("La identificacion es obligatoria")

        if not isinstance(identificacion, str) or not identificacion.isdigit():
            raise DatosInvalidosError("La identificacion debe contener numeros")

        if not isinstance (correo, str) or "@" not in correo:
            raise DatosInvalidosError("El correo no es valido")

        if not isinstance(telefono, str) or not telefono.isdigit():
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
