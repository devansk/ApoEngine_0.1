import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log

class Items:
    def __init__(self):
        self.sciezka = 'assets/items.json'
        self.items = self.load_items()

    def load_items(self):
        if not os.path.exists(self.sciezka):
            return []
        with open(self.sciezka, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def __str__(self):
        return f"Items: {self.items}"

    def get_item_by_id(self, item_id, typ=None):
        """
        Zwraca item o podanym id. Jeśli podano typ, filtruje także po typie.
        """
        for item in self.items:
            try:
                if item.get('id') == int(item_id):
                    if typ is None or item.get('type') == typ:
                        #log.log(f"Znaleziono item: {item['name']} o ID: {item_id}", 1)
                        return item
            except AttributeError:
                continue
        return None

baza = Items()
baza.load_items()  # Ensure items are loaded when the module is imported
