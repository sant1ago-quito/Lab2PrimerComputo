# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:14:33 2024

@author: Admin
"""

class elecdisp():
    def __init__(self):
        print("**************************BIENVENIDO*********************")
        self.marca = "PHR"
        self.caracteristicas = []
        self.preciocom = float(input("Por favor, ingrese el precio de compra del dispositivo: "))
        self.i = 1
    def ingresacarac(self):
        while self.i <= 6:
            caracteristica = input(f"Por favor ingrese la caracteristica {self.i}: ")
            self.caracteristicas.append(caracteristica)
            
            self.i = self.i + 1
            
    def preciovent(self):
        return self.preciocom * 1.7
    
    def mostrarinfo(self):
        print("")
        print("******************************************************")
        print("Caracteristicas del dispositivo:", ", ".join(self.caracteristicas) + ". " + f"Todos nuestros productos son importados y pertenecen a la marca {self.marca}")
        print("Precio de venta del dispositivo:", self.preciovent())
        print("*******************************************************")
disp = elecdisp()
disp.ingresacarac()
disp.mostrarinfo()