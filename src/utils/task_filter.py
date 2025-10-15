from typing import List
from models.todo_item import TodoItem


class TaskFilter:
    """Klasse für Filteroperationen auf Aufgaben"""
    
    @staticmethod
    def filter_by_status(tasks: List[TodoItem], status: str) -> List[TodoItem]:
        """Filtert Aufgaben nach Status"""
        if status == "Alle":
            return tasks
        elif status == "Offen":
            return [task for task in tasks if not task.completed]
        elif status == "Erledigt":
            return [task for task in tasks if task.completed]
        return tasks
    
    @staticmethod
    def filter_by_priority(tasks: List[TodoItem], priority: str) -> List[TodoItem]:
        """Filtert Aufgaben nach Priorität"""
        if priority in ["Hoch", "Normal", "Niedrig"]:
            return [task for task in tasks if task.priority == priority]
        return tasks
    
    @staticmethod
    def filter_by_category(tasks: List[TodoItem], category: str) -> List[TodoItem]:
        """Filtert Aufgaben nach Kategorie"""
        if category in ["Allgemein", "Arbeit", "Privat", "Einkaufen", "Gesundheit", "Hobby", "Familie"]:
            return [task for task in tasks if task.category == category]
        return tasks
    
    @staticmethod
    def search_tasks(tasks: List[TodoItem], search_text: str) -> List[TodoItem]:
        """Sucht in Aufgaben nach Text"""
        if not search_text.strip():
            return tasks
        
        search_lower = search_text.lower()
        return [task for task in tasks if 
                search_lower in task.text.lower() or 
                search_lower in task.description.lower() or
                search_lower in task.category.lower()]
    
    @staticmethod
    def apply_filter(tasks: List[TodoItem], filter_text: str, search_text: str = "") -> List[TodoItem]:
        """Wendet den gewählten Filter und Suche an"""
        # Erst Suche anwenden
        if search_text.strip():
            tasks = TaskFilter.search_tasks(tasks, search_text)
        
        # Dann Filter anwenden
        if filter_text == "Alle":
            return tasks
        elif filter_text in ["Offen", "Erledigt"]:
            return TaskFilter.filter_by_status(tasks, filter_text)
        elif filter_text in ["Hoch", "Normal", "Niedrig"]:
            return TaskFilter.filter_by_priority(tasks, filter_text)
        elif filter_text in ["Allgemein", "Arbeit", "Privat", "Einkaufen", "Gesundheit", "Hobby", "Familie"]:
            return TaskFilter.filter_by_category(tasks, filter_text)
        
        return tasks