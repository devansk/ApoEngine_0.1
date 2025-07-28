import sys
import os
import json
from core.items import baza

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log

class Inventory:
    def __init__(self):
        self.sciezka = 'saves/inv.json'
        self.items = self.load_inv()
        self.max_items = 100
        self.eq = [] #Equiped items

    def add_item(self, item_id, typ=None,quantity=1):
        item = baza.get_item_by_id(item_id, typ)
        if item is None:
            log.log(f"Item with ID {item_id} not found.", 4)
            return
        
        if len(self.items) < self.max_items:
            # Szukaj czy item już jest w inventory
            for inv_item in self.items:
                if inv_item.get('id') == item.get('id') and (typ is None or inv_item.get('type') == typ):
                    if inv_item.get('quantity', 1) >= inv_item.get('max_quantity', 1):
                        log.log(f"Item {inv_item['name']} is already at max quantity. Item added to new slot.", 4)
                        continue
                    else:
                        inv_item['quantity'] = inv_item.get('quantity', 1) + quantity
                        log.log(f"Item {inv_item['name']} quantity increased to {inv_item['quantity']}.", 4)
                        self.save_inv()
                        return
            # Jeśli nie ma, dodaj nowy item z quantity=1
            new_item = item.copy()
            new_item['quantity'] = quantity
            self.items.append(new_item)
            log.log(f"Item added to inventory: {new_item['name']}", 4)
            self.save_inv()
        #else:
            #dodaj kolejny item tego typu do ekwipunku pod


    def load_inv(self):
        if not os.path.exists(self.sciezka):
            return []
        with open(self.sciezka, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_inv(self):
        with open(self.sciezka, 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)

    def items_remove(self, item_id, typ=None,quantity=1):
        for i, item in enumerate(self.items):
            if item.get('id') == item_id and (item.get('type') == typ):
                if item.get('quantity') >= quantity:
                    item['quantity'] -= quantity
                    log.log(f"Item {item['name']} quantity decreased to {item['quantity']}.", 4)
                elif item.get('quantity') < quantity:
                    log.log(f"Not enough quantity of {item['name']} to remove.", 4)
                    return
                if item.get('quantity') == 0:
                    log.log(f"Item {item['name']} removed from inventory.", 4)
                    del self.items[i]
                self.save_inv()
                return
        log.log(f"Item with ID {item_id} not found in inventory.", 4)        
inv = Inventory()