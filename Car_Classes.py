from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada
#Developer Note: Sebastián please try to understand the code before erasing all to restart from scratch as previously done.

class Parts(ListaOrdenada): # This class is a list of parts, each part has a name and a quantity, used for both the inventory
# and the parts of every model in the catalogue.
    def __init__(self):
        super().__init__()

    #For each part, I will store a tuple with the name of the part and its quantity, I think this is the best way to do it.
    def add_part(self, part_name, qty):
        """Add a part to the inventory or update its quantity."""
        cursor = self.first()  # Start from the first element
        while cursor is not None:
            current_part, current_qty = self.get_element(cursor)
            if current_part == part_name:
                # If the part already exists, update its quantity
                self.replace(cursor, (part_name, current_qty + qty))
                return # Exit the method after updating if it exists already
            cursor = self.after(cursor)  # Move to the next element
        
        # If the part does not exist, add it to the inventory
        self.add((part_name, qty))
    
    def sustract_part(self, part_name, qty):
        """Subtract a part from the inventory."""
        cursor = self.first()
        while cursor is not None:
            current_part, current_qty = self.get_element(cursor)
            if current_part == part_name:
                if current_qty > qty:
                    # If the quantity is sufficient, subtract it
                    self.replace(cursor, (part_name, current_qty - qty))
                    return True
                else:  # If needed, this will remove the part from the inventory
                    # If the quantity is equal, remove the part
                    self.delete(cursor)
                    print(f"Eliminada: {part_name}.")
                    return False
            cursor = self.after(cursor)
        raise ValueError(f"La pieza {part_name} no debería faltar en el inventario.")# If the part is not found, this case should never happen if the catalog is pre-checked
    
    def model_parts_showcase(self): #Designed specifically for the catalogue, this will show the parts of a model in a different manner
        """Return a list of parts in the inventory."""
        parts_list = []
        cursor = self.first()
        while cursor is not None:
            part, qty = self.get_element(cursor)
            parts_list.append(f"{part} - {qty}")
            cursor = self.after(cursor)
        return "\n".join(parts_list)    
    
    def __str__(self):
        """Return a string representation of the inventory."""
        parts_list = []
        cursor = self.first()
        while cursor is not None:
            part, qty = self.get_element(cursor)
            parts_list.append(f"{part}: {qty}")
            cursor = self.after(cursor)
        return " | ".join(parts_list) #This is for printing the inventory in a readable way, learned something here tbh
    
class Inventory(Parts): #This class is a list of parts, each part has a name and a quantity, used for the inventory.
    def __init__(self):
        super().__init__()
    
    def read_parts_and_add_to_inventory(self,path="piezas.txt"): #I just read and directly add to the inventory
        parts=[]
        number_of_parts=[]
        with open(path) as f:
            for l in f.readlines():
                ls = l.strip().split(",")
                part_name, qty = ls[0], int(ls[1])
                #print(f"Por hacer: añadir al inventario la pieza \"{part_name}\" con ({qty} unidades)") # Old print from original code
                parts.append(part_name)
                number_of_parts.append(qty)
        for i in range(len(parts)):
            self.add_part(parts[i], number_of_parts[i])
        #Maybe add a return if needed later
    
    def sufficient_parts(self, parts:list):
        """Check if the inventory has sufficient parts for a list of parts."""
        missing_parts = []
        for part_name, qty in parts:
            found=False
            cursor = self.first()
            while cursor is not None:
                current_part, current_qty = self.get_element(cursor)
                if current_part == part_name:
                    found=True # If the part is found, check if the quantity is sufficient
                    if current_qty < qty:
                        missing_parts.append((part_name, qty - current_qty)) # If the quantity is not sufficient, add it to the list
                    break
                cursor = self.after(cursor)
            if not found:
                raise ValueError(f"La pieza {part_name} no debería faltar en el inventario.") # Error if the part is not found, this case should never happen if the catalog is pre-checked
        return missing_parts # For the parts not sufficient, to supply the order, this will return a list of tuples with the part name and the quantity needed
    

class Catalogue():# Same logic as before, but each model has a list of parts
    def __init__(self):
        self._catalogue = {} #this is a dictionary to be used as a catalogue of models and their parts
   
    def keys(self): #Had a bunch of errors because of this, I had to put the keys() method in the class
        """Return the keys of the catalogue."""
        return self._catalogue.keys()
    
    def __getitem__(self, model_name): #Same as before, these dictionary methods are a bit weird to handle 
        """Return the parts of a model."""
        if model_name in self._catalogue.keys():
            return self._catalogue[model_name]
        else:
            raise KeyError(f"Modelo {model_name} no encontrado en el catálogo.")
        
    def add_to_catalogue(self, model_name, part_name, qty): #Too easy to be true I think
        """Add a part to the catalogue."""
        if model_name not in self._catalogue.keys():
            self._catalogue[model_name] = Parts()
        self._catalogue[model_name].add_part(part_name, qty)
    
    def read_models_and_add_to_catalogue(self,path="modelos.txt"):
        model_name=[]
        part_name=[]
        qty=[]
        with open(path) as f:
            for l in f.readlines(): 
                ls = l.strip().split(",")
                model_name, part_name, qty = ls[0], ls[1], int(ls[2])
                #print(f"Por hacer: añadir al catálogo pieza \"{part_name}\" ({qty} unidades) al modelo \"{model_name}\"") # Old print from original code
                self.add_to_catalogue(model_name, part_name, qty)
    
    def remove_from_catalogue(self, model_name):
        """Remove a model from the catalogue."""
        if model_name in self._catalogue.keys():
            del self._catalogue[model_name]
            return True
        else:
            print(f"Modelo {model_name} no encontrado en el catálogo.") #This print is for debugging purposes, should be impossible to get
            return False
        
    def __str__(self): #I just used this list thing bc I kinda liked it before
        """Return a string representation of the catalogue."""
        between_models = []
        for model_name in self._catalogue.keys():
            model_list=[]
            model_list.append(f"{model_name}")
            model_list.append(str(self._catalogue[model_name]))
            between_models.append("\n\t".join(model_list))
        return "\n".join(between_models)

class Concesionario():
    def __init__(self):
        self._inventario=Inventory()
        self._catalogo=Catalogue()
    
    @property
    def inventario(self):
        return self._inventario

    @property
    def catalogo(self):
        return self._catalogo
    
    def  check_and_remove_models(self,out_of_stock_parts:list):
        """Check if a model is out of stock and remove it from the catalogue."""
        for part_name in out_of_stock_parts: # If the list is empty, this will not do anything
            for model_name in self._catalogo.keys():
                cursor = self._catalogo._catalogue[model_name].first()
                while cursor is not None:
                    part, _ = self._catalogo._catalogue[model_name].get_element(cursor)
                    if part == part_name:
                        self.catalogo.remove_from_catalogue(model_name)
                        print(f"Eliminado: modelo {model_name} dependiente")
                        break
                    cursor = self._catalogo._catalogue[model_name].after(cursor)

    def procces_order(self,model_name):
        """Process an order for a model."""
        if model_name not in self._catalogo.keys():
            print(f"Pedido NO atendido. Modelo {model_name} fuera de catálogo. ")
            return
        needed_parts_list = []
        cursor = self._catalogo[model_name].first()
        while cursor is not None:
            part, qty = self._catalogo[model_name].get_element(cursor)
            needed_parts_list.append((part, qty))
            cursor = self._catalogo[model_name].after(cursor)
        missing_parts = self._inventario.sufficient_parts(needed_parts_list) #This will check if the parts are in stock, as not to start subtracting some for the order not to be attended in the end
        
        if len(missing_parts)==0: #If there are no missing parts, the order can be attended
            out_of_stock_parts = [] # Made a list in case multiple parts go out of stock after the order is processed
            for needed_part in needed_parts_list:
                part, qty =needed_part
                result=self.inventario.sustract_part(part, qty) #This will throw an error if the part is not in stock, but it should never happen if the catalogue is pre-checked
                if not result:  #If the part is just out of stock but able to supply the order, this if will trigger and the part will be stored in a list for later removal 
                    out_of_stock_parts.append(part) 
            print(f"Pedido {model_name} atendido.")
            self.check_and_remove_models(out_of_stock_parts) #If there are parts out of stock, this will remove the models dependant on said parts from the catalogue        
        else:
            print(f"Pedido {model_name} NO atendido. Faltan:")
            for part, qty in missing_parts:
                print(f"\t{part} - ({qty})")
            if self.catalogo.remove_from_catalogue(model_name):
                print(f"Eliminado: {model_name} dependiente.")
    
    def receive_order(self,model_name):
        """Receive an order for a model."""
        if model_name not in self._catalogo.keys():
            print(f"Pedido NO atendido. Modelo {model_name} fuera de catálogo. ")
        else:
            print(f"{model_name}:")
            print(f"\t{self._catalogo[model_name].model_parts_showcase()} ") #Special method for the catalogue to show the parts of a model
            self.procces_order(model_name)

    def check_handler(self):
        """Check the inventory and catalogue for missing or invalid parts."""
        failed=False
        errors_count=0
        inventory_parts = {part: qty for part, qty in self._inventario}  # list comprehension to get the parts and their quantities from the inventory, It is unreadable but it gets the job done
        # Check the catalogue for missing or invalid parts
        for model_name in self._catalogo.keys():
            cursor = self._catalogo[model_name].first()
            while cursor is not None:
                part, qty = self._catalogo[model_name].get_element(cursor)
                if qty <= 0:
                    print(f"La pieza {part} del modelo {model_name} tiene una cantidad inválida: ({qty}).")
                    failed=True
                    errors_count+=1
                if part not in inventory_parts:
                    print(f"La pieza {part} del modelo {model_name} no existe en el inventario.")
                    failed=True
                    errors_count+=1
                cursor = self._catalogo[model_name].after(cursor)

        # Inventory check, for invalid quantities
        cursor = self._inventario.first()
        while cursor is not None:
            part, qty = self._inventario.get_element(cursor)
            if qty <= 0:
                print(f"La pieza {part} en el inventario tiene una cantidad inválida ({qty}).")
                failed=True
                errors_count+=1
            cursor = self._inventario.after(cursor)
        if failed:
            raise ValueError(f"Se encontraron errores ({errors_count}) en el inventario y catálogo. Verifique los mensajes anteriores y revise los archivos fuente.") # This will raise an error if there are any errors in the inventory or catalogue
        return True












    
