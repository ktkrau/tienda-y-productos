from Producto import Producto
class Tienda:


    def __init__(self):
        self.nombre = "La casa del programador"
        self.producto = []







    def imprime_lista(self):
        print("Total de productos:", len(self.producto))
        for producto in self.producto:
            print(producto.nombre)

    def agregar_producto(self, nuevo_producto):
        self.producto.append(nuevo_producto)
        return self
    
    def vender_producto(self, id):
        for elemento in self.producto:
            if elemento.id == id:
                self.producto.remove(elemento)
        return self

    def inflacion(self, porcentaje_aumento):
        for producto in self.producto:
            producto.actualizar_precio(porcentaje_aumento, True)
        return self

    def hacer_liquidacion(self, categoria_p, porcentaje_descuento):
        for producto in self.producto:
            if producto.categoria == categoria_p:
                producto.actualizar_precio(porcentaje_descuento, False)
        return self