class MiLista:
    def __init__(self):
        self.lista = []
    
    def agregar(self, elemento):
        self.lista.append(elemento)
    
    def eliminar(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print(f"{elemento} no encontrado en la lista.")
    
    def mostrar(self):
        print(self.lista)

#Ejemplo de uso
#Mandamos a llamar a la clase
lista = MiLista()

#Definiciones dentro de la clase
lista.agregar("Alumnos")
lista.agregar("Profesores")
lista.mostrar()

lista.eliminar("Alumnos")
lista.mostrar()

lista.eliminar("Pizarron")  #Este no se encuentra en el arreglo
