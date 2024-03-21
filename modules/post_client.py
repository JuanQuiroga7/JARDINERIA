import os
import re
from tabulate import tabulate
import json
import requests
import modules.get_client as gC

BASE_URL = "http://154.38.171.54:5001"


# Funcion para guardar un cliente nuevo
def postClient():
    cliente = dict()
    while True:
        try:
            # Validar que el codigo del cliente sea un número de 1 a 5 dígitos
            if(not cliente.get("codigo_cliente")):
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^\d{1,5}$', codigo) is not None):
                    data = gC.getClientCode(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo de cliente ya existe")
                    else:
                        cliente["codigo_cliente"] = int(codigo)
                else:
                    raise Exception("El codigo ingresado no cumple con los estandares")

            # Validar que el nombre del cliente cumpla con la estructura adecuada
            if(not cliente.get("nombre_cliente")):
                nombre = input("Ingrese el nombre del cliente: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', nombre) is not None):
                    cliente["nombre_cliente"] = nombre
                else:
                    raise Exception("El nombre ingresado no cumple con los estandares")

            # Validar que el nombre del contacto cumpla con la estructura adecuada
            if(not cliente.get("nombre_contacto")):
                nombre_contacto = input("Ingrese el nombre del contacto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', nombre_contacto) is not None):
                    cliente["nombre_contacto"] = nombre_contacto
                else:
                    raise Exception("El nombre del contacto no cumple con los estandares")

            # Validar que el apellido del contacto cumpla con la estructura adecuada
            if(not cliente.get("apellido_contacto")):
                apellido_contacto = input("Ingrese el apellido del contacto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', apellido_contacto) is not None):
                    cliente["apellido_contacto"] = apellido_contacto
                else:
                    raise Exception("El apellido del contacto no cumple con los estandares")

            # Validar que el telefono cumpla con la estructura adecuada
            if(not cliente.get("telefono")):
                telefono = input("Ingrese el telefono del cliente: ")
                if(re.match(r'^\d{11}$', telefono) is not None):
                    cliente["telefono"] = telefono
                else:
                    raise Exception("El telefono ingresado no cumple con los estandares")

            # Validar que el fax cumpla con la estructura adecuada
            if(not cliente.get("fax")):
                fax = input("Ingrese el fax del cliente: ")
                if(re.match(r'^\d{11}$', fax) is not None):
                    cliente["fax"] = fax
                else:
                    raise Exception("El fax ingresado no cumple con los estandares")

            # Validar que la linea de direccion1 cumpla con la estructura adecuada
            if(not cliente.get("linea_direccion1")):
                direccion1 = input("Ingrese la linea de direccion 1 del cliente: ")
                if(re.match(r'^[A-Za-z0-9\s]+$', direccion1) is not None):
                    cliente["linea_direccion1"] = direccion1
                else:
                    raise Exception("La linea de direccion 1 no cumple con los estandares")

            # Validar que la linea de direccion2 cumpla con la estructura adecuada
            if(not cliente.get("linea_direccion2")):
                direccion2 = input("Ingrese la linea de direccion 2 del cliente: ")
                if(re.match(r'^[A-Za-z0-9\s]+$', direccion2) is not None):
                    cliente["linea_direccion2"] = direccion2
                else:
                    raise Exception("La linea de direccion 1 no cumple con los estandares")
                
            # Validar que la ciudad cumpla con la estructura adecuada
            if(not cliente.get("ciudad")):
                ciudad = input("Ingrese la ciudad del cliente: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', ciudad) is not None):
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception("La ciudad ingresada no cumple con los estandares")
                
            # Validar que la region cumpla con la estructura adecuada
            if(not cliente.get("region")):
                region = input("Ingrese la region del cliente: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', region) is not None):
                    cliente["region"] = region
                else:
                    raise Exception("La ciudad ingresada no cumple con los estandares")

            # Validar que el pais cumpla con la estructura adecuada
            if(not cliente.get("pais")):
                pais = input("Ingrese el pais del cliente: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', pais) is not None):
                    cliente["pais"] = pais
                else:
                    raise Exception("El pais ingresado no cumple con los estandares")

            # Validar que el codigo postal cumpla con la estructura adecuada
            if(not cliente.get("codigo_postal")):
                codigo_postal = input("Ingrese el codigo postal del cliente: ")
                if(re.match(r'^\d{4,6}$', codigo_postal) is not None):
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception("El codigo postal ingresado no cumple con los estandares")

            # Validar que el codigo del empleado de ventas sea un número de 2 dígitos
            if(not cliente.get("codigo_empleado_rep_ventas")):
                codigo_empleado = input("Ingrese el codigo del empleado de ventas: ")
                if(re.match(r'^\d{2}$', codigo_empleado) is not None):
                    cliente["codigo_empleado_rep_ventas"] = int(codigo_empleado)
                else:
                    raise Exception("El codigo del empleado de ventas ingresado no cumple con los estandares")

            # Validar que el limite de credito sea un número
            if(not cliente.get("limite_credito")):
                limite_credito = input("Ingrese el limite de credito del cliente: ")
                if(re.match(r'^\d+$', limite_credito) is not None):
                    cliente["limite_credito"] = int(limite_credito)
                    break
                else:
                    raise Exception("El limite de credito ingresado no cumple con los estandares")

        except Exception as error:
            print(error)
    print(cliente)

    peticion = requests.post(f"{BASE_URL}/cliente", data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Guardado"
    return [res]


# Funcion para eliminar un producto
def deleteClient(id):
    data = gC.getClientId(id)
    if(len(data)):
        peticion = requests.delete(f"{BASE_URL}/cliente/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "cliente eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"cliente no encontrado",
                "id": id
            }],
            "status": 400,
        }


# Funcion para modificar un producto
def EditClient(id):
    data = gC.getClientId(id)
    if data is None:
        print(f"El cliente con ID {id} no existe")
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
        if modificacion == "codigo_cliente" or modificacion == "codigo_empleado_rep_ventas" or modificacion == "limite_credito":
            nuevo_valor = int(nuevo_valor)
        if modificacion in data[0]:
            data[0][modificacion] = nuevo_valor
        else:
            print(f"\nEl campo {modificacion} no existe")

    peticion = requests.put(f"{BASE_URL}/cliente/{id}", data=json.dumps(data[0]))
    res = peticion.json()
    res["Mensaje"] = "Cliente Modificado"
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
        1. Guardar un cliente nuevo
        2. Modificar un cliente
        3. Eliminar un cliente
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postClient(),headers= "keys", tablefmt="rounded_grid"))
        if (opcion == 2):
            id = input("Ingrese el ID del producto que desea modificar: ")
            print(tabulate(EditClient(id), headers="keys", tablefmt="rounded_grid"))
        if(opcion == 3):
            id = input("Ingrese el ID del producto que desea eliminar: ")
            print(tabulate(deleteClient(id),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

        input("Presione ENTER para continuar.....")