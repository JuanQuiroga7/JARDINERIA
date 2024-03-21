import os
import re
from tabulate import tabulate
import json
import requests
import modules.get_product as gP

BASE_URL = "http://154.38.171.54:5008"

# Funcion para guardar un producto nuevo
def postProduct():

    producto = dict()
    while True:
        try:

            # Validar que el codigo cumpla con la estructura (AR-001)
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-\d{1,3}$', codigo) is not None):
                    data = gP.getProductCode(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="rounded_grid"))
                        raise Exception("El codigo de producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("El codigo ingresado no cumple con los estandares")
            
            # Validar que el nombre cumpla con la estructura adecuada
            if(not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', nombre) is not None):
                    producto["nombre"] = nombre
                else:
                    raise Exception("El nombre ingresado no cumple con los estandares")

            # Validar que la gama cumpla con la estructura adecuada   
            if(not producto.get("gama")):
                gama = input("Ingrese la gama del producto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', gama) is not None):
                    producto["gama"] = gama
                else:
                    raise Exception("La gama ingresada no cumple con los estandares")
                
            # Validar que las dimensiones cumplan con la estructura adecuada
            if(not producto.get("dimensiones")):
                dimensiones = input("Ingrese las dimensiones del producto: ")
                if(re.match(r'^\d{2,3}\s*-\s*\d{2,3}$', dimensiones) is not None):
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("Las dimensiones ingresadas no cumple con los estandares")
                
            # Validar que el nombre del proveedor cumpla con la estructura adecuada
            if(not producto.get("proveedor")):
                proveedores = input("Ingrese el proveedor del producto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', proveedores) is not None):
                    producto["proveedor"] = proveedores
                else:
                    raise Exception("El nombre del proveedor no cumple con los estandares")
                
            # Validar que la descripcion cumpla con la estructura adecuada
            if(not producto.get("descripcion")):
                descripciones = input("Ingrese la descripcion del producto: ")
                if(re.match(r'^[A-Z][a-zA-Z0-9\s]+$', descripciones) is not None):
                    producto["descripcion"] = descripciones
                else:
                    raise Exception("La descripcion no cumple con los estandares")
                
            # Validar que la cantidad en stock cumpla con la estructura adecuada
            if(not producto.get("cantidadEnStock")):
                stock = input("Ingrese la cantidad en stock del producto: ")
                if(re.match(r'^\d+$', stock) is not None):
                    stock = int(stock)
                    producto["cantidadEnStock"] = stock
                else:
                    raise Exception("El valor ingresado no cumple con los estandares")
                
            # Validar que el precio de venta cumpla con la estructura adecuada
            if(not producto.get("precio_venta")):
                venta = input("Ingrese el precio de venta del producto: ")
                if(re.match(r'^\d+$', venta) is not None):
                    venta = int(venta)
                    producto["precio_venta"] = venta
                else:
                    raise Exception("El valor ingresado no cumple con los estandares")
                
            # Validar que el precio de proveedor cumpla con la estructura adecuada
            if(not producto.get("precio_proveedor")):
                precioProv = input("Ingrese el precio de proveedor del producto: ")
                if(re.match(r'^\d+$', precioProv) is not None):
                    precioProv = int(precioProv)
                    producto["precio_proveedor"] = precioProv
                    break
                else:
                    raise Exception("El valor ingresado no cumple con los estandares")
                
            
        except Exception as error:
            print(error)
    print(producto)
    
    peticion = requests.post(f"{BASE_URL}/productos", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



# Funcion para eliminar un producto
def deleteProduct(id):
    data = gP.getProductId(id)
    if(len(data)):
        peticion = requests.delete(f"{BASE_URL}/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"producto no encontrado",
                "id": id
            }],
            "status": 400,
        }




# Funcion para modificar un producto
def EditProduct(id):
    data = gP.getProductId(id)
    if data is None:
        print(f"El producto con ID {id} no existe")
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
        if modificacion == "cantidadEnStock" or modificacion == "precio_venta" or modificacion == "precio_proveedor":
            nuevo_valor = int(nuevo_valor)
        if modificacion in data[0]:
            data[0][modificacion] = nuevo_valor
        else:
            print(f"\nEl campo {modificacion} no existe")

    peticion = requests.put(f"{BASE_URL}/productos/{id}", data=json.dumps(data[0]))
    res = peticion.json()
    res["Mensaje"] = "Producto Modificado"
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
        1. Guardar un producto nuevo
        2. Modificar un producto
        3. Eliminar un producto
      
""")
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postProduct(),headers= "keys", tablefmt="rounded_grid"))
        if (opcion == 2):
            id = input("Ingrese el ID del producto que desea modificar: ")
            print(tabulate(EditProduct(id), headers="keys", tablefmt="rounded_grid"))
        if(opcion == 3):
            id = input("Ingrese el ID del producto que desea eliminar: ")
            print(tabulate(deleteProduct(id),headers= "keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break

        input("Presione ENTER para continuar.....")
