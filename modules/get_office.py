import os
import requests
from tabulate import tabulate

BASE_URL = "http://154.38.171.54:5005"


def getAllData():
    peticion = requests.get(f"{BASE_URL}/oficinas")
    data = peticion.json()
    return data

def getOfficeId(codigo):
    for val in getAllData():
        if(val.get("id") == codigo):
            return [val]
        
def getOfficeCode(codigo):
    for val in getAllData():
        if(val.get("codigo_oficina") == codigo):
            return [val]
        

# Funcion para filtrar oficinas por ciudad 
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in getAllData(): 
        codigoCiudad.append({
            "Codigo": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad")
        })
    return codigoCiudad 


# Funcion para filtrar informacion de oficinas por pais
def getAllPhonesCity(pais):
    phonesCity = []
    for val in getAllData():
        if(val.get("pais") == pais ):
            phonesCity.append({
            "Telefono": val.get("telefono"),
            "Ciudad": val.get("ciudad"),
            "Oficina": val.get("codigo_oficina"),
            "Pais": val.get("pais")
        })
    return phonesCity


def menu():

    while True:
        os.system("clear")
        print(""" 
    

______                            _               _         _____   __  _        _                    
| ___ \                          | |             | |       |  _  | / _|(_)      (_)                   
| |_/ /  ___  _ __    ___   _ __ | |_   ___    __| |  ___  | | | || |_  _   ___  _  _ __    __ _  ___ 
|    /  / _ \| '_ \  / _ \ | '__|| __| / _ \  / _` | / _ \ | | | ||  _|| | / __|| || '_ \  / _` |/ __|
| |\ \ |  __/| |_) || (_) || |   | |_ |  __/ | (_| ||  __/ \ \_/ /| |  | || (__ | || | | || (_| |\__ 
\_| \_| \___|| .__/  \___/ |_|    \__| \___|  \__,_| \___|  \___/ |_|  |_| \___||_||_| |_| \__,_||___/
             | |                                                                                      
             |_|                                                                                      
                                                                              

        0. Regresar al menu anterior
        1. Filtrar oficinas por ciudad (Codigo y ciudad)
        2. Buscar oficinas por pais 
        
""")

        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllCodigoCiudad(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 2):
            pais = input("Ingrese el pais para revisar telefono de oficinas: ")
            print(tabulate(getAllPhonesCity(pais),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break
        input("Presione ENTER para continuar.....")

