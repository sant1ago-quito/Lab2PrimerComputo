# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:15:17 2024

@author: Admin
"""

class VetPerro():
    def __init__(self):
        print("*******************TOMA DE DATOS********************")
        self.Nombre = input("Por favor ingrese el nombre del perro: ")
        self.Peso = float(input("Por favor ingrese el peso del perro en KG: "))
        self.Raza = input("Por favor ingrese la raza del perro: ")
        self.Sexo = input("Por favor ingrese el sexo del perro: ")
        self.Edad = int(input("Por favor ingrese la edad del perro (en años): "))
        self.Estado = "No Atendido"
        self.Categoria = ""
        
        if self.Peso >= 10:
            self.Categoria = "Perro Grande"
        elif self.Peso < 10:
            self.Categoria = "Perro Pequeño"
            
    def registrar(self):
        self.Estado = "Atendido"
    
    def Salida(self):
        print("")
        print("*******************SALIDA********************")
        print("El nombre del perro es:", self.Nombre)
        print("El peso de", self.Nombre, "es", self.Peso, "kg")
        print("La raza de", self.Nombre, "es", self.Raza)
        print("La edad de", self.Nombre, "es", self.Edad, "años")
        print("La Categoria designada a", self.Nombre, "es", self.Categoria)
        print("Estado:", self.Estado)
        
        
Datos = VetPerro()
Datos.registrar()
Datos.Salida()
        