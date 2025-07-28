#quests type: - collect, - kill, - find
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets')))
from log_system import log

class Quests:
    def __init__(self, sciezka='assets/quests.json'):
        self.sciezka = sciezka
        self.quests = self._load_quests()

    def _load_quests(self):
        if not os.path.exists(self.sciezka):
            return []
        with open(self.sciezka, 'r', encoding='utf-8') as f:
            try:
                log.log(f"Loading quests from {self.sciezka}.", 7)
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def get_quest_by_id(self, quest_id,player=None):
        log.log(f"Searching for quest with ID: {quest_id}", 7)
        for quest in self.quests:
            try:
                if quest.get('id') == int(quest_id):
                    #return Quest(**Quest)
                    log.log(f"Quest found: {quest['name']} (ID: {quest['id']})", 7)
                    x = Quest(player=player,id=quest['id'], name=quest['name'], description=quest['description'], balance=quest['balance'],type=quest['type'], is_completed=quest['is_completed'], is_active=quest['is_active'], xp=quest['xp'], items=quest.get('items', []))
                    return x
            except AttributeError:
                continue
        return None

class Quest:
    def __init__(self, id=None, player=None, name="Quest", description="Description of the quest", balance=5, is_completed=False, is_active=True,xp=5,items=None,type=None):
        self.id = id
        self.name = name
        self.xp = xp
        self.balance = balance
        self.description = description
        self.type = type
        self.is_active = is_active
        self.is_completed = is_completed
        self.items = items if items is not None else []
        self.player = player
        log.log(f"Quest {self.name} created with type {self.type}.", 7)


    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_xp(self):
        return self.xp
    def set_xp(self, xp):
        self.xp = xp
    
    def get_balance(self):
        return self.balance
    def set_balance(self, balance):
        self.balance = balance
    
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    
    def get_items(self):
        return self.items
    def set_items(self, items):
        self.items = items if items is not None else []
    
    def get_type(self):
        return self.type
    def set_type(self, type):
        self.type = type if type is not None else "collect"
    
    def is_completed(self):
        return self.is_completed
    def set_completed(self, is_completed):
        self.is_completed = is_completed
        log.log(f"Quest {self.name} (ID: {self.id}) completed status set to {self.is_completed}.", 7)
    
    def is_active(self):
        return self.is_active
    def set_active(self, is_active):
        self.is_active = is_active
        log.log(f"Quest {self.name} (ID: {self.id}) active status set to {self.is_active}.", 7)

    def __str__(self):
        log.log(f"Quest {self.name} (ID: {self.id}) - {self.description} | XP: {self.xp}, Balance: {self.balance}, Type: {self.type}",7)




    