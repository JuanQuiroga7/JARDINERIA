import os
import re
from tabulate import tabulate
import json
import requests
import modules.get_pedido as gP

BASE_URL = "http://154.38.171.54:5007"


def postPedido():
    pedido = dict()
    while True:
        try:
            # Validar que el codigo del pedido sea un número
            if(not pedido.get("codigo_pedido")):
                codigo = input("Ingrese el codigo del pedido: ")
                if(re.match(r'^\d+$', codigo) is not None):
                    data = gP.getPedidoCode(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo de pedido ya existe")
                    else:
                        pedido["codigo_pedido"] = int(codigo)
                else:
                    raise Exception("El codigo ingresado no cumple con los estandares")

            # Validar que la fecha del pedido cumpla con la estructura adecuada
            if(not pedido.get("fecha_pedido")):
                fecha_pedido = input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_pedido) is not None):
                    pedido["fecha_pedido"] = fecha_pedido
                else:
                    raise Exception("La fecha del pedido ingresada no cumple con los estandares")

            # Validar que la fecha esperada cumpla con la estructura adecuada
            if(not pedido.get("fecha_esperada")):
                fecha_esperada = input("Ingrese la fecha esperada del pedido (YYYY-MM-DD): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_esperada) is not None):
                    pedido["fecha_esperada"] = fecha_esperada
                else:
                    raise Exception("La fecha esperada ingresada no cumple con los estandares")

            # Validar que la fecha de entrega cumpla con la estructura adecuada
            if(not pedido.get("fechaEntrega")):
                fechaEntrega = input("Ingrese la fecha de entrega del pedido (YYYY-MM-DD): ")
                if(re.match(r'^\d{4}-\d{2}-\d{2}$', fechaEntrega) is not None):
                    pedido["fechaEntrega"] = fechaEntrega
                else:
                    raise Exception("La fecha de entrega ingresada no cumple con los estandares")

            # Validar que el estado cumpla con la estructura adecuada
            if(not pedido.get("estado")):
                estado = input("Ingrese el estado del pedido: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', estado) is not None):
                    pedido["estado"] = estado
                else:
                    raise Exception("El estado ingresado no cumple con los estandares")

            # Validar que el codigo del cliente sea un número
            if(not pedido.get("codigo_cliente")):
                codigo_cliente = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^\d+$', codigo_cliente) is not None):
                    pedido["codigo_cliente"] = int(codigo_cliente)
                    break
                else:
                    raise Exception("El codigo del cliente ingresado no cumple con los estandares")

        except Exception as error:
            print(error)
    print(pedido)

    peticion = requests.post(f"{BASE_URL}/pedidos", data=json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]


# Funcion para eliminar un pedido
def deletePedido(id):
    data = gP.getPedidoId(id)
    if(len(data)):
        peticion = requests.delete(f"{BASE_URL}/pedidos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "pedido eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"pedido no encontrado",
                "id": id
            }],
            "status": 400,
        }


# Funcion para modificar un producto
def EditPedido(id):
    data = gP.getPedidoId(id)
    if data is None:
        print(f"El pedido con ID {id} no existe")
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
        if modificacion == "codigo_pedido" or modificacion == "codigo_cliente":
            nuevo_valor = int(nuevo_valor)
        if modificacion in data[0]:
            data[0][modificacion] = nuevo_valor
        else:
            print(f"\nEl campo {modificacion} no existe")

    peticion = requests.put(f"{BASE_URL}/pedidos/{id}", data=json.dumps(data[0]))
    res = peticion.json()
    res["Mensaje"] = "Pedido Modificado"
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
        1. Guardar un pedido nuevo
        2. Modificar un pedido
        3. Eliminar un pedido
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postPedido(),headers= "keys", tablefmt="rounded_grid"))
        if (opcion == 2):
            id = input("Ingrese el ID del pedido que desea modificar: ")
            print(tabulate(EditPedido(id), headers="keys", tablefmt="rounded_grid"))
        if(opcion == 3):
            id = input("Ingrese el ID del pedido que desea eliminar: ")
            print(tabulate(deletePedido(id),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

        input("Presione ENTER para continuar.....")