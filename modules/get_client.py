import os
import requests
from tabulate import tabulate

BASE_URL = "http://154.38.171.54:5001"


def getAllClient():
    peticion = requests.get(f"{BASE_URL}/cliente")
    data = peticion.json()
    return data



# Funcion para filtrar cliente por nombre
def getAllClientsName():
    clientName = list()
    for val in getAllClient():
        codigoName = dict({
            "Codigo del cliente": val.get('codigo_cliente'),
            "Nombre del cliente": val.get('nombre_cliente')
        })    
        clientName.append(codigoName)
    return clientName

   
# Funcion para filtrar cliente por codigo 
def getOneClientCode(codigo):
    for val in getAllClient():
        if(val.get('codigo_cliente') == codigo):
            return [{
                "codigo de cliente": val.get('codigo_cliente'),
                "nombre del cliente": val.get('nombre_cliente')
            }]

# Funcion para filtrar cliente por limite de credito y ciudad. 
def getAllClientCreditCity(creditLimit, city):
    clientCredit = list()
    for val in getAllClient():
        if(val.get('limite_credito') >= creditLimit and val.get('ciudad') == city):
            clientCredit.append({
                "Codigo del cliente": val.get('codigo_cliente'),
                "Nombre del cliente": val.get('nombre_cliente'),
                "Nombre de contacto": f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Teléfono y fax": f'{val.get("telefono")} / {val.get("fax")}',
                "Dirección completa": f'{val.get("linea_direccion1")} {val.get("linea_direccion2")} , {val.get("codigo_postal")}',
                "Locación": f'{val.get("pais")} - {val.get("region")} - {val.get("ciudad")}',
                "Código Rep ventas": val.get('codigo_empleado_rep_ventas'),
                "Límite de Crédito": val.get('limite_credito'),
            })
    return clientCredit
            
# Funcion para filtrar clientes por representantes de venta
def getAllClientPerSalesRep(codigo):
    clientRep = []
    for val in getAllClient():
        if(val.get('codigo_empleado_rep_ventas') == codigo):
            clientRep.append({
                "Codigo del cliente": val.get('codigo_cliente'),
                "Nombre del cliente": val.get('nombre_cliente'),
                "Nombre de contacto": f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Teléfono y fax": f'{val.get("telefono")} / {val.get("fax")}',
                "Dirección completa": f'{val.get("linea_direccion1")} {val.get("linea_direccion2")} , {val.get("codigo_postal")}',
                "Locación": f'{val.get("pais")} - {val.get("region")} - {val.get("ciudad")}',
                "Código Rep ventas": val.get('codigo_empleado_rep_ventas'),
                "Límite de Crédito": val.get('limite_credito'),
            })
    return clientRep

# Funcion para filtrar clientes por pais, region y ciudad
def getAllClientCountryRegionCity(country, region=None, city=None):
    clientzone = []
    for val in getAllClient():
        if(
            val.get('pais') == country or
            (val.get('region') == region or val.get('region') == None) and 
            (val.get('ciudad') == city or val.get('ciudad') == None)
        ):
            clientzone.append({
                "Codigo del cliente": val.get('codigo_cliente'),
                "Nombre del cliente": val.get('nombre_cliente'),
                "Nombre de contacto": f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Teléfono y fax": f'{val.get("telefono")} / {val.get("fax")}',
                "Dirección completa": f'{val.get("linea_direccion1")} {val.get("linea_direccion2")} , {val.get("codigo_postal")}',
                "Locación": f'{val.get("pais")} - {val.get("region")} - {val.get("ciudad")}',
                "Código Rep ventas": val.get('codigo_empleado_rep_ventas'),
                "Límite de Crédito": val.get('limite_credito'),
            })
    return clientzone



def menu():
    
    while True:
        os.system("clear")
        print(""" 
    

______                            _               _         _____  _  _               _              
| ___ \                          | |             | |       /  __ \| |(_)             | |             
| |_/ /  ___  _ __    ___   _ __ | |_   ___    __| |  ___  | /  \/| | _   ___  _ __  | |_   ___  ___ 
|    /  / _ \| '_ \  / _ \ | '__|| __| / _ \  / _` | / _ \ | |    | || | / _ \| '_ \ | __| / _ \/ __|
| |\ \ |  __/| |_) || (_) || |   | |_ |  __/ | (_| ||  __/ | \__/\| || ||  __/| | | || |_ |  __/\__ 
\_| \_| \___|| .__/  \___/ |_|    \__| \___|  \__,_| \___|  \____/|_||_| \___||_| |_| \__| \___||___/
             | |                                                                                     
             |_|                                                                                     

        0. Regresar al menu anterior
        1. Buscar cliente por nombre (codigo y nombre)
        2. Buscar cliente por codigo (codigo y nombre)
        3. Filtrar clientes por limite de credito y ciudad (ejem: 3000.0, San Francisco)
        4. Buscar clientes por representante de ventas
        5. Buscar clientes por pais, region y ciudad
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllClientsName(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 2):
            codigoDelCliente = int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClientCode(codigoDelCliente),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 3):
            ciudadCliente = input("Ingrese la ciudad que desea revisar: ")
            limiteCredito = float(input("Ingrese el limite de credito minimo a revisar: "))
            print(tabulate(getAllClientCreditCity(limiteCredito, ciudadCliente),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 4):
            codigoRep = int(input("Ingrese el codigo del representante de ventas: "))
            print(tabulate(getAllClientPerSalesRep(codigoRep),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 5):
            pais = input("Ingrese el pais que desea revisar: ")
            region = input("Ingrese la region que desea revisar (opcional): ")
            ciudad = input("Ingrese la ciudad que desea revisar (opcional): ")
            print(tabulate(getAllClientCountryRegionCity(pais, region, ciudad),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break
        input("Presion ENTER para volver al menu....")









    



