# Administracion de servicios

from models.excepciones import DatosInvalidosError


class GestionServicios:

    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio):

        if servicio is None:
            raise DatosInvalidosError("Debe ingresar un servicio")

        for registrado in self.servicios:
            if registrado.nombre == servicio.nombre:
                raise DatosInvalidosError("El servicio ya existe")

        self.servicios.append(servicio)
        print("Servicio agregado correctamente")

    def mostrar_servicios(self):

        for servicio in self.servicios:
            print(servicio.describir(), "-", servicio.precio)

    def buscar_servicio(self, nombre):

        for servicio in self.servicios:
            if servicio.nombre == nombre:
                return servicio

        return None