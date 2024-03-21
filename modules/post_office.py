import os
import re
from tabulate import tabulate
import json
import requests
import modules.get_office as gO

BASE_URL = "http://154.38.171.54:5005"

def postOffice():

    oficina = dict()
    while True:
        try:
            # Validar que el codigo de la oficina cumpla con la estructura adecuada
            if(not oficina.get("codigo_oficina")):
                codigo = input("Ingrese el codigo de la oficina: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigo) is not None):
                    data = gO.getOfficeCode(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo de oficina ya existe")
                    else:
                        oficina["codigo_oficina"] = codigo
                else:
                    raise Exception("El codigo ingresado no cumple con los estandares")

            # Validar que la ciudad cumpla con la estructura adecuada
            if(not oficina.get("ciudad")):
                ciudad = input("Ingrese la ciudad de la oficina: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', ciudad) is not None):
                    oficina["ciudad"] = ciudad
                else:
                    raise Exception("La ciudad ingresada no cumple con los estandares")

            # Validar que el pais cumpla con la estructura adecuada
            if(not oficina.get("pais")):
                pais = input("Ingrese el pais de la oficina: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', pais) is not None):
                    oficina["pais"] = pais
                else:
                    raise Exception("El pais ingresado no cumple con los estandares")

            # Validar que el codigo postal cumpla con la estructura adecuada
            if(not oficina.get("codigo_postal")):
                codigo_postal = input("Ingrese el codigo postal de la oficina: ")
                if(re.match(r'^\d{4,6}$', codigo_postal) is not None):
                    oficina["codigo_postal"] = codigo_postal
                else:
                    raise Exception("El codigo postal ingresado no cumple con los estandares")

            # Validar que el telefono cumpla con la estructura adecuada
            if(not oficina.get("telefono")):
                telefono = input("Ingrese el telefono de la oficina: ")
                if(re.match(r'^\+\d{2}\s\d{2,3}\s\d{4,7}$', telefono) is not None):
                    oficina["telefono"] = telefono
                else:
                    raise Exception("El telefono ingresado no cumple con los estandares")

            # Validar que la linea de direccion1 cumpla con la estructura adecuada
            if(not oficina.get("linea_direccion1")):
                direccion1 = input("Ingrese la linea de direccion 1 de la oficina: ")
                if(re.match(r'^[A-Za-z0-9\s,]+$', direccion1) is not None):
                    oficina["linea_direccion1"] = direccion1
                else:
                    raise Exception("La linea de direccion 1 no cumple con los estandares")

            # Validar que la linea de direccion2 cumpla con la estructura adecuada
            if(not oficina.get("linea_direccion2")):
                direccion2 = input("Ingrese la linea de direccion 2 de la oficina (si existe): ")
                if direccion2 == "" or re.match(r'^[A-Za-z0-9\s,]+$', direccion2) is not None:
                    oficina["linea_direccion2"] = direccion2 if direccion2 != "" else None
                else:
                    raise Exception("La linea de direccion 2 no cumple con los estandares")

            if all(key in oficina for key in ["codigo_oficina", "ciudad", "pais", "codigo_postal", "telefono", "linea_direccion1"]):
                break

        except Exception as error:
            print(error)
    print(oficina)

    peticion = requests.post(f"{BASE_URL}/oficinas", data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]


# Funcion para eliminar una oficina
def deleteOffice(id):
    data = gO.getOfficeId(id)
    if(len(data)):
        peticion = requests.delete(f"{BASE_URL}/oficinas/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Oficina eliminada correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"Oficina no encontrada",
                "id": id
            }],
            "status": 400,
        }


# Funcion para modificar un producto
def EditOffice(id):
    data = gO.getOfficeId(id)
    if data is None:
        print(f"La oficina con ID {id} no existe")
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
        if modificacion in data[0]:
            data[0][modificacion] = nuevo_valor
        else:
            print(f"\nEl campo {modificacion} no existe")

    peticion = requests.put(f"{BASE_URL}/oficinas/{id}", data=json.dumps(data[0]))
    res = peticion.json()
    res["Mensaje"] = "Oficina Modificada"
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
        1. Guardar una oficina nueva
        2. Modificar una oficina
        3. Eliminar una oficina
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postOffice(),headers= "keys", tablefmt="rounded_grid"))
        if (opcion == 2):
            id = input("Ingrese el ID de la oficina que desea modificar: ")
            print(tabulate(EditOffice(id), headers="keys", tablefmt="rounded_grid"))
        if(opcion == 3):
            id = input("Ingrese el ID de la oficina que desea eliminar: ")
            print(tabulate(deleteOffice(id),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

        input("Presione ENTER para continuar.....")
