from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

class Parts(ListaOrdenada):
    """
    A list of parts, each part has a name and a quantity. Used for both the inventory
    and the parts of every model in the catalogue.

    Methods
    -------
    add_part(part_name, qty):
        Add a part to the inventory or update its quantity.
    sustract_part(part_name, qty):
        Subtract a part from the inventory.
    delete_part(part):
        Delete a part from the inventory.
    model_parts_showcase():
        Return a list of parts in a formatted string.
    __str__():
        Return a string representation of the inventory.
    """
    def __init__(self):
        """
        Initialize the Parts object.

        Returns
        -------
        None.
        """
        super().__init__()

    def add_part(self, part_name, qty):
        """
        Add a part to the inventory or update its quantity.

        Parameters
        ----------
        part_name : str
            The name of the part.
        qty : int
            The quantity of the part.

        Returns
        -------
        None.
        """
        cursor = self.first()
        while cursor is not None:
            current_part, current_qty = self.get_element(cursor)
            if current_part == part_name:
                self.replace(cursor, (part_name, current_qty + qty))
                return
            cursor = self.after(cursor)
        self.add((part_name, qty))

    def sustract_part(self, part_name, qty):
        """
        Subtract a part from the inventory.

        Parameters
        ----------
        part_name : str
            The name of the part.
        qty : int
            The quantity to subtract.

        Returns
        -------
        bool
            True if the part is still in stock, False if it is out of stock.
        """
        cursor = self.first()
        while cursor is not None:
            current_part, current_qty = self.get_element(cursor)
            if current_part == part_name:
                if current_qty > qty:
                    self.replace(cursor, (part_name, current_qty - qty))
                    return True
                if current_qty == qty:
                    self.replace(cursor, (part_name, current_qty - qty))
                    return False
            cursor = self.after(cursor)
        raise ValueError(f"La pieza {part_name} no debería faltar en el inventario.")

    def delete_part(self, part):
        """
        Delete a part from the inventory.

        Parameters
        ----------
        part : str
            The name of the part to delete.

        Returns
        -------
        None.
        """
        cursor = self.first()
        while cursor is not None:
            current_part, _ = self.get_element(cursor)
            if current_part == part:
                self.delete(cursor)
                print(f"Eliminada: Pieza - {part}.")
                return
        return

    def model_parts_showcase(self):
        """
        Return a list of parts in the inventory in a formatted string.

        Returns
        -------
        str
            A formatted string of parts and their quantities.
        """
        parts_list = []
        cursor = self.first()
        while cursor is not None:
            part, qty = self.get_element(cursor)
            parts_list.append(f"{part} - {qty}")
            cursor = self.after(cursor)
        return "\n".join(parts_list)

    def __str__(self):
        """
        Return a string representation of the inventory.

        Returns
        -------
        str
            A string representation of the inventory.
        """
        parts_list = []
        cursor = self.first()
        while cursor is not None:
            part, qty = self.get_element(cursor)
            parts_list.append(f"{part}: {qty}")
            cursor = self.after(cursor)
        return " | ".join(parts_list)


class Inventory(Parts):
    """
    A list of parts, each part has a name and a quantity, used for the inventory.

    Methods
    -------
    read_parts_and_add_to_inventory(path):
        Read parts from a file and add them to the inventory.
    sufficient_parts(parts):
        Check if the inventory has sufficient parts for a list of parts.
    """
    def __init__(self):
        """
        Initialize the Inventory object.

        Returns
        -------
        None.
        """
        super().__init__()

    def read_parts_and_add_to_inventory(self, path="piezas.txt"):
        """
        Read parts from a file and add them to the inventory.

        Parameters
        ----------
        path : str
            The file path where the parts are stored.

        Returns
        -------
        None.
        """
        parts = []
        number_of_parts = []
        with open(path) as f:
            for l in f.readlines():
                ls = l.strip().split(",")
                part_name, qty = ls[0], int(ls[1])
                parts.append(part_name)
                number_of_parts.append(qty)
        for i in range(len(parts)):
            self.add_part(parts[i], number_of_parts[i])

    def sufficient_parts(self, parts: list):
        """
        Check if the inventory has sufficient parts for a list of parts.

        Parameters
        ----------
        parts : list
            A list of tuples where each tuple contains the part name and the quantity.

        Returns
        -------
        list
            A list of missing parts and their required quantities.
        """
        missing_parts = []
        for part_name, qty in parts:
            found = False
            cursor = self.first()
            while cursor is not None:
                current_part, current_qty = self.get_element(cursor)
                if current_part == part_name:
                    found = True
                    if current_qty < qty:
                        missing_parts.append((part_name, qty - current_qty))
                    break
                cursor = self.after(cursor)
            if not found:
                raise ValueError(f"La pieza {part_name} no debería faltar en el inventario.")
        return missing_parts


class Catalogue:
    """
    A catalogue of models, where each model has a list of parts.

    Methods
    -------
    keys():
        Return the keys of the catalogue.
    __getitem__(model_name):
        Return the parts of a model.
    add_to_catalogue(model_name, part_name, qty):
        Add a part to the catalogue.
    read_models_and_add_to_catalogue(path):
        Read models and their parts from a file and add them to the catalogue.
    remove_from_catalogue(model_name):
        Remove a model from the catalogue.
    __str__():
        Return a string representation of the catalogue.
    """
    def __init__(self):
        """
        Initialize the Catalogue object.

        Returns
        -------
        None.
        """
        self._catalogue = {}

    def keys(self):
        """
        Return the keys of the catalogue.

        Returns
        -------
        dict_keys
            The keys of the catalogue.
        """
        return self._catalogue.keys()

    def __getitem__(self, model_name):
        """
        Return the parts of a model.

        Parameters
        ----------
        model_name : str
            The name of the model.

        Returns
        -------
        Parts
            The parts of the model.
        """
        if model_name in self._catalogue.keys():
            return self._catalogue[model_name]
        else:
            raise KeyError(f"Modelo {model_name} no encontrado en el catálogo.")

    def add_to_catalogue(self, model_name, part_name, qty):
        """
        Add a part to the catalogue.

        Parameters
        ----------
        model_name : str
            The name of the model.
        part_name : str
            The name of the part.
        qty : int
            The quantity of the part.

        Returns
        -------
        None.
        """
        if model_name not in self._catalogue.keys():
            self._catalogue[model_name] = Parts()
        self._catalogue[model_name].add_part(part_name, qty)

    def read_models_and_add_to_catalogue(self, path="modelos.txt"):
        """
        Read models and their parts from a file and add them to the catalogue.

        Parameters
        ----------
        path : str
            The file path where the models are stored.

        Returns
        -------
        None.
        """
        with open(path) as f:
            for l in f.readlines():
                ls = l.strip().split(",")
                model_name, part_name, qty = ls[0], ls[1], int(ls[2])
                self.add_to_catalogue(model_name, part_name, qty)

    def remove_from_catalogue(self, model_name):
        """
        Remove a model from the catalogue.

        Parameters
        ----------
        model_name : str
            The name of the model to remove.

        Returns
        -------
        bool
            True if the model was removed, False otherwise.
        """
        if model_name in self._catalogue.keys():
            del self._catalogue[model_name]
            return True
        else:
            print(f"Modelo {model_name} no encontrado en el catálogo.")
            return False

    def __str__(self):
        """
        Return a string representation of the catalogue.

        Returns
        -------
        str
            A string representation of the catalogue.
        """
        between_models = []
        for model_name in self._catalogue.keys():
            model_list = []
            model_list.append(f"{model_name}")
            model_list.append(str(self._catalogue[model_name]))
            between_models.append("\n\t".join(model_list))
        return "\n".join(between_models)


class Concesionario:
    """
    A dealership that manages an inventory and a catalogue of models.

    Methods
    -------
    check_and_remove_models(out_of_stock_parts):
        Check if a model is out of stock and remove it from the catalogue.
    procces_order(model_name):
        Process an order for a model.
    receive_order(model_name):
        Receive an order for a model.
    check_handler():
        Check the inventory and catalogue for missing or invalid parts.
    """
    def __init__(self):
        """
        Initialize the Concesionario object.

        Returns
        -------
        None.
        """
        self._inventario = Inventory()
        self._catalogo = Catalogue()

    @property
    def inventario(self):
        """
        Return the inventory.

        Returns
        -------
        Inventory
            The inventory object.
        """
        return self._inventario

    @property
    def catalogo(self):
        """
        Return the catalogue.

        Returns
        -------
        Catalogue
            The catalogue object.
        """
        return self._catalogo

    def check_and_remove_models(self, out_of_stock_parts: list):
        """
        Check if a model is out of stock and remove it from the catalogue.

        Parameters
        ----------
        out_of_stock_parts : list
            A list of parts that are out of stock.

        Returns
        -------
        None.
        """
        copy_catalog = list(self._catalogo.keys())
        for part_name in out_of_stock_parts:
            for model_name in copy_catalog:
                cursor = self._catalogo._catalogue[model_name].first()
                while cursor is not None:
                    part, _ = self._catalogo._catalogue[model_name].get_element(cursor)
                    if part == part_name:
                        self.catalogo.remove_from_catalogue(model_name)
                        print(f"Eliminado: modelo {model_name} dependiente")
                        break
                    cursor = self._catalogo._catalogue[model_name].after(cursor)

    def procces_order(self, model_name):
        """
        Process an order for a model.

        Parameters
        ----------
        model_name : str
            The name of the model to process.

        Returns
        -------
        bool
            True if the catalogue is empty after processing, False otherwise.
        """
        if model_name not in self._catalogo.keys():
            print(f"Pedido NO atendido. Modelo {model_name} fuera de catálogo.")
            return
        needed_parts_list = []
        cursor = self._catalogo[model_name].first()
        while cursor is not None:
            part, qty = self._catalogo[model_name].get_element(cursor)
            needed_parts_list.append((part, qty))
            cursor = self._catalogo[model_name].after(cursor)
        missing_parts = self._inventario.sufficient_parts(needed_parts_list)

        if len(missing_parts) == 0:
            out_of_stock_parts = []
            for needed_part in needed_parts_list:
                part, qty = needed_part
                result = self.inventario.sustract_part(part, qty)
                if not result:
                    out_of_stock_parts.append(part)
            print(f"Pedido {model_name} atendido.")
            if len(out_of_stock_parts) != 0:
                for part in out_of_stock_parts:
                    self.inventario.delete_part(part)
            self.check_and_remove_models(out_of_stock_parts)

        else:
            print(f"Pedido {model_name} NO atendido. Faltan:")
            for part, qty in missing_parts:
                print(f"\t{part} - ({qty})")
            if self.catalogo.remove_from_catalogue(model_name):
                print(f"Eliminado: {model_name}")

        if len(self._catalogo.keys()) == 0:
            is_finished = True
            return is_finished

    def receive_order(self, model_name):
        """
        Receive an order for a model.

        Parameters
        ----------
        model_name : str
            The name of the model to receive.

        Returns
        -------
        None.
        """
        if model_name not in self._catalogo.keys():
            print(f"Pedido NO atendido. Modelo {model_name} fuera de catálogo.")
        else:
            print(f"{model_name}:")
            print(f"\t{self._catalogo[model_name].model_parts_showcase()} ")
            self.procces_order(model_name)

    def check_handler(self):
        """
        Check the inventory and catalogue for missing or invalid parts.

        Returns
        -------
        bool
            True if no errors are found, raises ValueError otherwise.
        """
        failed = False
        errors_count = 0
        inventory_parts = {part: qty for part, qty in self._inventario}
        for model_name in self._catalogo.keys():
            cursor = self._catalogo[model_name].first()
            while cursor is not None:
                part, qty = self._catalogo[model_name].get_element(cursor)
                if qty <= 0:
                    print(f"La pieza {part} del modelo {model_name} tiene una cantidad inválida: ({qty}).")
                    failed = True
                    errors_count += 1
                if part not in inventory_parts:
                    print(f"La pieza {part} del modelo {model_name} no existe en el inventario.")
                    failed = True
                    errors_count += 1
                cursor = self._catalogo[model_name].after(cursor)

        cursor = self._inventario.first()
        while cursor is not None:
            part, qty = self._inventario.get_element(cursor)
            if qty <= 0:
                print(f"La pieza {part} en el inventario tiene una cantidad inválida ({qty}).")
                failed = True
                errors_count += 1
            cursor = self._inventario.after(cursor)
        if failed:
            raise ValueError(f"Se encontraron errores ({errors_count}) en el inventario y catálogo. Verifique los mensajes anteriores y revise los archivos fuente.")
        return True