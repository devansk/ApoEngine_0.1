import sys
import os
import random
from core.inventory import inv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log

class Gracz:
    #sciezka = "saves/player_save.json"
    # name,leve,health, health_max, experience, experience_need, balance, attack, defense, critical_hit_chance
    def __init__(self, name="Steve", level=1, health=100,
                 health_max=100, experience=0, experience_need=100,
                 balance=0, attack=10, defense=5, critical_hit_chance=0.1,skill_points=0):
        self.name = name
        self.level = level
        self.health = health
        self.health_max = health_max   
        self.experience = experience
        self.experience_need = experience_need
        self.balance = balance
        self.attack = attack
        self.defense = defense
        self.critical_hit_chance = critical_hit_chance # 10% szans na trafienie krytyczne
        self.damage = int(self.attack * 0.7) #dmg = 70% wartości ataku
        self.eq = inv
        self.skill_points = skill_points
        log.log(f"Gracz {self.name} został stworzony.", 1)

    def __str__(self):
        return f"Gracz: {self.imie}, Poziom: {self.poziom}"

    @classmethod
    def load_from_file(cls, player_file='saves/player_save.json'):#wczytywanie danych gracza
        import json, os
        # Wczytaj dane gracza
        if os.path.exists(player_file):
            with open(player_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            log.log(f"Wczytano dane gracza z pliku: {player_file}", 10)
        else:
            data = {}

        return cls(
            name=data.get('name', "Steve"),
            health=data.get('health', 100),
            health_max=data.get('health_max', 100),
            level=data.get('level', 1),
            experience=data.get('experience', 0),
            experience_need=data.get('experience_need', 100),
            balance=data.get('balance', 0),
            attack=data.get('attack', 10),
            defense=data.get('defense', 5),
            critical_hit_chance=data.get('critical_hit_chance', 0.1),
            skill_points=data.get('skill_points', 0)
        )
    def save_to_file(self, filename='saves/player_save.json'):#zapis danych gracza do pliku
        import json, os
        data = {
            'name': self.name,
            'health': self.health,
            'health_max': self.health_max,
            'level': self.level,
            'experience': self.experience,
            'experience_need': self.experience_need,
            'balance': self.balance,
            'attack': self.attack,
            'defense': self.defense,
            'damage': self.damage,
            'critical_hit_chance': self.critical_hit_chance
            
        }
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            log.log(f"Zapisano dane gracza do pliku: {filename}", 10)

    # getters and setters for attributes
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        log.log(f"Zmieniono imię gracza na: {self.name}", 1)
    
    def get_level(self):
        return self.level
    def set_level(self, level):
        self.level = level
        log.log(f"Zmieniono poziom gracza na: {self.level}", 1)
    
    def get_health(self):
        return self.health
    def set_health(self, health):
        self.health = health
        log.log(f"Zmieniono zdrowie gracza na: {self.health}", 1)
    
    def get_health_max(self):
        return self.health_max
    def set_health_max(self, health_max):
        self.health_max = health_max
        log.log(f"Zmieniono maksymalne zdrowie gracza na: {self.health_max}", 1)
    
    def get_skill_points(self):
        return self.skill_points
    def set_skill_points(self, skill_points):
        self.skill_points = skill_points
        log.log(f"Zmieniono punkty umiejętności gracza na: {self.skill_points}", 1)

    def increase_skills(self, attribute = None, amount=1):
        points_left = self.get_skill_points()
        if points_left <= 0:
            log.log(f"{self.name} nie ma wystarczającej ilości punktów atrybutów do zwiększenia statystyk.", 1)
            return
        if points_left < amount:
            log.log(f"{self.name} nie ma wystarczającej ilości punktów atrybutów do zwiększenia statystyk o {amount}. Pozostało punktów: {points_left}", 1)
            return
        if attribute == "a":
            self.set_attack(self.get_attack() + amount)
        elif attribute == "d":
            self.set_defense(self.get_defense() + amount)
        elif attribute == "h":
            self.set_health_max(self.get_health_max() + amount * 10)
        elif attribute == "c":
            self.set_critical_hit_chance(self.get_critical_hit_chance() + amount * 0.01)

    def level_up(self):
        self.set_skill_points(self.get_skill_points()+5)  # Increase skill points on level up +5
        self.set_level(self.get_level() + 1)
        self.set_experience_need(int(self.get_experience_need() * 1.3))  # Increase experience needed for next level
        #log.log(f"{self.name} awansował na poziom {self.level}!", 1)
        #log.log(f"Potrzebne doświadczenie do następnego poziomu: {self.experience_need}", 1)

        self.set_health_max(int(self.get_health_max() *1.1))  # Increase max health on level up
        self.set_health(self.get_health_max())  # Restore health on level up
        #log.log(f"Maksymalne zdrowie gracza {self.name} zostało zwiększone do: {self.health_max}", 1)
        #log.log(f"Zdrowie gracza {self.name} zostało przywrócone do maksymalnego poziomu: {self.health_max}", 1)

    def get_experience(self):
        return self.experience
    def set_experience(self, experience):
        self.experience = experience
        log.log(f"Zmieniono doświadczenie gracza na: {self.experience}", 1)
    def add_experience(self, amount):
        if self.experience + amount >= self.experience_need: #jeśli doświadczenie przekracza próg, to level up
            log.log(f"Dodano {amount} doświadczenia do gracza {self.name}.",1)
            rest_xp = self.experience + amount - self.experience_need
            self.set_experience(rest_xp) #dodaj resztę doświadczenia
            self.level_up()
        else:
            self.experience += amount
            log.log(f"Dodano {amount} doświadczenia do gracza {self.name}.",1)
    
    def get_experience_need(self):
        return self.experience_need
    def set_experience_need(self, experience_need):
        self.experience_need = experience_need
        log.log(f"Zmieniono potrzebne doświadczenie do poziomu na: {self.experience_need}", 1)
    
    def get_balance(self):
        return self.balance
    def set_balance(self, balance):
        self.balance = balance
        log.log(f"Zmieniono stan konta gracza na: {self.balance}", 1)
    def add_balance(self, amount):
        self.balance += amount
        log.log(f"Dodano {amount} do stanu konta gracza {self.name}. Nowy stan konta: {self.balance}", 1)
    
    def get_attack(self):
        return self.attack
    def set_attack(self, attack):
        self.attack = attack
        #self.get_damage()  # Update damage based on new attack value
        log.log(f"Zmieniono atak gracza na: {self.get_attack()}", 1)
        log.log(f"Obrażenia gracza {self.get_name()} zostały zaktualizowane na: {self.get_damage()}", 1)
    
    def get_defense(self):
        return self.defense
    def set_defense(self, defense):
        self.defense = defense
        log.log(f"Zmieniono obronę gracza na: {self.defense}", 1)
    
    def get_critical_hit_chance(self):
        return self.critical_hit_chance
    def set_critical_hit_chance(self, critical_hit_chance):
        self.critical_hit_chance = critical_hit_chance
        log.log(f"Zmieniono szansę na trafienie krytyczne gracza na: {self.critical_hit_chance}", 1)   
    def roll_crit(self):
        #log.log(f"{self.name} is rolling for a critical hit with {self.critical_hit_chance}% chance.", 1)
        crit_yes_no = random.randint(1, 100) <= self.critical_hit_chance*100
        if crit_yes_no:
            random_dmg = random.randint(3, 70)/10
            additional_dmg = int(self.damage * random_dmg)  # 30%-70% more damage on crit
            log.log(f"critical hit [+{additional_dmg} dmg]", 1)
            return additional_dmg
        return 0

    def get_damage(self):
        dmg_value = self.damage
        dmg = random.randint(dmg_value-2,dmg_value+2)
        crit = self.roll_crit()
        if crit:
            dmg += crit
        return dmg
    def set_damage(self, damage):
        self.damage = damage
        log.log(f"Zmieniono obrażenia gracza na: {self.damage}", 1)
    
    def add_item(self, item_id, typ=None):
        """
        Dodaje item do ekwipunku gracza.
        """
        inv.add_item(item_id, typ)
        self.eq = inv
    def show_inventory(self):
        """
        Wyświetla zawartość ekwipunku gracza.
        """
        if not self.eq.items:
            log.log(f"Ekwipunek gracza {self.name} jest pusty.", 4)
            return "Ekwipunek jest pusty."
        inventory_list = [f"{item['name']} (ID: {item['id']}, Ilość: {item['quantity']})" for item in self.eq.items]
        log.log(f"Ekwipunek gracza {self.name}: {', '.join(inventory_list)}", 4)
        return inventory_list
    
