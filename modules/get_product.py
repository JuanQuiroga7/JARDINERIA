import os
import requests
from tabulate import tabulate




def getAllData():
    peticion = requests.get("http://172.16.106.152:5432")
    data = peticion.json()
    return data



# Funcion para filtrar producto por gama, stock y precio de venta de mayor a menor
def getAllGamaStockPrice(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    
    def priceOrder(val):
        return val.get("precio_venta")
    condiciones.sort(key=priceOrder, reverse=True)
    for i, val in enumerate(condiciones):
        if(condiciones[i].get("descripcion")):
            condiciones[i]["descripcion"] = f'{condiciones[i]["descripcion"][:5]}...'      
            condiciones[i] = {
                "Codigo": val.get("codigo_producto"),
                "Nombre": val.get("nombre"),
                "Gama": val.get("gama"),
                "Dimensiones": val.get("dimensiones"),
                "Proveedor": val.get("proveedor"),
                "Descripcion": val.get("descripcion"),
                "Stock": val.get("cantidad_en_stock"),
                "Precio venta": val.get("precio_venta"),
                "Precio base": val.get("precio_proveedor"),
            }
    return condiciones


def menu():
    
    while True:
        os.system("clear")
        print(""" 
    

______                            _               _        ______                   _               _               
| ___ \                          | |             | |       | ___ \                 | |             | |              
| |_/ /  ___  _ __    ___   _ __ | |_   ___    __| |  ___  | |_/ / _ __   ___    __| | _   _   ___ | |_   ___   ___ 
|    /  / _ \| '_ \  / _ \ | '__|| __| / _ \  / _` | / _ \ |  __/ | '__| / _ \  / _` || | | | / __|| __| / _ \ / __|
| |\ \ |  __/| |_) || (_) || |   | |_ |  __/ | (_| ||  __/ | |    | |   | (_) || (_| || |_| || (__ | |_ | (_) |\__ 
\_| \_| \___|| .__/  \___/ |_|    \__| \___|  \__,_| \___| \_|    |_|    \___/  \__,_| \__,_| \___| \__| \___/ |___/
             | |                                                                                                    
             |_|                                                                                                    
                                                                                    

        0. Atras
        1. Buscar productos filtrando por gama y cantida minima en stock (Se detalla precio de venta de mayor a menor)
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            gama = input("Ingrese la gama del producto: ")
            stock = int(input("Ingrese cantidad minima en stock a revisar: "))
            print(tabulate(getAllGamaStockPrice(gama, stock),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

