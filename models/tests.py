
"""Pruebas del sistema integral Software FJ."""

import unittest

from models.entidad import Entidad
from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from models.excepciones import (
    DatosInvalidosError,
    ParametroFaltanteError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    ServicioNoDisponibleError,
    CalculoInconsistenteError,
    ErrorSistemaFJ
)

from Services.gestion_clientes import GestionClientes
from Services.gestion_servicios import GestionServicios


class EntidadPrueba(Entidad):

    def describir(self):
        return f"Entidad {self.id_entidad}: {self.nombre}"


class PruebasSistemaFJ(unittest.TestCase):

    # PRUEBAS DE ENTIDAD

    def test_entidad_valida(self):
        entidad = EntidadPrueba(1, "Laura Gomez")
        self.assertEqual(entidad.nombre, "Laura Gomez")

    def test_identificador_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            EntidadPrueba(0, "Laura Gomez")

    def test_nombre_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            EntidadPrueba(2, "   ")

    # PRUEBAS DE CLIENTES

    def test_cliente_valido(self):
        cliente = Cliente(
            1, "Laura Gomez", "12345",
            "laura@gmail.com", "3001234567"
        )
        self.assertEqual(cliente.obtener_nombre(), "Laura Gomez")
        self.assertEqual(cliente.obtener_identificacion(), "12345")

    def test_identificacion_invalida(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente(2, "Laura", "ABC", "laura@gmail.com", "3001234567")

    def test_correo_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente(3, "Laura", "12346", "correo", "3001234567")

    def test_nombre_faltante(self):
        with self.assertRaises(ParametroFaltanteError):
            Cliente(4, "", "12347", "laura@gmail.com", "3001234567")

    def test_gestion_clientes(self):
        gestion = GestionClientes()
        cliente = Cliente(
            5, "Ana Gomez", "12348",
            "ana@gmail.com", "3001234567"
        )
        gestion.agregar_cliente(cliente)

        self.assertEqual(len(gestion.clientes), 1)
        self.assertIs(gestion.buscar_cliente("12348"), cliente)

    def test_cliente_duplicado(self):
        gestion = GestionClientes()
        cliente1 = Cliente(
            6, "Ana", "12349",
            "ana@gmail.com", "3001234567"
        )
        cliente2 = Cliente(
            6, "Maria", "12350",
            "maria@gmail.com", "3001234568"
        )

        gestion.agregar_cliente(cliente1)

        with self.assertRaises(DatosInvalidosError):
            gestion.agregar_cliente(cliente2)

    # PRUEBAS DE SERVICIOS

    def test_reserva_sala(self):
        servicio = ReservaSala("Sala principal", 100)
        self.assertEqual(servicio.calcular_costo(2), 200)

    def test_alquiler_equipo(self):
        servicio = AlquilerEquipo("Computador", 50)
        self.assertEqual(servicio.calcular_costo(3), 150)

    def test_asesoria(self):
        servicio = Asesoria("Asesoria tecnica", 80)
        self.assertEqual(servicio.calcular_costo(2), 160)

    def test_calculo_con_impuesto_y_descuento(self):
        servicio = ReservaSala("Sala", 100)
        costo = servicio.calcular_costo(2, 10, 5)
        self.assertAlmostEqual(costo, 209)

    def test_cantidad_invalida(self):
        servicio = ReservaSala("Sala", 100)

        with self.assertRaises(DatosInvalidosError):
            servicio.calcular_costo(15)

    def test_servicio_no_disponible(self):
        servicio = ReservaSala("Sala", 100)
        servicio.disponible = False

        with self.assertRaises(ServicioNoDisponibleError):
            servicio.calcular_costo(2)

    def test_gestion_servicios(self):
        gestion = GestionServicios()
        servicio = ReservaSala("Sala de reuniones", 100)

        gestion.agregar_servicio(servicio)

        self.assertEqual(len(gestion.servicios), 1)
        self.assertIs(
            gestion.buscar_servicio("Sala de reuniones"),
            servicio
        )

    def test_servicio_duplicado(self):
        gestion = GestionServicios()

        gestion.agregar_servicio(ReservaSala("Sala", 100))

        with self.assertRaises(DatosInvalidosError):
            gestion.agregar_servicio(ReservaSala("Sala", 150))

    # PRUEBAS DE RESERVAS

    def crear_reserva(self):
        cliente = Cliente(
            10, "Carlos Perez", "55555",
            "carlos@gmail.com", "3001234567"
        )
        servicio = ReservaSala("Sala de eventos", 100)

        return Reserva(cliente, servicio, 2)

    def test_reserva_valida(self):
        reserva = self.crear_reserva()
        self.assertEqual(reserva.estado, "Pendiente")

    def test_reserva_sin_cliente(self):
        servicio = ReservaSala("Sala", 100)

        with self.assertRaises(ReservaInvalidaError):
            Reserva(None, servicio, 2)

    def test_duracion_invalida(self):
        cliente = Cliente(
            11, "Carlos", "55556",
            "carlos@gmail.com", "3001234567"
        )
        servicio = ReservaSala("Sala", 100)

        with self.assertRaises(ReservaInvalidaError):
            Reserva(cliente, servicio, 0)

    def test_confirmar_reserva(self):
        reserva = self.crear_reserva()
        reserva.confirmar()

        self.assertEqual(reserva.estado, "Confirmada")

    def test_procesar_reserva(self):
        reserva = self.crear_reserva()
        reserva.confirmar()

        costo = reserva.procesar()

        self.assertEqual(costo, 200)

    def test_procesar_reserva_sin_confirmar(self):
        reserva = self.crear_reserva()

        with self.assertRaises(ReservaInvalidaError):
            reserva.procesar()

    def test_cancelar_reserva(self):
        reserva = self.crear_reserva()
        reserva.cancelar()

        self.assertEqual(reserva.estado, "Cancelada")

    def test_cancelar_reserva_dos_veces(self):
        reserva = self.crear_reserva()
        reserva.cancelar()

        with self.assertRaises(OperacionNoPermitidaError):
            reserva.cancelar()

    def test_confirmar_servicio_no_disponible(self):
        reserva = self.crear_reserva()
        reserva.servicio.disponible = False

        with self.assertRaises(ServicioNoDisponibleError):
            reserva.confirmar()

    def test_encadenamiento_de_excepciones(self):
        reserva = self.crear_reserva()
        reserva.confirmar()

        with self.assertRaises(ErrorSistemaFJ) as contexto:
            reserva.procesar(0, 60)

        self.assertIsInstance(
            contexto.exception.__cause__,
            CalculoInconsistenteError
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
