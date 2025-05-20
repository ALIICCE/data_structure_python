
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía.")
    
    def esta_vacia(self):
        return len(self.items) == 0

#Ejemplo de uso
pila = Pila()

#Apilando los elementos
pila.apilar("A")
pila.apilar("B")
pila.apilar("C")

print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())