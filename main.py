import modules.get_client as cliente
from tabulate import tabulate


# tablefmt="rounded_grid"
#head(ers = ["Cliente", "Nombre", "Apellido", "telefono", "fax", "Direcciion", "Ciudad", "Region", "Pais", "postal", "Rep", "credito" ]
print(tabulate(cliente.getAverageCreditLimitByRegion, tablefmt="rounded_grid"))
