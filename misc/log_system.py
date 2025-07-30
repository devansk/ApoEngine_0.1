# utilities/log_system.py
# - log system
#id = 0 - general log
#id = 1 - player log
#id = 2 - monster log
#id = 3 - event log
from datetime import datetime
import os


class LogSystem:
    def __init__(self, log_path='saves/logs'):
        self.log_path = log_path
        self._add_session_separator()
        self.logs = self.load_logs()

    def _add_session_separator(self):
        # Dodaj pustą linię na końcu pliku logów przy każdym uruchomieniu
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write('\n')

    def log(self, message, id=0):
        if id == 0:
            log_type = "[General]"
        elif id == 1:
            log_type = "[Player]"
        elif id == 2:
            log_type = "[Monster]"
        elif id == 3:
            log_type = "[Event]"
        elif id == 4:
            log_type = "[Inventory]"
        elif id == 5:
            log_type = "[Crafting]"
        elif id == 6:
            log_type = "[Gathering]"
        elif id == 7:
            log_type = "[Quest]"
        elif id == 8:
            log_type = "[Shop]"
        elif id == 9:
            log_type = "[Print]"
        elif id == 10:
            log_type = "[Save]"
        elif id == 11:
            log_type = "[Fight]"
        else:
            log_type = "[Unknown]"
        czas = datetime.now().strftime("[%H:%M][%d.%m.%Y]")
        entry = f"{czas}{log_type} - {message}"
        self.logs.append(entry)
        self.save_logs()

    def get_logs(self):
        return self.logs
    
    def get_logs_by_id(self, id):
        log_types = {0: "[General]", 1: "[Player]", 2: "[Monster]", 3: "[Event]", 4: "[Inventory]", 5: "[Crafting]", 6: "[Gathering]", 7: "[Quest]", 8: "[Shop]", 9: "[Print]"}
        log_type = log_types.get(id, "[Unknown]")
        return "\n".join([log for log in self.logs if log.startswith(log_type)])

    def clear_logs(self):
        self.logs = []
        self.save_logs()

    def save_logs(self):
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        with open(self.log_path, 'w', encoding='utf-8') as f:
            for log in self.logs:
                f.write(log + '\n')

    def load_logs(self):
        if not os.path.exists(self.log_path):
            return []
        with open(self.log_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]

log = LogSystem()