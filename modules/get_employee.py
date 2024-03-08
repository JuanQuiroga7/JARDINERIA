import storage.empleado as em

# Funcion para filtrar informacion de empleados de jefe (X)
def getAllNameEmailEmployees(codigo):
    infoEmpleado = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            infoEmpleado.append({
                "Nombre": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Email": val.get("email"),
                "Jefe": val.get("codigo_jefe")
            })
    return infoEmpleado

# Funcion para filtrar informacion del jefe de la empresa
def getBossDetails(codigo):
    infoBoss = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            infoBoss.append(val)
    return infoBoss

# Funcion para filtrar puestos diferentes a Representantes de venta
def getNonSalesRepInfo():
    infoemp = []
    for val in em.empleados:
        if(val.get("puesto") != ("Representante Ventas")):
            infoemp.append({
                "Nombres": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Puesto": val.get("puesto")
            })
    return infoemp


