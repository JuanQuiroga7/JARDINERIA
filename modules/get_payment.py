import storage.pago as pay


# Funcion para filtrar pagos por metodo, año y organizar el total del pago de mayor a menor
def getAllPaymentYear():
    paymentYear = []
    for val in pay.pago:
        if val.get("forma_pago") == "PayPal" and  "2008" in val.get("fecha_pago"):
            paymentYear.append(val)   
    paymentYear = paymentYear[::-1]        
    return paymentYear


def getAllPaymentMethods():
    payMeth = []
    for val in pay.pago:
        payMeth.append({
            "Metodo_pago": val.get("forma_pago")
    })
    converted = set(payMeth)
    return converted


    