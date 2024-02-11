import os
import json

while True :
    seguimiento_academico = int(input("""
    Bienvenido a CampusLands,elige tu rol
    (1) Coordinador
    (2) Trainer
    (3) Salir
    """))
    
    if seguimiento_academico == 1:
        print("-----------------------")
        print("Bienvenido Coordinador")
        print("------------------------")
        print(" 1. Asignar Notas")
        print(" 2. Asignar Campers")
        print(" 3. Asignar Trainers")
        print(" 4. Asignar Ruta")
        print(" 5. Fecha de inicio")
        print(" 6. Fecha de Finalizacion")
        print(" 7. Salon de Entrenamiento")
    elif seguimiento_academico == 2:
        print("------------------")
        print("Trainer")
        print("-------------------")
        print(" 1. Mirar Horario")
    else:
        break     