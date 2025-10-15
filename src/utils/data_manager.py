import json
import os
from typing import List
from models.todo_item import TodoItem


class DataManager:
    """Verwaltet das Laden und Speichern von Aufgaben"""
    
    def __init__(self, data_file="../data/tasks.json"):
        self.data_file = data_file
    
    def save_tasks(self, tasks: List[TodoItem]) -> bool:
        """Speichert Aufgaben in JSON-Datei"""
        try:
            # Verzeichnis erstellen falls nicht vorhanden
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            
            # Aufgaben zu Dictionary konvertieren
            tasks_data = [task.to_dict() for task in tasks]
            
            # In Datei speichern
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(tasks_data, f, ensure_ascii=False, indent=2)
            
            return True
            
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False
    
    def load_tasks(self) -> List[TodoItem]:
        """Lädt Aufgaben aus JSON-Datei"""
        try:
            if not os.path.exists(self.data_file):
                return []
            
            with open(self.data_file, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
            
            # Dictionary zu TodoItem konvertieren
            tasks = [TodoItem.from_dict(data) for data in tasks_data]
            return tasks
            
        except Exception as e:
            print(f"Fehler beim Laden: {e}")
            return []