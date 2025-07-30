import sys
import os
import json
import random   
from core.items import baza


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log

class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.rounds = 0
        self.winner = None
        self.drop_items = monster.get_drop_items() if hasattr(monster, 'get_drop_items') else []
        self.drop_chance = monster.get_drop_chance() if hasattr(monster, 'get_drop_chance') else 0.1

    def drop(self):
        for id in self.drop_items:
            item = baza.get_item_by_id(id)
            item_drop_chance = item.get('drop_chance', 0.1) if item else 0.1
            if random.randint(1,100) <= self.drop_chance * 100:  # Convert drop chance to percentage
                if random.randint(1,100) <= item_drop_chance * 100:
                    log.log(f"Item {item['name']} dropped from monster {self.monster.get_name()}.", 11)
                    self.player.add_item(id)

    def start(self):
        while self.player.health >= 0 and self.monster.health >= 0:
            self.rounds += 1

            self.monster.set_health(self.monster.health - self.player.attack + self.monster.defense) # Player attacks monster
            if self.monster.health <= 0: # Monster defeated
                self.winner = "player"
                log.log(f"{self.player.get_name()} wygrał walkę z {self.monster.get_name()} w {self.rounds} rundach!", 11)

                self.drop()  # Drop items after monster is defeated
                self.player.add_experience(self.monster.experience)  # Add experience to player
                self.player.add_balance(self.monster.balance)  # Add balance to player
                break

            # Check if monster is still alive before it attacks back
            if self.monster.health > 0: # Monster attacks player
                self.player.set_health(self.player.health - self.monster.attack + self.player.defense)
            if self.player.health <= 0: # Player defeated
                self.winner = "monster"
                log.log(f"{self.monster.get_name()} wygrał walkę z {self.player.get_name()} w {self.rounds} rundach!", 11)
                break
        return self.winner
    
    def repeat_fight(self):
        log.log(f"Rozpoczynamy walkę ponownie z {self.monster.get_name()}.", 11)
        self.rounds = 0
        self.winner = None
        self.monster.set_health(self.monster.health_max)
        self.start()