import os
from tabulate import tabulate
import json
import requests

def postProduct(producto):
    
    producto = {
                "codigo_producto": input("Ingrese el codigo del producto: "),
                "nombre": input("Ingrese el codigo del producto: "),
                "gama": input("Ingrese el codigo del producto: "),
                "dimensiones": input("Ingrese el codigo del producto: "),
                "proveedor": input("Ingrese el codigo del producto: "),
                "descripcion": input("Ingrese el codigo del producto: "),
                "cantidad_en_stock": input("Ingrese el codigo del producto: "),
                "precio_venta": input("Ingrese el codigo del producto: "),
                "precio_proveedor": input("Ingrese el codigo del producto: "),
            },
    
    peticion = requests.post("http://172.16.106.152:5432", data=json.dumbps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



def menu():
    
    while True:
        os.system("clear")
        print(""" 
    

___  ___            _  _   __  _                     ______         _               
|  \/  |           | |(_) / _|(_)                    |  _  \       | |              
| .  . |  ___    __| | _ | |_  _   ___   __ _  _ __  | | | |  __ _ | |_   ___   ___ 
| |\/| | / _ \  / _` || ||  _|| | / __| / _` || '__| | | | | / _` || __| / _ \ / __|
| |  | || (_) || (_| || || |  | || (__ | (_| || |    | |/ / | (_| || |_ | (_) |\__ 
\_|  |_/ \___/  \__,_||_||_|  |_| \___| \__,_||_|    |___/   \__,_| \__| \___/ |___/
                                                                                    
                                                                                    
                                                                                                                                                                                  

        0. Atras 
        1. Guardar un producto nuevo
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postProduct(),headers= "keys", tablefmt="rounded_grid"))
            input("Presione una tecla para continuar.....")
        elif(opcion == 0):
            break