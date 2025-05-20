
class Cola:
    def __init__(self):
        self.cola = []
    
    def encolar(self, item):
        self.cola.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            print("La cola está vacía.")
    
    def esta_vacia(self):
        return len(self.cola) == 0
    
#Ejemplo de uso
q = Cola()

# Poner en cola los elementos
q.encolar("uno")
q.encolar("dos")
q.encolar("tres")

# Quitar de la cola los elementos
print("Desencolando elementos:")
print(q.desencolar())  # uno
print(q.desencolar())  # dos
print(q.desencolar())  # tres
print(q.desencolar())  # debería decir que esta vacia
