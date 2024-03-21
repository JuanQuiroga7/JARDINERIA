import os
import requests
from datetime import datetime
from tabulate import tabulate

BASE_URL = "http://154.38.171.54:5007"


def getAllData():
    peticion = requests.get(f"{BASE_URL}/pedidos")
    data = peticion.json()
    return data

def getPedidoId(codigo):
    for val in getAllData():
        if(val.get("id") == codigo):
            return [val]
        
def getPedidoCode(codigo):
    for val in getAllData():
        if(val.get("codigo_pedido") == codigo):
            return [val]



# Funcion para filtrar estado de pedidos
def getAllOrderSteps():
    orSteps = set()
    for val in getAllData():
        if val.get("estado") in ["Pendiente", "Entregado", "Rechazado"]:
            orSteps.add(val.get("estado"))
    return [{"estado del pedido": estado} for estado in orSteps]

# Funcion para filtrar pedidos entregados tarde
def getAllDelayOrders():
    pedidoEntregado = []
    for val in getAllData():
        if val.get("estado") == "Entregado" and val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidoEntregado.append({
                    "Codigo_Pedido": val.get("codigo_pedido"),
                    "Codigo_Cliente": val.get("codigo_cliente"),
                    "Fecha_Esperada": val.get("fecha_esperada"),
                    "fechaEntregada": val.get("fechaEntrega")
                })
    return pedidoEntregado


# Funcion para filtrar pedidos entregados al menos dos dias antes de la fecha esperada
def getAllEarlyOrders():
    pedidoEntregado = []
    for val in getAllData():
        if val.get("estado") == "Entregado" and val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days > 1):
                pedidoEntregado.append({
                    "Codigo_Pedido": val.get("codigo_pedido"),
                    "Codigo_Cliente": val.get("codigo_cliente"),
                    "Fecha_Esperada": val.get("fecha_esperada"),
                    "fechaEntregada": val.get("fechaEntrega")
                })
    return pedidoEntregado


# Funcion para filtrar pedidos rechazados en 2009 o fecha por definir
def getAllDeniedOrders(year):
    deniedOrder = []
    for val in getAllData():
        if val.get("estado") == "Rechazado" and year in val.get("fecha_pedido"):
            deniedOrder.append(val)
    return deniedOrder


# Funcion para filtrar todos los pedidos entregados en mes de Enero
def getAllShippedOrderMonth(month):
    shippedOrder = []
    for val in getAllData():
        if val.get("estado") == "Entregado" and val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado" and val.get("fechaEntrega").split("-")[1] == month:
            shippedOrder.append(val)
    return shippedOrder


def menu():

    while True:
        print(""" 
    

______                            _               _        ______            _  _      _             
| ___ \                          | |             | |       | ___ \          | |(_)    | |            
| |_/ /  ___  _ __    ___   _ __ | |_   ___    __| |  ___  | |_/ /  ___   __| | _   __| |  ___   ___ 
|    /  / _ \| '_ \  / _ \ | '__|| __| / _ \  / _` | / _ \ |  __/  / _ \ / _` || | / _` | / _ \ / __|
| |\ \ |  __/| |_) || (_) || |   | |_ |  __/ | (_| ||  __/ | |    |  __/| (_| || || (_| || (_) |\__ 
\_| \_| \___|| .__/  \___/ |_|    \__| \___|  \__,_| \___| \_|     \___| \__,_||_| \__,_| \___/ |___/
             | |                                                                                     
             |_|                                                                                     
                                                                                     

        0. Regresar al menu anterior
        1. Filtrar estado de todos los pedidos
        2. Filtrar todos los pedidos entregados a destiempo
        3. Filtrar pedidos entregados al menos dos dias antes de la fecha esperada
        4. Filtrar pedidos rechazados por año
        5. Filtrar pedidos entregados por mes
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllOrderSteps(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 2):
            print(tabulate(getAllDelayOrders(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 3):
            print(tabulate(getAllEarlyOrders(),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 4):
            year = (input("Ingrese el año a filtrar: "))
            print(tabulate(getAllDeniedOrders(year),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 5):
            month = input("Ingrese el mes a filtrar: (01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12)")
            print(tabulate(getAllShippedOrderMonth(month),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break
        input("Presion ENTER para volver al menu....")
