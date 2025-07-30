

class Wildland:
    def __init__(self):
        self.name = "Wildland"
        self.description = "A vast and untamed wilderness filled with dangers and treasures."
        self.monsters = ["Wolf", "Bear", "Bandit"]
        self.quests = ["Find the Lost Treasure", "Defeat the Bandit Leader"]
        self.items = ["Healing Herb", "Rusty Sword", "Old Map"]

    def get_info(self):
        return f"{self.name}: {self.description}"

    def get_monsters(self):
        return self.monsters

    def get_quests(self):
        return self.quests

    def get_items(self):
        return self.items