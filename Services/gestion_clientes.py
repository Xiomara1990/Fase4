
class GestionClientes:

    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente agregado")

    def buscar_cliente(self, identificacion):
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente

        return None

    def mostrar_clientes(self):
        for cliente in self.clientes:
            cliente.mostrar_informacion()
