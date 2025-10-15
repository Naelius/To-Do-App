from datetime import datetime


class TodoItem:
    """Datenmodell für eine einzelne Aufgabe"""
    
    def __init__(self, text, completed=False, priority="Normal", due_date=None, description="", category="Allgemein"):
        self.text = text
        self.completed = completed
        self.priority = priority
        self.due_date = due_date
        self.description = description
        self.category = category
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        """Konvertiert die Aufgabe zu einem Dictionary für JSON-Serialisierung"""
        return {
            'text': self.text,
            'completed': self.completed,
            'priority': self.priority,
            'due_date': self.due_date,
            'description': self.description,
            'category': self.category,
            'created_date': self.created_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Erstellt eine TodoItem-Instanz aus einem Dictionary"""
        item = cls(
            text=data.get('text', ''),
            completed=data.get('completed', False),
            priority=data.get('priority', 'Normal'),
            due_date=data.get('due_date'),
            description=data.get('description', ''),
            category=data.get('category', 'Allgemein')
        )
        item.created_date = data.get('created_date', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return item
    
    def __str__(self):
        return f"TodoItem('{self.text}', completed={self.completed}, priority='{self.priority}', category='{self.category}')"