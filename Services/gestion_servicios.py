
# Administracion de servicios

from models.excepciones import DatosInvalidosError
from Services.registro_logs import registrar_evento, registrar_error


class GestionServicios:

    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio):

        try:
            if servicio is None:
                raise DatosInvalidosError("Debe ingresar un servicio")

            for registrado in self.servicios:
                if registrado.nombre == servicio.nombre:
                    raise DatosInvalidosError("El servicio ya existe")

            self.servicios.append(servicio)

            registrar_evento(
                f"Servicio agregado: {servicio.nombre}"
            )
            print("Servicio agregado correctamente")

        except DatosInvalidosError as error:
            registrar_error(f"Error al agregar servicio: {error}")
            raise

    def mostrar_servicios(self):

        registrar_evento("Consulta del listado de servicios")

        for servicio in self.servicios:
            print(servicio.describir(), "-", servicio.precio)

    def buscar_servicio(self, nombre):

        for servicio in self.servicios:
            if servicio.nombre == nombre:
                registrar_evento(f"Servicio encontrado: {nombre}")
                return servicio

        registrar_evento(f"Servicio no encontrado: {nombre}")
        return None
