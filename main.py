# Programa principal de Software FJ

from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from models.excepciones import ErrorSistemaFJ
from Services.gestion_clientes import GestionClientes
from Services.gestion_servicios import GestionServicios
from Services.gestion_reservas import GestionReservas
from Services.registro_logs import registrar_evento, registrar_error


def ejecutar(numero, descripcion, accion):
    print("\n--- Operacion", numero, ":", descripcion, "---")

    try:
        resultado = accion()
    except ErrorSistemaFJ as error:
        print("Error controlado:", error)
        if error.__cause__ is not None:
            print("Causa:", error.__cause__)
        registrar_error(f"Operacion {numero}: {error}")
    except Exception as error:
        print("Error inesperado:", error)
        registrar_error(f"Operacion {numero}: {error}")
    else:
        print("Operacion correcta")
        registrar_evento(f"Operacion {numero}: {descripcion}")
        return resultado
    finally:
        print("La aplicacion sigue activa")


def main():
    clientes = GestionClientes()
    servicios = GestionServicios()
    reservas = GestionReservas()

    def registrar_ana():
        cliente = Cliente(1, "Ana Lopez", "1001", "ana@correo.com", "3001112233")
        clientes.agregar_cliente(cliente)
        return cliente

    ana = ejecutar(1, "Registrar cliente valido", registrar_ana)

    def cliente_correo_malo():
        Cliente(2, "Luis Perez", "1002", "correo-sin-arroba", "3001112244")

    ejecutar(2, "Registrar cliente con correo invalido", cliente_correo_malo)

    def cliente_telefono_malo():
        Cliente(3, "Marta Diaz", "1003", "marta@correo.com", "telefono")

    ejecutar(3, "Registrar cliente con telefono invalido", cliente_telefono_malo)

    def cliente_sin_nombre():
        Cliente(4, "   ", "1004", "vacio@correo.com", "3001112255")

    ejecutar(4, "Registrar cliente sin nombre", cliente_sin_nombre)

    def cliente_repetido():
        repetido = Cliente(5, "Ana Otra", "1001", "otra@correo.com", "3009998877")
        clientes.agregar_cliente(repetido)

    ejecutar(5, "Registrar un cliente repetido", cliente_repetido)

    def crear_sala():
        sala = ReservaSala("Sala A", 50000)
        servicios.agregar_servicio(sala)
        return sala

    sala = ejecutar(6, "Crear reserva de sala valida", crear_sala)

    def crear_equipo_malo():
        AlquilerEquipo("Portatil", 0)

    ejecutar(7, "Crear servicio con precio invalido", crear_equipo_malo)

    def crear_equipo():
        equipo = AlquilerEquipo("Portatil", 80000)
        servicios.agregar_servicio(equipo)
        return equipo

    equipo = ejecutar(8, "Crear alquiler de equipo valido", crear_equipo)

    def crear_asesoria():
        asesoria = Asesoria("Asesoria Python", 100000)
        servicios.agregar_servicio(asesoria)
        return asesoria

    asesoria = ejecutar(9, "Crear asesoria valida", crear_asesoria)

    def sala_repetida():
        servicios.agregar_servicio(ReservaSala("Sala A", 50000))

    ejecutar(10, "Registrar un servicio que ya existe", sala_repetida)

    def reserva_exitosa():
        reserva = Reserva(ana, sala, 3)
        reservas.agregar_reserva(reserva)
        reserva.confirmar()
        reserva.procesar(19, 10)
        return reserva

    ejecutar(11, "Reserva de sala confirmada y procesada", reserva_exitosa)

    def reserva_sin_confirmar():
        reserva = Reserva(ana, equipo, 2)
        reservas.agregar_reserva(reserva)
        reserva.procesar()

    ejecutar(12, "Procesar una reserva sin confirmar", reserva_sin_confirmar)

    def servicio_no_disponible():
        asesoria.disponible = False
        reserva = Reserva(ana, asesoria, 2)
        reservas.agregar_reserva(reserva)
        reserva.confirmar()

    ejecutar(13, "Confirmar un servicio no disponible", servicio_no_disponible)

    def cancelar_dos_veces():
        reserva = Reserva(ana, equipo, 1)
        reservas.agregar_reserva(reserva)
        reserva.cancelar()
        reserva.cancelar()

    ejecutar(14, "Cancelar una reserva ya cancelada", cancelar_dos_veces)

    def descuento_invalido():
        otra_sala = ReservaSala("Sala B", 40000)
        servicios.agregar_servicio(otra_sala)
        reserva = Reserva(ana, otra_sala, 2)
        reservas.agregar_reserva(reserva)
        reserva.confirmar()
        reserva.procesar(19, 80)

    ejecutar(15, "Procesar con un descuento no permitido", descuento_invalido)

    print("\n--- Clientes registrados ---")
    clientes.mostrar_clientes()
    print("\n--- Servicios registrados ---")
    servicios.mostrar_servicios()
    print("\n--- Reservas registradas ---")
    reservas.mostrar_reservas()


if __name__ == "__main__":
    main()