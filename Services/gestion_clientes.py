
# Administracion de clientes

from models.excepciones import DatosInvalidosError
from models.cliente import Cliente


class GestionClientes:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):

        if cliente is None:
            raise DatosInvalidosError("Debe ingresar un cliente")

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("El objeto ingresado no es un cliente valido")

        for registrado in self.clientes:
            if registrado.id_entidad == cliente.id_entidad:
                raise DatosInvalidosError("El cliente ya existe")

            if registrado.obtener_identificacion() == cliente.obtener_identificacion():
                raise DatosInvalidosError("La identificacion ya esta registrada")

        self.clientes.append(cliente)
        print("Cliente agregado correctamente")

    def mostrar_clientes(self):

        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def buscar_cliente(self, identificacion):

        for cliente in self.clientes:
            if cliente.obtener_identificacion() == identificacion:
                return cliente

        return None
