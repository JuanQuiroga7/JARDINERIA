import storage.oficina as of

# Funcion para filtrar oficinas por ciudad 
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina: 
        codigoCiudad.append({
            "Codigo": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad")
        })
    return codigoCiudad 


def getAllPhonesCity(pais):
    phonesCity = []
    for val in of.oficina:
        if(val.get("pais") == pais ):
            phonesCity.append({
            "Telefono": val.get("telefono"),
            "Ciudad": val.get("ciudad"),
            "Oficina": val.get("codigo_oficina"),
            "Pais": val.get("pais")
        })
    return phonesCity


