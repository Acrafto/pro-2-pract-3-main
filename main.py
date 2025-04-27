from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada
# from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada
from Car_Classes import *

def procces_order(orders: list, concesionario: Concesionario):
    """
    Process an order for a specific model.

    Parameters
    ----------
    orders : list
        A list of tuples where each tuple contains the model name and the customer name.
    concesionario : Concesionario
        The dealership object that processes the orders.

    Returns
    -------
    bool
        True if the process is completed successfully.
    """
    for model_name, customer in orders:
        print(f"Nuevo pedido: {model_name}--{customer}")
        is_finished = concesionario.procces_order(model_name, orders)  # This will process the order
        print("--------STOCK--------")
        print(inventario)
        print("---------------------")
        if is_finished is True:
            break
    return True

def read_orders_and_procces(path: str, concesionario: Concesionario):
    """
    Read the orders from a file and process them.

    Parameters
    ----------
    path : str
        The file path where the orders are stored.
    concesionario : Concesionario
        The dealership object that processes the orders.

    Returns
    -------
    bool
        True if the orders are processed successfully.
    """
    with open(path) as f:
        orders = []
        for l in f.readlines():
            ls = l.strip().split(",")
            customer, model_name = ls[0], ls[1]
            orders.append((model_name, customer))
            # print(f"Por hacer: procesar pedido de modelo {model_name} para cliente {customer}") # Old print from original code
    return procces_order(orders, concesionario)  # This will process the order


if __name__ == "__main__":
    """
    Main entry point of the program. Initializes the dealership, reads inventory and catalog data,
    and processes orders from a file.
    """
    concesionario = Concesionario()
    inventario = concesionario.inventario
    catalogo = concesionario.catalogo

    # Load inventory and catalog data
    inventario.read_parts_and_add_to_inventory()
    catalogo.read_models_and_add_to_catalogue()

    # Check if the dealership is ready to handle orders
    if concesionario.check_handler():
        print("--------STOCK--------")
        print(inventario)
        print("--------CATALOGO-------- ")
        print(catalogo)

        # Process orders from the file
        finished = read_orders_and_procces("pedidos.txt", concesionario)
        if finished:
            print("--------CATALOGO-------- ")
            print(catalogo)
