
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def mostrar_en_orden(self):
        self._in_orden(self.raiz)

    def _in_orden(self, nodo):
        if nodo is not None:
            self._in_orden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._in_orden(nodo.derecha)

#Ejemplo de uso
arbol = ArbolBinario()

#Insertar valores en el arbol
valores = [8, 3, 10, 25, 6, 14, 4, 7]
for v in valores:
    arbol.insertar(v)

#Mostrar datos en orden
print("Recorrido en orden:")
arbol.mostrar_en_orden()
