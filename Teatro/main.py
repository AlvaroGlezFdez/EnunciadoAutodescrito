from teatro import Teatro
from cliente import Cliente

def main():
    teatro = Teatro("Teatro Real", 5, 6)  # Personaliza las filas y asientos por fila
    cliente1 = Cliente("Alicia")
    cliente2 = Cliente("Juan")     # vamos a poner unos ejemplos de uso

    # Mostrar asientos iniciales
    teatro.mostrar_asientos()
    print("\n")

    # Clientes que realizan reservas
    cliente1.hacer_reserva(teatro, "A1")
    cliente2.hacer_reserva(teatro, "A2")
    cliente1.hacer_reserva(teatro, "B1")
    print("\n")

    # Mostramos asientos después de las reservas
    teatro.mostrar_asientos()
    cliente1.ver_reservas()
    cliente2.ver_reservas()

if __name__ == "__main__":
    main()