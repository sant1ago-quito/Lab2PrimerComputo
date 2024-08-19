# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:40:11 2024

@author: Admin
"""

class autos():
    def __init__(self):
        self.caracteristicas = []
        print("*****************BIENVENIDO****************")
        self.precio = float(input("Introduzca el precio de compra del auto: "))
        self.i = 1
        self.ruedas = 4
        self.capacidad = "5 personas"
    def precio_venta(self):
        return self.precio * 1.40
    
    def ingresarcaracteristicas(self):
        print("")
        while self.i <= 10:
            caracteristicas = input(f"Por favor escriba la caracteristica {self.i} del auto: ")
            self.caracteristicas.append(caracteristicas)
            self.i = self.i + 1
    
    def mostrarinfo(self):
        print("")
        print("*****************************************************************")
        print("Caracteristicas del auto:", ", ".join(self.caracteristicas) + ". "f"Cada auto cuenta con {self.ruedas} ruedas, y capacidad para {self.capacidad}")
        print("Precio de venta del auto: ", self.precio_venta())
        print("*****************************************************************")

Autos = autos()
Autos.ingresarcaracteristicas()
Autos.mostrarinfo()