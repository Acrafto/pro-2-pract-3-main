from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada
#from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada
from Car_Classes import *

def procces_orders(orders:list,concesionario:Concesionario): #This will later be used to process the order
    """Process an order for a specific model."""
    for model_name,customer in orders:
        print(f"Nuevo pedido: {model_name}--{customer}")
        concesionario.procces_order(model_name) #This will process the order
        print("--------STOCK--------")
        print(inventario) 
        print("---------------------")
    return True

def read_orders_and_procces(path, concesionario): #This will read the orders from a file and process them
    with open(path) as f:
        orders=[]
        for l in f.readlines():
            ls = l.strip().split(",")
            customer, model_name = ls[0], ls[1]
            orders.append((model_name,customer))
            #print(f"Por hacer: procesar pedido de modelo {model_name} para cliente {customer}") # Old print from original code
    return procces_orders(orders, concesionario) #This will process the order


			
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
    finished=read_orders_and_procces("pedidos.txt", concesionario)
    if finished:
        print("--------CATALOGO-------- ")
        print(catalogo)
