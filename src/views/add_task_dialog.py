from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, 
                             QComboBox, QDateEdit, QTextEdit, QDialogButtonBox)
from PyQt5.QtCore import QDate
from models.todo_item import TodoItem


class AddTaskDialog(QDialog):
    """Dialog zum Hinzufügen/Bearbeiten von Aufgaben"""
    
    def __init__(self, parent=None, task=None, prefill_text=""):
        super().__init__(parent)
        self.task = task
        self.prefill_text = prefill_text
        self.init_ui()
        
        if task:
            self.populate_fields()
        elif prefill_text:
            self.task_input.setText(prefill_text)
    
    def init_ui(self):
        """Initialisiert die Benutzeroberfläche"""
        self.setWindowTitle("Aufgabe hinzufügen" if not self.task else "Aufgabe bearbeiten")
        self.setModal(True)
        self.resize(400, 300)
        
        layout = QVBoxLayout()
        
        # Aufgabentext
        layout.addWidget(QLabel("Aufgabe:"))
        self.task_input = QLineEdit()
        layout.addWidget(self.task_input)
        
        # Kategorie
        layout.addWidget(QLabel("Kategorie:"))
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Allgemein", "Arbeit", "Privat", "Einkaufen", "Gesundheit", "Hobby", "Familie"])
        self.category_combo.setCurrentText("Allgemein")
        layout.addWidget(self.category_combo)
        
        # Priorität
        layout.addWidget(QLabel("Priorität:"))
        self.priority_combo = QComboBox()
        self.priority_combo.addItems(["Niedrig", "Normal", "Hoch"])
        self.priority_combo.setCurrentText("Normal")
        layout.addWidget(self.priority_combo)
        
        # Fälligkeitsdatum
        layout.addWidget(QLabel("Fälligkeitsdatum:"))
        self.due_date = QDateEdit()
        self.due_date.setDate(QDate.currentDate())
        self.due_date.setCalendarPopup(True)
        layout.addWidget(self.due_date)
        
        # Beschreibung
        layout.addWidget(QLabel("Beschreibung:"))
        self.description_input = QTextEdit()
        self.description_input.setMaximumHeight(80)
        layout.addWidget(self.description_input)
        
        # Buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        layout.addWidget(self.button_box)
        
        self.setLayout(layout)
        
        # Fokus auf das erste Eingabefeld setzen
        self.task_input.setFocus()
    
    def populate_fields(self):
        """Füllt die Felder mit vorhandenen Daten"""
        if self.task:
            self.task_input.setText(self.task.text)
            self.category_combo.setCurrentText(self.task.category)
            self.priority_combo.setCurrentText(self.task.priority)
            if self.task.due_date:
                date = QDate.fromString(self.task.due_date, "yyyy-MM-dd")
                self.due_date.setDate(date)
            self.description_input.setPlainText(self.task.description)
    
    def showEvent(self, event):
        """Wird aufgerufen wenn Dialog angezeigt wird"""
        super().showEvent(event)
        # Fokus auf das passende Feld setzen
        if not self.task_input.text():
            self.task_input.setFocus()
        else:
            self.priority_combo.setFocus()
    
    def get_task_data(self):
        """Holt die Aufgabendaten aus dem Dialog"""
        return {
            'text': self.task_input.text(),
            'category': self.category_combo.currentText(),
            'priority': self.priority_combo.currentText(),
            'due_date': self.due_date.date().toString("yyyy-MM-dd"),
            'description': self.description_input.toPlainText()
        }