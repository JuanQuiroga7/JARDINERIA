import os
import re
from tabulate import tabulate
import json
import requests
import modules.get_employee as gE

BASE_URL = "http://154.38.171.54:5003"

def postEmployee():
    empleado = dict()
    while True:
        try:
            # Validar que el codigo del empleado sea un número
            if(not empleado.get("codigo_empleado")):
                codigo = input("Ingrese el codigo del empleado: ")
                if(re.match(r'^\d+$', codigo) is not None):
                    data = gE.getEmployeeCode(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo de empleado ya existe")
                    else:
                        empleado["codigo_empleado"] = int(codigo)
                else:
                    raise Exception("El codigo ingresado no cumple con los estandares")

            # Validar que el nombre cumpla con la estructura adecuada
            if(not empleado.get("nombre")):
                nombre = input("Ingrese el nombre del empleado: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', nombre) is not None):
                    empleado["nombre"] = nombre
                else:
                    raise Exception("El nombre ingresado no cumple con los estandares")

            # Validar que el apellido1 cumpla con la estructura adecuada
            if(not empleado.get("apellido1")):
                apellido1 = input("Ingrese el primer apellido del empleado: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', apellido1) is not None):
                    empleado["apellido1"] = apellido1
                else:
                    raise Exception("El primer apellido ingresado no cumple con los estandares")

            # Validar que el apellido2 cumpla con la estructura adecuada
            if(not empleado.get("apellido2")):
                apellido2 = input("Ingrese el segundo apellido del empleado: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', apellido2) is not None):
                    empleado["apellido2"] = apellido2
                else:
                    raise Exception("El segundo apellido ingresado no cumple con los estandares")

            # Validar que la extension cumpla con la estructura adecuada
            if(not empleado.get("extension")):
                extension = input("Ingrese la extension del empleado: ")
                if(re.match(r'^\d{4}$', extension) is not None):
                    empleado["extension"] = extension
                else:
                    raise Exception("La extension ingresada no cumple con los estandares")

            # Validar que el email cumpla con la estructura adecuada
            if(not empleado.get("email")):
                email = input("Ingrese el email del empleado: ")
                if(re.match(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$', email) is not None):
                    empleado["email"] = email
                else:
                    raise Exception("El email ingresado no cumple con los estandares")

            # Validar que el codigo de la oficina cumpla con la estructura adecuada
            if(not empleado.get("codigo_oficina")):
                codigo_oficina = input("Ingrese el codigo de la oficina del empleado: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{2}$', codigo_oficina) is not None):
                    empleado["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception("El codigo de la oficina ingresado no cumple con los estandares")
                
            # Validar que el codigo del jefe cumpla con la estructura adecuada
            if(not empleado.get("codigo_jefe")):
                codigo_jefe = input("Ingrese el codigo del jefe: ")
                if(re.match(r'^\d+$', codigo_jefe) is not None):
                    empleado["codigo_jefe"] = int(codigo_jefe)
                else:
                    raise Exception("El codigo del jefe ingresado no cumple con los estandares")

            # Validar que el puesto cumpla con la estructura adecuada
            if(not empleado.get("puesto")):
                puesto = input("Ingrese el puesto del empleado: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', puesto) is not None):
                    empleado["puesto"] = puesto
                    break
                else:
                    raise Exception("El puesto ingresado no cumple con los estandares")

        except Exception as error:
            print(error)
    print(empleado)

    peticion = requests.post(f"{BASE_URL}/empleados", data=json.dumps(empleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

# Funcion para eliminar un empleado
def deleteEmployee(id):
    data = gE.getEmployeeId(id)
    if(len(data)):
        peticion = requests.delete(f"{BASE_URL}/empleados/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "empleado eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"empleado no encontrado",
                "id": id
            }],
            "status": 400,
        }


# Funcion para modificar un empleado
def EditProduct(id):
    data = gE.getEmployeeId(id)
    if data is None:
        print(f"El empleado con ID {id} no existe")
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
        if modificacion == "codigo_empleado" or modificacion == "codigo_jefe":
            nuevo_valor = int(nuevo_valor)
        if modificacion in data[0]:
            data[0][modificacion] = nuevo_valor
        else:
            print(f"\nEl campo {modificacion} no existe")

    peticion = requests.put(f"{BASE_URL}/empleados/{id}", data=json.dumps(data[0]))
    res = peticion.json()
    res["Mensaje"] = "Empleado Modificado"
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
        1. Guardar un empleado nuevo
        2. Modificar un empleado
        3. Eliminar un empleado
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postEmployee(),headers= "keys", tablefmt="rounded_grid"))
        if (opcion == 2):
            id = input("Ingrese el ID del empleado que desea modificar: ")
            print(tabulate(EditProduct(id), headers="keys", tablefmt="rounded_grid"))
        if(opcion == 3):
            id = input("Ingrese el ID del empleado que desea eliminar: ")
            print(tabulate(deleteEmployee(id),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

        input("Presione ENTER para continuar.....")
