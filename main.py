from tabulate import tabulate
import sys

import modules.get_client as cliente
import modules.get_office as oficina
import modules.get_employee as empleado
import modules.get_pedido as pedido
import modules.get_payment as pago



if(__name__ == "__main__"):
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
    """)
    opcion = int(input("Seleccione una de las opciones: "))
    if(opcion == 1):
        cliente.menu()
    elif(opcion == 2):
        oficina.menu()
    elif(opcion == 3):
        empleado.menu()
    elif(opcion == 4):
        pedido.menu()
    elif(opcion == 5):
        pedido.menu()
    else:
        print("Opcion invalida")



    

#print(tabulate(pago.getAllPaymentMethods(), tablefmt="rounded_grid"))



