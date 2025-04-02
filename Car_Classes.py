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
                if current_qty >= qty:
                    # If the quantity is sufficient, subtract it
                    self.replace(cursor, (part_name, current_qty - qty))
                else:
                    raise(f"Error: Not enough quantity of {part_name} in inventory(Current:{current_qty}).")
                return
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

class Catalogue():
    def __init__(self):
        self._catalogue = {} #this is a dictionary to be used as a catalogue of models and their parts
    
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
    
    def __str__(self): #I just used this list thing bc I kinda liked it 
        """Return a string representation of the catalogue."""
        between_models = []
        for model_name in self._catalogue.keys():
            model_list=[]
            model_list.append(f"{model_name}")
            model_list.append(str(self._catalogue[model_name]))
            between_models.append("\n\t".join(model_list))
        return "\n".join(between_models)
    


# This kind of list is a messy sack of shit, I know its better in some ways, but I hate pointers for some reason 
    



    
