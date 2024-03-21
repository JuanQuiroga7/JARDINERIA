import os
import re
from tabulate import tabulate
import json
import requests
import modules.get_payment as gP

BASE_URL = "http://154.38.171.54:5006"


def postPayment():
    pago = dict()
    while True:
        try:
            # Validar que el codigo del cliente sea un número
            if(not pago.get("codigo_cliente")):
                codigo_cliente = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^\d+$', codigo_cliente) is not None):
                    pago["codigo_cliente"] = int(codigo_cliente)
                else:
                    raise Exception("El codigo del cliente ingresado no cumple con los estandares")

            # Validar que la forma de pago cumpla con la estructura adecuada
            if(not pago.get("forma_pago")):
                forma_pago = input("Ingrese la forma de pago: ")
                if(re.match(r'^[A-Za-z0-9\s]+$', forma_pago) is not None):
                    pago["forma_pago"] = forma_pago
                else:
                    raise Exception("La forma de pago ingresada no cumple con los estandares")

            # Validar que el id de la transaccion cumpla con la estructura adecuada
            if(not pago.get("id_transaccion")):
                id_transaccion = input("Ingrese el id de la transaccion: ")
                if(re.match(r'^[a-z]{2}-[a-z]{3}-\d{6}$', id_transaccion) is not None):
                    pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception("El id de la transaccion ingresado no cumple con los estandares")

            # Validar que la fecha de pago cumpla con la estructura adecuada
            if(not pago.get("fecha_pago")):
                fecha_pago = input("Ingrese la fecha de pago (YYYY-MM-DD): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_pago) is not None):
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception("La fecha de pago ingresada no cumple con los estandares")

            # Validar que el total sea un número
            if(not pago.get("total")):
                total = input("Ingrese el total del pago: ")
                if(re.match(r'^\d+$', total) is not None):
                    pago["total"] = int(total)
                    break
                else:
                    raise Exception("El total ingresado no cumple con los estandares")

        except Exception as error:
            print(error)
    print(pago)

    peticion = requests.post(f"{BASE_URL}/pagos", data=json.dumps(pago))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]



# Funcion para eliminar un producto
def deletePayment(id):
    data = gP.getPaymentId(id)
    if(len(data)):
        peticion = requests.delete(f"{BASE_URL}/pagos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "pago eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"pago no encontrado",
                "id": id
            }],
            "status": 400,
        }




# Funcion para modificar un producto
def EditPayment(id):
    data = gP.getPaymentId(id)
    if data is None:
        print(f"El pago con ID {id} no existe")
        return    
    
    while True:
        os.system("clear")
        
        print(tabulate(data, headers="keys", tablefmt="pretty"))
        keys = list(data[0].keys())
        for i, key in enumerate(keys, start=1):
            print(f"\n{i}. {key}")
        modificacion = input("\nIngrese el numero del campo que desea modificar (Escriba listo para finalizar): ")
        if modificacion == "1":
            print("\nNo se puede modificar el ID")
            continue
        if modificacion.lower() == "listo":
            break
        modificacion = keys[int(modificacion) - 1]
        nuevo_valor = input(f"\nIngrese el nuevo valor para {modificacion}: ")
        if modificacion == "codigo_cliente" or modificacion == "total":
            nuevo_valor = int(nuevo_valor)
        if modificacion in data[0]:
            data[0][modificacion] = nuevo_valor
        else:
            print(f"\nEl campo {modificacion} no existe")

    peticion = requests.put(f"{BASE_URL}/pagos/{id}", data=json.dumps(data[0]))
    res = peticion.json()
    res["Mensaje"] = "Pago Modificado"
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
        1. Guardar un pago nuevo
        2. Modificar un pago
        3. Eliminar un pago
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postPayment(),headers= "keys", tablefmt="rounded_grid"))
        if (opcion == 2):
            id = input("Ingrese el ID del pago que desea modificar: ")
            print(tabulate(EditPayment(id), headers="keys", tablefmt="rounded_grid"))
        if(opcion == 3):
            id = input("Ingrese el ID del pago que desea eliminar: ")
            print(tabulate(deletePayment(id),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

        input("Presione ENTER para continuar.....")
