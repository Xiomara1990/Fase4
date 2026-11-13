# Administracion de clientes

from models.excepciones import DatosInvalidosError


class GestionClientes:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):

        if cliente is None:
            raise DatosInvalidosError("Debe ingresar un cliente")

        for registrado in self.clientes:
            if registrado.obtener_identificacion() == cliente.obtener_identificacion():
                raise DatosInvalidosError("El cliente ya existe")

        self.clientes.append(cliente)
        print("Cliente agregado correctamente")

    def mostrar_clientes(self):

        for cliente in self.clientes:
            print(cliente.describir())

    def buscar_cliente(self, identificacion):

        for cliente in self.clientes:
            if cliente.obtener_identificacion() == identificacion:
                return cliente

        return None