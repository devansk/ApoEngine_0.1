import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log


class Monsters:
    def __init__(self, sciezka='assets/monsters.json'):
        self.sciezka = sciezka
        self.monsters = self._load_monsters()

    def _load_monsters(self):
        if not os.path.exists(self.sciezka):
            return []
        with open(self.sciezka, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def get_monster_by_id(self, monster_id):
        for monster in self.monsters:
            try:
                if monster.get('id') == int(monster_id):
                    return Monster(**monster)
            except AttributeError:
                continue
        return None

class Monster:
    def __init__(self, id=None, name="Monster", health=100, health_max=100, level=1, experience=0, balance=0, attack=10, defense=5, description="A scary monster", drop_chance=0.1, drop_items=None, type=None):
        
        # Jeśli podano tylko id, pobierz dane z Monsters
        if id is not None and name == "Monster" and health == 100 and health_max == 100 and level == 1 and experience == 0 and balance == 0 and attack == 10 and defense == 5 and description == "A scary monster" and drop_chance == 0.1 and type == None and drop_items is None:
            quest_data = Monsters().get_monster_by_id(id)
            if quest_data:
                self.id = quest_data.id
                self.name = quest_data.name
                self.health = quest_data.health
                self.health_max = quest_data.health_max
                self.level = quest_data.level
                self.experience = quest_data.experience
                self.balance = quest_data.balance
                self.attack = quest_data.attack
                self.defense = quest_data.defense
                self.description = quest_data.description
                self.drop_chance = quest_data.drop_chance
                self.drop_items = quest_data.drop_items
                self.damage = quest_data.damage
                self.type = quest_data.type
                log.log(f"Monster {self.name} created with level {self.level}.", 2)
            else:
                # Brak danych, domyślne wartości
                self.id = id
                self.name = name
                self.health = health
                self.health_max = health_max
                self.level = level
                self.experience = experience
                self.balance = balance
                self.attack = attack
                self.defense = defense
                self.description = description
                self.drop_chance = drop_chance
                self.drop_items = drop_items if drop_items is not None else []
                self.damage = attack * 0.7
                self.type = type if type is not None else "monster"
                
        else:
            self.id = id
            self.name = name
            self.health = health
            self.health_max = health_max
            self.level = level
            self.experience = experience
            self.balance = balance
            self.attack = attack
            self.defense = defense
            self.description = description
            self.drop_chance = drop_chance
            self.drop_items = drop_items if drop_items is not None else []
            self.damage = attack * 0.7
            self.type = type if type is not None else "monster"
        

    def get_drop_chance(self):
        return self.drop_chance
    def set_drop_chance(self, drop_chance):
        self.drop_chance = drop_chance
        log.log(f"Zmieniono szansę dropu {self.get_name()} na: {self.get_drop_chance()}", 2)
    
    def get_drop_items(self):
        return self.drop_items
    def set_drop_items(self, drop_items):
        self.drop_items = drop_items
        log.log(f"Zmieniono przedmioty dropu {self.get_name()} na: {self.get_drop_items()}", 2)
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        stare = self.get_name()
        self.name = name
        log.log(f"Zmieniono imię {stare} na: {self.get_name()}", 2)
    
    def get_level(self):
        return self.level
    def set_level(self, level):
        self.level = level
        log.log(f"Zmieniono poziom {self.get_name()} na: {self.level}", 2)
    
    def get_health(self):
        return self.health
    def set_health(self, health):
        self.health = health
        log.log(f"Zmieniono zdrowie {self.get_name()} na: {self.health}", 2)
    
    def get_health_max(self):
        return self.health_max
    def set_health_max(self, health_max):
        self.health_max = health_max
        log.log(f"Zmieniono maksymalne zdrowie {self.get_name()} na: {self.health_max}", 2)

    def get_experience(self):
        return self.experience
    def set_experience(self, experience):
        self.experience = experience
        log.log(f"Zmieniono doświadczenie {self.get_name()} na: {self.get_experience()}", 2)
    
    def get_balance(self):
        return self.balance
    def set_balance(self, balance):
        self.balance = balance
        log.log(f"Zmieniono stan konta {self.get_name()} na: {self.get_balance()}", 2)
    
    def get_attack(self):
        return self.attack
    def set_attack(self, attack):
        self.attack = attack
        #self.get_damage()  # Update damage based on new attack value
        log.log(f"Zmieniono atak {self.get_name()} na: {self.get_attack()}", 2)
        log.log(f"Obrażenia {self.get_name()} zostały zaktualizowane na: {self.get_damage()}", 2)
    
    def get_defense(self):
        return self.defense
    def set_defense(self, defense):
        self.defense = defense
        log.log(f"Zmieniono obronę gracza na: {self.get_defense()}", 2)
    def get_description(self):
        return self.description
    
    def get_damage(self):
        return self.damage

