import storage.cliente as cli

# Funcion para filtrar cliente por nombre
def getAllClientsName():
    clientName = list()
    for val in cli.clientes:
        codigoName = dict({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })    
        
        clientName.append(codigoName)
    return clientName

 # Funcion para filtrar cliente por codigo   
def getOneClientCode(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }

# Funcion para filtrar cliente por limite de credito y ciudad. 
def getAllClientCreditCity(creditLimit, city):
    clientCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= creditLimit and val.get('ciudad') == city):
            clientCredit.append(val)
    return clientCredit
            
# Funcion para filtrar clientes por representantes de venta
def getAllClientPerSalesRep(codigo):
    clientRep = []
    for val in cli.clientes:
        if(val.get('codigo_empleado_rep_ventas') == codigo):
            clientRep.append(val)
    return clientRep

# Funcion para filtrar clientes por paiis, region y ciudad
def getAllClientCountryRegionCity(country, region=None, city=None):
    clientzone = []
    for val in cli.clientes:
        if(
            val.get('pais') == country or
            (val.get('region') == region or val.get('region') == None) and 
            (val.get('ciudad') == city or val.get('ciudad') == None)
        ):
            clientzone.append(val)
    return clientzone




    