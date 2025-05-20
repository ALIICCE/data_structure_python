
class MiDiccionario:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    def hash(self, clave):
        return hash(clave) % self.size
    
    def agregar(self, clave, valor):
        indice = self.hash(clave)
        self.table[indice] = valor
    
    def obtener(self, clave):
        indice = self.hash(clave)
        return self.table[indice]

personal_data = MiDiccionario()

# Usamos def agregar
personal_data.agregar("nombre", "Ramses")
personal_data.agregar("edad", 22)
personal_data.agregar("pais", "México")

# Usamos def obtener
print("Nombre:", personal_data.obtener("nombre"))
print("Edad:", personal_data.obtener("edad"))
print("País:", personal_data.obtener("pais"))

