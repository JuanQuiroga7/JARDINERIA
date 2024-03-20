import os
import requests
from tabulate import tabulate

BASE_URL = "http://154.38.171.54:5003"


def getAllData():
    peticion = requests.get(f"{BASE_URL}/empleados")
    data = peticion.json()
    return data


# Funcion para filtrar informacion de empleados de jefe (X)
def getAllNameEmailEmployees(codigo):
    infoEmpleado = []
    for val in getAllData():
        if(val.get("codigo_jefe") == codigo):
            infoEmpleado.append({
                "Nombre": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Email": val.get("email"),
                "Jefe": val.get("codigo_jefe")
            })
    return infoEmpleado

# Funcion para filtrar informacion del jefe de la empresa
def getBossDetails():
    infoBoss = []
    for val in getAllData():
        if val.get("codigo_jefe") is None:
            infoBoss.append(val)
    return infoBoss

# Funcion para filtrar puestos diferentes a Representantes de venta
def getNonSalesRepInfo():
    infoemp = []
    for val in getAllData():
        if(val.get("puesto") != ("Representante Ventas")):
            infoemp.append({
                "Nombres": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Puesto": val.get("puesto")
            })
    return infoemp


def menu():
    
    while True:
        os.system("clear")
        print(""" 
    

______                            _               _         _____                    _                   _             
| ___ \                          | |             | |       |  ___|                  | |                 | |            
| |_/ /  ___  _ __    ___   _ __ | |_   ___    __| |  ___  | |__   _ __ ___   _ __  | |  ___   __ _   __| |  ___   ___ 
|    /  / _ \| '_ \  / _ \ | '__|| __| / _ \  / _` | / _ \ |  __| | '_ ` _ \ | '_ \ | | / _ \ / _` | / _` | / _ \ / __|
| |\ \ |  __/| |_) || (_) || |   | |_ |  __/ | (_| ||  __/ | |___ | | | | | || |_) || ||  __/| (_| || (_| || (_) |\__ 
\_| \_| \___|| .__/  \___/ |_|    \__| \___|  \__,_| \___| \____/ |_| |_| |_|| .__/ |_| \___| \__,_| \__,_| \___/ |___/
             | |                                                             | |                                       
             |_|                                                             |_|                                       
                                                                                    

        0. Regresar al menu anterior
        1. Buscar lista de empleados por jefe
        2. Mostrar informacion de jefe de la empresa
        3. Filtrar empleados con puesto diferente a representante de ventas
       
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            codigoJefeEM = int(input("Ingrese el codigo de jefe: "))
            print(tabulate(getAllNameEmailEmployees(codigoJefeEM),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 2):
            print(tabulate(getBossDetails(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 3):
            print(tabulate(getNonSalesRepInfo(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break
        input("Presione ENTER para continuar.....")