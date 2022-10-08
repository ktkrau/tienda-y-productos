from Tienda import Tienda
from Producto import Producto


monitor = Producto("Monitor", 200, "monitores y pantallas", 1)
teclado = Producto("Teclado bluetooth", 100, "teclados", 2)
mouse = Producto("Mouse vertical", 50, "mouse", 3)
pendrive = Producto("Pendrive", 10, "pendrives", 4)


lacasadelprogramador = Tienda()

lacasadelprogramador.agregar_producto(monitor).agregar_producto(teclado).agregar_producto(mouse).agregar_producto(pendrive).imprime_lista()

lacasadelprogramador.vender_producto(3).imprime_lista()

pendrive.print_info()

lacasadelprogramador.hacer_liquidacion("pendrives", 0.02)
pendrive.print_info()

lacasadelprogramador.inflacion(0.05)

pendrive.print_info()