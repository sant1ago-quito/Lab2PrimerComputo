# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:42:44 2024

@author: Admin
"""
"""

Este programa permite al usuario agregar hasta 5 tareas a una lista y luego muestra todas las tareas ingresadas :D

1. Clase TareasPendientes: Define una lista para almacenar las tareas.

2. Método obtenernombre: Este lo añadí para darle un mejor toque al código al ser personalizado permitiendo la entrada de datos del usuario como su nombre.  

3. Método agregar_tareas: Usa un bucle while para pedir al usuario que ingrese tareas. El bucle se repite 5 veces, añadiendo cada tarea a la lista.

4. Método mostrar_tareas: Imprime la lista de tareas que el usuario ha ingresado.

Este programa facilita la organización de tareas al permitir que el usuario ingrese una lista de hasta 5 tareas pendientes y las visualice todas juntas, ideal para una gestión sencilla de actividades.

"""

class TareasPendientes:
    def __init__(self):
        self.tareas = []

    def obtenernombre(self):
        print("****************************BIENVENIDO***************")
        print("")
        self.nombre = input("Hola, por favor escribe tu nombre :D \nNombre: ")
        print("")
    def agregar_tareas(self):
        i = 0
        while i < 5:
            tarea = input(f"Por favor ingresa la tarea {i + 1}: ")
            self.tareas.append(tarea)
            i += 1
            print(f"Tarea '{tarea}' agregada =)")
    
    def mostrar_tareas(self):
        print("")
        print("******************************************************")
        print(f"{self.nombre}, esta es tu lista de tareas Pendientes =( ")
        print("")
        for tarea in self.tareas:
            print(f"- {tarea}")
        print("********************************************************")
        
mis_tareas = TareasPendientes()

mis_tareas.obtenernombre()
mis_tareas.agregar_tareas()
mis_tareas.mostrar_tareas()

