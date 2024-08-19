# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:53:57 2024

@author: Admin
"""

class Articulo:
    def __init__(self):
        self.precio = float(input("Por favor, introduzca el precio de compra del articulo: "))

    def precio_venta(self, multiplicador=1.30):
        return self.precio * multiplicador

class Cuaderno(Articulo):
    def __init__(self):
        super().__init__()
        self.marca = "HOJITAS"
        self.hojas = int(input("Por favor, introduzca el numero de hojas (50 o 100): "))

    def mostrar_info(self):
        print("Usted ha ingresado un cuaderno de", self.hojas, "hojas, Marca:", self.marca, "cuyo precio de venta es:", self.precio_venta())

class Lapiz(Articulo):
    def __init__(self):
        super().__init__()
        self.marca = "RAYAS"
        self.tipo = input("Introduce el tipo de lapiz (grafito o colores): ")

    def mostrar_info(self):
        print("Usted ha ingresado un lapiz de tipo", self.tipo, "Marca:", self.marca, "Precio de Venta:", self.precio_venta())


tipo_articulo = input("¿Qué desea registrar, cuaderno o lapiz? ").lower()

if tipo_articulo == "cuaderno":
    cuaderno = Cuaderno()
    cuaderno.mostrar_info()

elif tipo_articulo == "lapiz":
    lapiz = Lapiz()
    lapiz.mostrar_info()

else:
    print("Artículo no reconocido.")
