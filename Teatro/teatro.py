from arbol_avl import ArbolAVL, NodoAVL

class Teatro:
    def __init__(self, nombre, filas, asientos_por_fila):
        self.nombre = nombre
        self.filas = filas
        self.asientos_por_fila = asientos_por_fila
        self.arbol = ArbolAVL()
        self.raiz = None
        self.precio_vip = 100  # Precio para asientos VIP
        self.precio_estandar = 50  # Precio para asientos estándar
        self.generar_asientos()
        

    def generar_asientos(self):
        for fila in range(self.filas):
            for asiento in range(self.asientos_por_fila):
                clave = f"{chr(65 + fila)}{asiento + 1}"
                categoria = "VIP" if fila < self.filas // 2 else "Estandar"
                precio = self.precio_vip if categoria == "VIP" else self.precio_estandar
                self.raiz = self.arbol.insertar(self.raiz, clave, categoria, precio)

    def reservar_asiento(self, clave):
        nodo = self.arbol.buscar(self.raiz, clave)
        if nodo and not nodo.reservado:
            nodo.reservado = True
            print(f"Asiento {clave} reservado exitosamente por ${nodo.precio}.")
            return nodo.precio
        elif nodo and nodo.reservado:
            print(f"Asiento {clave} ya está reservado.")
            return None
        else:
            print(f"Asiento {clave} no existe.")
            return None

    def mostrar_asientos(self):
        for fila in range(self.filas):
            fila_visual = ""
            for asiento in range(self.asientos_por_fila):
                clave = f"{chr(65 + fila)}{asiento + 1}"
                nodo = self.arbol.buscar(self.raiz, clave)
                if nodo:
                    simbolo = "R" if nodo.reservado else "L"  # L = Libre, R = Reservado
                    fila_visual += f"{simbolo}"
            print(fila_visual)