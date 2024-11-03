class NodoAVL:
    def __init__(self, clave, categoria, precio):
        self.clave = clave
        self.categoria = categoria  # 'VIP' o 'Estandar'
        self.precio = precio
        self.izquierdo = None
        self.derecho = None
        self.altura = 1
        self.reservado = False


class ArbolAVL:
    def insertar(self, raiz, clave, categoria, precio):
        if not raiz:
            return NodoAVL(clave, categoria, precio)
        elif clave < raiz.clave:
            raiz.izquierdo = self.insertar(raiz.izquierdo, clave, categoria, precio)
        else:
            raiz.derecho = self.insertar(raiz.derecho, clave, categoria, precio)

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierdo), self.obtener_altura(raiz.derecho))
        balance = self.obtener_balance(raiz)

        if balance > 1 and clave < raiz.izquierdo.clave:
            return self.rotar_derecha(raiz)
        if balance < -1 and clave > raiz.derecho.clave:
            return self.rotar_izquierda(raiz)
        if balance > 1 and clave > raiz.izquierdo.clave:
            raiz.izquierdo = self.rotar_izquierda(raiz.izquierdo)
            return self.rotar_derecha(raiz)
        if balance < -1 and clave < raiz.derecho.clave:
            raiz.derecho = self.rotar_derecha(raiz.derecho)
            return self.rotar_izquierda(raiz)

        return raiz

    def buscar(self, raiz, clave):
        if not raiz or raiz.clave == clave:
            return raiz
        elif clave < raiz.clave:
            return self.buscar(raiz.izquierdo, clave)
        else:
            return self.buscar(raiz.derecho, clave)

    def rotar_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo
        y.izquierdo = z
        z.derecho = T2
        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        return y

    def rotar_derecha(self, z):
        y = z.izquierdo
        T3 = y.derecho
        y.derecho = z
        z.izquierdo = T3
        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        return y

    def obtener_altura(self, raiz):
        return 0 if not raiz else raiz.altura

    def obtener_balance(self, raiz):
        return 0 if not raiz else self.obtener_altura(raiz.izquierdo) - self.obtener_altura(raiz.derecho)