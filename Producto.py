
class Producto:
    def __init__(self, nombre, precio, categoria, id):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = id

    def print_info(self):
        print(f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: ${self.precio}")


    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado == True:
            self.precio = self.precio + (self.precio * cambio_porcentaje)
        else:
            self.precio = self.precio - (self.precio * cambio_porcentaje)
