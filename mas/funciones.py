import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verify_opc(enunciado,bajo,arriba):
    while True:
        try: 
            opcion=int(input(enunciado))
            if opcion >=bajo and opcion<=arriba:
                return opcion
            else:
                print(f"")
        except ValueError:
            print("Por favor, digite un numero valido")