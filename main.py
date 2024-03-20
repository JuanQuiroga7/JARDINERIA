from tabulate import tabulate
import sys
import os
import re

import modules.get_client as Recliente
import modules.post_client as GAEcliente
import modules.get_office as REoficina
import modules.post_office as GAEoficina
import modules.get_employee as REempleado
import modules.post_employee as GAEempleado
import modules.get_pedido as REpedido
import modules.post_pedido as GAEpedido
import modules.get_payment as REpago
import modules.post_payment as GAEpago
import modules.get_product as Reproducto
import modules.post_product as GAEproducto


def menuProducto():
    while True:
        os.system("clear")
        print("""

______  _                                   _      _                 _                                 
| ___ \(_)                                 (_)    | |               | |                                
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _ | |  _ __ ___    ___  _ __   _   _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` || | | '_ ` _ \  / _ \| '_ \ | | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| || | | | | | | ||  __/| | | || |_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_||_| |_| |_| |_| \___||_| |_| \__,_|
                                                                                                       
                                                                                                       
     _                                 _               _                                               
    | |                               | |             | |                                              
  __| |  ___   _ __   _ __   ___    __| | _   _   ___ | |_   ___   ___                                 
 / _` | / _ \ | '_ \ | '__| / _ \  / _` || | | | / __|| __| / _ \ / __|                                
| (_| ||  __/ | |_) || |   | (_) || (_| || |_| || (__ | |_ | (_) |\__ \                                
 \__,_| \___| | .__/ |_|    \___/  \__,_| \__,_| \___| \__| \___/ |___/                                
              | |                                                                                      
              |_|                                                                                      

    
    0. Regresar al menu principal
    1. Reporte de productos
    2. Guardar, Actualizar y eliminar productos
    """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            Reproducto.menu()
        elif(opcion == 2):
            GAEproducto.menu()
        elif(opcion == 0):
            break


def menuCliente():
    while True:
        os.system("clear")
        print("""

______  _                                   _      _                 _                                 
| ___ \(_)                                 (_)    | |               | |                                
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _ | |  _ __ ___    ___  _ __   _   _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` || | | '_ ` _ \  / _ \| '_ \ | | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| || | | | | | | ||  __/| | | || |_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_||_| |_| |_| |_| \___||_| |_| \__,_|
                                                                                                       
                                                                                                       
     _               _  _               _                                                              
    | |             | |(_)             | |                                                             
  __| |  ___    ___ | | _   ___  _ __  | |_   ___  ___                                                 
 / _` | / _ \  / __|| || | / _ \| '_ \ | __| / _ \/ __|                                                
| (_| ||  __/ | (__ | || ||  __/| | | || |_ |  __/\__ \                                                
 \__,_| \___|  \___||_||_| \___||_| |_| \__| \___||___/                                                
                                                                                                       
                                                                                                       

    
    0. Regresar al menu principal
    1. Reporte de clientes (Filtrar, buscar, etc)
    2. Guardar, Actualizar y elminar clientes
    """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            Recliente.menu()
        elif(opcion == 2):
            GAEcliente.menu()
        elif(opcion == 0):
            break


def menuOficina():
    while True:
        os.system("clear")
        print("""

______  _                                   _      _                 _                                 
| ___ \(_)                                 (_)    | |               | |                                
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _ | |  _ __ ___    ___  _ __   _   _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` || | | '_ ` _ \  / _ \| '_ \ | | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| || | | | | | | ||  __/| | | || |_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_||_| |_| |_| |_| \___||_| |_| \__,_|
                                                                                                       
                                                                                                       
     _         _____   __  _        _                                                                  
    | |       |  _  | / _|(_)      (_)                                                                 
  __| |  ___  | | | || |_  _   ___  _  _ __    __ _  ___                                               
 / _` | / _ \ | | | ||  _|| | / __|| || '_ \  / _` |/ __|                                              
| (_| ||  __/ \ \_/ /| |  | || (__ | || | | || (_| |\__ \                                              
 \__,_| \___|  \___/ |_|  |_| \___||_||_| |_| \__,_||___/                                              
                                                                                                       
                                                                                                       
                                                 
                                                                                                          
    0. Regresar al menu principal
    1. Reporte de oficinas (Filtrar, buscar, etc)
    2. Guardar, Actualizar y elminar oficinas
    """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            REoficina.menu()
        elif(opcion == 2):
            GAEoficina.menu()
        elif(opcion == 0):
            break


def menuEmpleado():
    while True:
        os.system("clear")
        print("""


______  _                                   _      _                 _                                 
| ___ \(_)                                 (_)    | |               | |                                
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _ | |  _ __ ___    ___  _ __   _   _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` || | | '_ ` _ \  / _ \| '_ \ | | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| || | | | | | | ||  __/| | | || |_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_||_| |_| |_| |_| \___||_| |_| \__,_|
                                                                                                       
                                                                                                       
     _         _____                    _                   _                                          
    | |       |  ___|                  | |                 | |                                         
  __| |  ___  | |__   _ __ ___   _ __  | |  ___   __ _   __| |  ___   ___                              
 / _` | / _ \ |  __| | '_ ` _ \ | '_ \ | | / _ \ / _` | / _` | / _ \ / __|                             
| (_| ||  __/ | |___ | | | | | || |_) || ||  __/| (_| || (_| || (_) |\__ \                             
 \__,_| \___| \____/ |_| |_| |_|| .__/ |_| \___| \__,_| \__,_| \___/ |___/                             
                                | |                                                                    
                                |_|                                                                    
                                           
                                                                                                       

                                                                                                                                                                                                                  
    0. Regresar al menu principal
    1. Reporte de empleados (Filtrar, buscar, etc)
    2. Guardar, Actualizar y eliminar registros de empleados
    """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            REempleado.menu()
        elif(opcion == 2):
            GAEempleado.menu()
        elif(opcion == 0):
            break


def menuPedido():
    while True:
        os.system("clear")
        print("""


______  _                                   _      _                 _                                 
| ___ \(_)                                 (_)    | |               | |                                
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _ | |  _ __ ___    ___  _ __   _   _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` || | | '_ ` _ \  / _ \| '_ \ | | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| || | | | | | | ||  __/| | | || |_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_||_| |_| |_| |_| \___||_| |_| \__,_|
                                                                                                       
                                                                                                       
     _        ______            _  _      _                                                            
    | |       | ___ \          | |(_)    | |                                                           
  __| |  ___  | |_/ /  ___   __| | _   __| |  ___   ___                                                
 / _` | / _ \ |  __/  / _ \ / _` || | / _` | / _ \ / __|                                               
| (_| ||  __/ | |    |  __/| (_| || || (_| || (_) |\__ \                                               
 \__,_| \___| \_|     \___| \__,_||_| \__,_| \___/ |___/                                               
                                                                                                       
                                                                                                       
                                                                  
                                           
                                                                                                                                                                                                                                                                                                                      
    0. Regresar al menu principal
    1. Reporte de pedidos (Filtrar, buscar, etc)
    2. Guardar, Actualizar y eliminar registros de pedidos
    """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            REpedido.menu()
        elif(opcion == 2):
            GAEpedido.menu()
        elif(opcion == 0):
            break


def menuPago():
    while True:
        os.system("clear")
        print("""



______  _                                   _      _                 _                                 
| ___ \(_)                                 (_)    | |               | |                                
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _ | |  _ __ ___    ___  _ __   _   _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` || | | '_ ` _ \  / _ \| '_ \ | | | |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| || | | | | | | ||  __/| | | || |_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_||_| |_| |_| |_| \___||_| |_| \__,_|
                                                                                                       
                                                                                                       
     _        ______                                                                                   
    | |       | ___ \                                                                                  
  __| |  ___  | |_/ /  __ _   __ _   ___   ___                                                         
 / _` | / _ \ |  __/  / _` | / _` | / _ \ / __|                                                        
| (_| ||  __/ | |    | (_| || (_| || (_) |\__ \                                                        
 \__,_| \___| \_|     \__,_| \__, | \___/ |___/                                                        
                              __/ |                                                                    
                             |___/                                                                     
                                              
                                                                                                       
                                                                  
                                                                                                                                                                                                                                                                                                                                                              
    0. Regresar al menu principal
    1. Reporte de pagos (Filtrar, buscar, etc)
    2. Guardar, Actualizar y eliminar registros de pagos
    """)
        opcion = int(input("Seleccione una de las opciones: "))
        if(opcion == 1):
            REpago.menu()
        elif(opcion == 2):
            GAEpago.menu()
        elif(opcion == 0):
            break
        
        



if(__name__ == "__main__"):
    
   

    while True:
        os.system("clear")
        print(""" 
       
___  ___                      ______        _               _                _ 
|  \/  |                      | ___ \      (_)             (_)              | |
| .  . |  ___  _ __   _   _   | |_/ / _ __  _  _ __    ___  _  _ __    __ _ | |
| |\/| | / _ \| '_ \ | | | |  |  __/ | '__|| || '_ \  / __|| || '_ \  / _` || |
| |  | ||  __/| | | || |_| |  | |    | |   | || | | || (__ | || |_) || (_| || |
\_|  |_/ \___||_| |_| \__,_|  \_|    |_|   |_||_| |_| \___||_|| .__/  \__,_||_|
                                                              | |              
                                                              |_|              

    1. Cliente
    2. Oficina
    3. Empleado
    4. Pedido
    5. Pago
    6. Producto
    0. Salir
    """)
        

      
        opcion = int(input("Seleccione una de las opciones (Recuerde que en cualquier momento puede presionar CTRL + C para regresar al menu): "))
        if(opcion == 1):
            menuCliente()
        elif(opcion == 2):
            menuOficina()
        elif(opcion == 3):
            menuEmpleado()
        elif(opcion == 4):
            menuPedido()
        elif(opcion == 5):
            menuPago()
        elif(opcion == 6):
            menuProducto()
        elif(opcion == 0):
            break
        else:
            print("Opcion invalida")



    

#print(tabulate(pago.getAllPaymentMethods(), tablefmt="rounded_grid"))



