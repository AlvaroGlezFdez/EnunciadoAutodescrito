
import time
from teatro import Teatro

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def hacer_reserva(self, teatro, clave_asiento):
        print(f"Cliente {self.nombre} intenta reservar el asiento {clave_asiento}...")
        precio = teatro.reservar_asiento(clave_asiento)
        if precio:
            self.reservas.append({'asiento': clave_asiento, 'precio': precio})
        time.sleep(1)

    def ver_reservas(self):
        print(f"Reservas de {self.nombre}: ")
        for reserva in self.reservas:
            print(f"  Asiento: {reserva['asiento']} - ${reserva['precio']}")