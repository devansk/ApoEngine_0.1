from core.player import Gracz
from core.monsters import Monster
from core.fight import Fight
from core.quests import Quests

import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'misc')))
from log_system import log
'''
    CO DZIAŁA?
        -> klasa gracz
            - obsługa wczytywania i zapisywania stanu gracza
            - możliwość dodawania przedmiotów do ekwipunku
            - level up postaci
            - rozwoj statystyk gracza
        
        -> klasa przedmiot
            - obsługa przedmiotów, wczytywanie z pliku
            - możliwość dodawania przedmiotów do ekwipunku gracza
        
        -> klasa ekwipunek
            - obsługa ekwipunku, wczytywanie i zapisywanie stanu ekwipunku
            - możliwość wyświetlania ekwipunku gracza
            - możliwość dodawania przedmiotów do ekwipunku gracza
            - obsługa ilości przedmiotów w ekwipunku (np. 2x mikstura zdrowia)       
'''
'''
    CO ROBIE?
        -> dodać możliwość zapisu 3 postaci gracza
        -> dodać możliwość wyboru postaci gracza
        -> dodać 2 dodatkowe ekwipunki dla 2 pozostałych postaci
        -> klasa monster [80%]
        -> klasa walka [60%]
        -> klasa mapa
        -> klasa quest
        -> klasa sklep


'''
def main():
    #gracz1 = Gracz()
    gracz1 = Gracz.load_from_file()
    #print(gracz1.level)
    #gracz1.add_item(0,"healing")  # Example item ID
    #gracz1.show_inventory()  
    # Add more functionality here as needed
    #gracz1.add_experience(150)  # Example of adding experience
    #print(f"Gracz {gracz1.name} ma teraz {gracz1.experience} doświadczenia i jest na poziomie {gracz1.level}.")
    #gracz1.increase_skills(attribute='a', amount=5)  # Increase health by 5
    #print(f"Gracz {gracz1.name} ma teraz {gracz1.get_attack()} ataku.")
    #gracz1.save_to_file()  # Save the player's state to a file

    # Example of creating a monster
    monster = Monster(1)  # Load monster with ID 1

    # Example of starting a fight
    #fight = Fight(gracz1, monster)
    #winner = fight.start()
    quest = Quests().get_quest_by_id(id=2,player=gracz1)  # Get quest with ID 1


if __name__ == "__main__":
    main()