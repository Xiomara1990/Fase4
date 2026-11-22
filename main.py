
"""Programa principal del sistema Software FJ."""

from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from Services.gestion_clientes import GestionClientes
from Services.gestion_servicios import GestionServicios
from Services.gestion_reservas import GestionReservas
from Services.registro_logs import registrar_evento, registrar_error


def ejecutar(numero, descripcion, accion):
    """Ejecuta una operación y controla los errores."""
    print(f"\nPRUEBA {numero}: {descripcion}")

    try:
        accion()

    except Exception as error:
        print(f"Error controlado: {error}")
        registrar_error(
            f"Prueba {numero} - {descripcion}: {error}"
        )
        return False

    else:
        print("Operación realizada correctamente.")
        registrar_evento(
            f"Prueba {numero} - {descripcion}: exitosa"
        )
        return True

    finally:
        print(f"Finalizada prueba {numero}.")


def main():
    print("=" * 50)
    print("SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 50)

    gestion_clientes = GestionClientes()
    gestion_servicios = GestionServicios()
    gestion_reservas = GestionReservas()

    datos = {}

    operaciones = [

        (1, "Registrar un cliente válido",
         lambda: (
             datos.update(cliente=Cliente(
                 1, "Ana Lopez", "1001",
                 "ana@gmail.com", "3001112233"
             )),
             gestion_clientes.agregar_cliente(
                 datos["cliente"]
             )
         )),

        (2, "Registrar un cliente con correo inválido",
         lambda: Cliente(
             2, "Carlos Perez", "1002",
             "correo-invalido", "3002223344"
         )),

        (3, "Registrar un cliente con identificación duplicada",
         lambda: gestion_clientes.agregar_cliente(
             Cliente(
                 3, "Maria Gomez", "1001",
                 "maria@gmail.com", "3003334455"
             )
         )),

        (4, "Crear y registrar una sala",
         lambda: (
             datos.update(sala=ReservaSala("Sala A", 50000)),
             gestion_servicios.agregar_servicio(
                 datos["sala"]
             )
         )),

        (5, "Crear un equipo con precio inválido",
         lambda: AlquilerEquipo("Portatil", 0)),

        (6, "Crear y registrar un alquiler de equipo",
         lambda: (
             datos.update(equipo=AlquilerEquipo("Portatil", 80000)),
             gestion_servicios.agregar_servicio(
                 datos["equipo"]
             )
         )),

        (7, "Crear y registrar una asesoría",
         lambda: (
             datos.update(asesoria=Asesoria("Asesoria Python", 100000)),
             gestion_servicios.agregar_servicio(
                 datos["asesoria"]
             )
         )),

        (8, "Crear y registrar una reserva",
         lambda: (
             datos.update(reserva=Reserva(
                 datos["cliente"], datos["sala"], 2
             )),
             gestion_reservas.agregar_reserva(
                 datos["reserva"]
             )
         )),

        (9, "Confirmar y procesar una reserva",
         lambda: (
             datos["reserva"].confirmar(),
             datos["reserva"].procesar(
                 impuesto=19, descuento=10
             )
         )),

        (10, "Intentar crear una reserva sin cliente",
         lambda: Reserva(
             None, datos["sala"], 2
         )),

        (11, "Cancelar una reserva existente",
         lambda: gestion_reservas.cancelar_reserva(
             datos["reserva"]
         )),

        (12, "Intentar cancelar nuevamente la reserva",
         lambda: gestion_reservas.cancelar_reserva(
             datos["reserva"]
         ))
    ]

    exitosas = 0
    fallidas = 0

    for numero, descripcion, accion in operaciones:
        resultado = ejecutar(numero, descripcion, accion)

        if resultado:
            exitosas += 1
        else:
            fallidas += 1

    print("\n" + "=" * 50)
    print("RESUMEN DE OPERACIONES")
    print("=" * 50)
    print(f"Operaciones exitosas: {exitosas}")
    print(f"Operaciones con errores controlados: {fallidas}")
    print(f"Total de operaciones: {exitosas + fallidas}")

    gestion_clientes.mostrar_clientes()
    gestion_servicios.mostrar_servicios()
    gestion_reservas.mostrar_reservas()

    registrar_evento("Finalización de las pruebas del sistema.")
    print("\nSistema Software FJ finalizado correctamente.")


if __name__ == "__main__":
    main()
