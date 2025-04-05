from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada
#from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada
from Car_Classes import *
def procces_order(model_name,concesionario): #This will later be used to process the order
    """Process an order for a specific model."""
    return None

def read_orders_and_procces(path, concesionario): #This will read the orders from a file and process them
    with open(path) as f:
        for l in f.readlines():
            ls = l.strip().split(",")
            customer, model_name = ls[0], ls[1]
            print(f"Nuevo pedido: {model_name}--{customer}")
            procces_order(model_name,concesionario)


			
if __name__ == "__main__":
    concesionario=Concesionario()
    inventario=concesionario.inventario
    catalogo=concesionario.catalogo
    inventario.read_parts_and_add_to_inventory()
    catalogo.read_models_and_add_to_catalogue()
    print("--------STOCK--------")
    print(inventario) 
    print("--------CATALOGO-------- ")
    print(catalogo)
    read_orders_and_procces("pedidos.txt", concesionario)
