
# Administracion de clientes

from models.excepciones import DatosInvalidosError
from models.cliente import Cliente
from Services.registro_logs import registrar_evento, registrar_error


class GestionClientes:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):

        try:
            if cliente is None:
                raise DatosInvalidosError("Debe ingresar un cliente")

            if not isinstance(cliente, Cliente):
                raise DatosInvalidosError(
                    "El objeto ingresado no es un cliente valido"
                )

            for registrado in self.clientes:
                if registrado.id_entidad == cliente.id_entidad:
                    raise DatosInvalidosError("El cliente ya existe")

                if registrado.obtener_identificacion() == cliente.obtener_identificacion():
                    raise DatosInvalidosError(
                        "La identificacion ya esta registrada"
                    )

            self.clientes.append(cliente)
            registrar_evento(
                f"Cliente agregado: {cliente.obtener_nombre()}"
            )
            print("Cliente agregado correctamente")

        except DatosInvalidosError as error:
            registrar_error(f"Error al agregar cliente: {error}")
            raise

    def mostrar_clientes(self):

        registrar_evento("Consulta de listado de clientes")

        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def buscar_cliente(self, identificacion):

        for cliente in self.clientes:
            if cliente.obtener_identificacion() == identificacion:
                registrar_evento(
                    f"Cliente encontrado: {identificacion}"
                )
                return cliente

        registrar_evento(
            f"Busqueda sin resultados para identificacion: {identificacion}"
        )
        return None
