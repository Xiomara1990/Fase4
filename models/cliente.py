from models.entidad import Entidad
from models.excepciones import DatosInvalidosError

class Cliente(Entidad):

    def __init__(self, nombre, identificacion, correo, telefono):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__correo = correo
        self.__telefono = telefono

    def describir(self):
        return f"Cliente: {self.__nombre}"

    def validar_datos(self):
        if self.__nombre == "":
            raise DatosInvalidosError("El nombre es obligatorio")

        if self.__identificacion <= 0:
            raise DatosInvalidosError("Identificacion incorrecta")

        if "@" not in self.__correo:
            raise DatosInvalidosError("Correo invalido")

    def mostrar_informacion(self):
        print("Nombre:", self.__nombre)
        print("Identificacion:", self.__identificacion)
        print("Correo:", self.__correo)
        print("Telefono:", self.__telefono)
