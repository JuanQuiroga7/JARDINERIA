import storage.pedido as ped
from datetime import datetime

#Funcion para filtrar estado de pedidos
def getAllOrderSteps():
    orSteps = []
    for val in ped.pedido:
        if(val.get("estado") == "Pendiente", "Entregado", "Rechazado"):
            orSteps.append({
                "estado del pedido": val.get("estado")
            })
    return orSteps

#Funcion para filtrar pedidos entregados tarde
def getAllDelayOrders():
    pedidoEntregado = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidoEntregado.append({
                    "Codigo_Pedido": val.get("codigo_pedido"),
                    "Codigo_Cliente": val.get("codigo_cliente"),
                    "Fecha_Esperada": val.get("fecha_esperada"),
                    "Fecha_Entregada": val.get("fecha_entrega")
                })
    return pedidoEntregado


#Funcion para filtrar pedidos entregados al menos dos dias antes de la fecha esperada
def getAllEarlyOrders():
    pedidoEntregado = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days > 1):
                pedidoEntregado.append({
                    "Codigo_Pedido": val.get("codigo_pedido"),
                    "Codigo_Cliente": val.get("codigo_cliente"),
                    "Fecha_Esperada": val.get("fecha_esperada"),
                    "Fecha_Entregada": val.get("fecha_entrega")
                })
    return pedidoEntregado


# Funcion para filtrar pedidos rechazados en 2009 o fecha por definir
def getAllDeniedOrders():
    deniedOrder = []
    for val in ped.pedido:
        if val.get("estado") == "Rechazado" and  "2009" in val.get("fecha_pedido"):
            deniedOrder.append(val)
    return deniedOrder


# Funcion para filtrar todos los pedidos entregados en mes de Enero
def getAllShippedOrderMonth():
    shippedOrder = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado" and val.get("fecha_entrega").split("-")[1] == "01":
            shippedOrder.append(val)
    return shippedOrder


