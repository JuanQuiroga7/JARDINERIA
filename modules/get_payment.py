import os
import requests
from tabulate import tabulate

BASE_URL = "http://154.38.171.54:5006"


def getAllData():
    peticion = requests.get(f"{BASE_URL}/pagos")
    data = peticion.json()
    return data

# Funcion para filtrar pagos por metodo, año y organizar el total del pago de mayor a menor
def getAllPaymentYear(metodo, year):
    paymentYear = []
    for val in getAllData():
        if val.get("forma_pago") == metodo and year in val.get("fecha_pago"):
            paymentYear.append(val)   
    paymentYear = sorted(paymentYear, key=lambda x: x['total'], reverse=True)        
    return paymentYear

# Funcion para filtrar pagos por metodo
def getAllPaymentMethods():
    payMeth = set()
    for val in getAllData():
        if val.get("forma_pago") in ["PayPal", "Transferencia", "Cheque"]:
            payMeth.add(val.get("forma_pago"))
    return [{"Metodo de pago": metodo} for metodo in payMeth]


def menu():
    
    while True:
        os.system("clear")
        print(""" 
    
              
______                            _               _        ______                           
| ___ \                          | |             | |       | ___ \                          
| |_/ /  ___  _ __    ___   _ __ | |_   ___    __| |  ___  | |_/ /  __ _   __ _   ___   ___ 
|    /  / _ \| '_ \  / _ \ | '__|| __| / _ \  / _` | / _ \ |  __/  / _` | / _` | / _ \ / __|
| |\ \ |  __/| |_) || (_) || |   | |_ |  __/ | (_| ||  __/ | |    | (_| || (_| || (_) |\__ 
\_| \_| \___|| .__/  \___/ |_|    \__| \___|  \__,_| \___| \_|     \__,_| \__, | \___/ |___/
             | |                                                           __/ |            
             |_|                                                          |___/             
                                                                                                   
                                                                                    

        0. Atras
        1. Buscar pagos filtrando por metodo de pago, año y total de pago (de mayor a menor)
        2. Buscar pagos filtrando por metodo de pago
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            metodo = input("Ingrese el metodo de pago: (PayPal, Transferencia, Cheque) ")
            year = input("Ingrese el año a revisar: ")
            print(tabulate(getAllPaymentYear(metodo, year),headers= "keys", tablefmt="rounded_grid"))
        if(opcion == 2):
            print(tabulate(getAllPaymentMethods(),headers= "keys", tablefmt="rounded_grid"))   
        elif(opcion == 0):
            break
        input("Presion ENTER para volver al menu....")

    