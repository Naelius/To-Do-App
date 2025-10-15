from PyQt5.QtWidgets import QMessageBox, QDialog
from typing import List

from models.todo_item import TodoItem
from utils.data_manager import DataManager
from utils.task_filter import TaskFilter
from views.main_window import MainWindow
from views.add_task_dialog import AddTaskDialog


class TodoController:
    """Controller für die Todo-Anwendung - verbindet Model und View"""
    
    def __init__(self):
        self.tasks: List[TodoItem] = []
        self.data_manager = DataManager()
        self.view = MainWindow()
        
        # Signals verbinden
        self.connect_signals()
        
        # Daten laden
        self.load_tasks()
    
    def connect_signals(self):
        """Verbindet View-Signals mit Controller-Methoden"""
        todo_widget = self.view.get_todo_widget()
        
        # Todo-Liste Signals
        todo_widget.detailed_task_requested.connect(self.add_detailed_task)
        todo_widget.task_toggled.connect(self.toggle_task_completion)
        todo_widget.filter_changed.connect(self.apply_filter)
        todo_widget.search_changed.connect(self.apply_search)
        
        # Main Window Signals
        self.view.delete_requested.connect(self.delete_task)
        self.view.edit_requested.connect(self.edit_task)
        self.view.save_requested.connect(self.save_tasks)
        self.view.theme_changed.connect(self.on_theme_changed)
    
    def add_detailed_task(self, prefill_text=""):
        """Fügt eine detaillierte Aufgabe über Dialog hinzu"""
        dialog = AddTaskDialog(self.view, prefill_text=prefill_text)
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.get_task_data()
            if data['text'].strip():
                task = TodoItem(
                    text=data['text'],
                    category=data['category'],
                    priority=data['priority'],
                    due_date=data['due_date'],
                    description=data['description']
                )
                self.tasks.append(task)
                self.update_view()
                self.save_tasks()
    
    def edit_task(self):
        """Bearbeitet die ausgewählte Aufgabe"""
        todo_widget = self.view.get_todo_widget()
        current_row = todo_widget.get_current_row()
        
        if current_row < 0:
            QMessageBox.information(
                self.view, 
                "Info", 
                "Bitte wählen Sie eine Aufgabe zum Bearbeiten aus."
            )
            return
        
        # Gefilterte Tasks holen
        visible_tasks = self.get_filtered_tasks()
        if current_row >= len(visible_tasks):
            return
            
        task = visible_tasks[current_row]
        dialog = AddTaskDialog(self.view, task)
        
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.get_task_data()
            task.text = data['text']
            task.category = data['category']
            task.priority = data['priority']
            task.due_date = data['due_date']
            task.description = data['description']
            self.update_view()
            self.save_tasks()
    
    def delete_task(self):
        """Löscht die ausgewählte Aufgabe"""
        todo_widget = self.view.get_todo_widget()
        current_row = todo_widget.get_current_row()
        
        if current_row < 0:
            QMessageBox.information(
                self.view, 
                "Info", 
                "Bitte wählen Sie eine Aufgabe zum Löschen aus."
            )
            return
        
        # Gefilterte Tasks holen
        visible_tasks = self.get_filtered_tasks()
        if current_row >= len(visible_tasks):
            return
            
        task_to_delete = visible_tasks[current_row]
        
        reply = QMessageBox.question(
            self.view, 
            "Löschen bestätigen",
            f"Sind Sie sicher, dass Sie die Aufgabe '{task_to_delete.text}' löschen möchten?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.tasks.remove(task_to_delete)
            self.update_view()
            self.save_tasks()
    
    def toggle_task_completion(self, task: TodoItem):
        """Ändert den Erledigungsstatus einer Aufgabe"""
        task.completed = not task.completed
        self.update_view()
        self.save_tasks()
    
    def apply_filter(self, filter_text: str):
        """Wendet Filter auf Aufgabenliste an"""
        self.update_view()
    
    def apply_search(self, search_text: str):
        """Wendet Suche auf Aufgabenliste an"""
        self.update_view()
    
    def get_filtered_tasks(self) -> List[TodoItem]:
        """Gibt gefilterte und durchsuchte Aufgaben zurück"""
        todo_widget = self.view.get_todo_widget()
        filter_text = todo_widget.filter_combo.currentText()
        search_text = todo_widget.search_input.text()
        return TaskFilter.apply_filter(self.tasks, filter_text, search_text)
    
    def update_view(self):
        """Aktualisiert die Ansicht mit gefilterten Aufgaben"""
        filtered_tasks = self.get_filtered_tasks()
        todo_widget = self.view.get_todo_widget()
        todo_widget.update_task_list(filtered_tasks)
        todo_widget.update_progress(self.tasks)  # Fortschritt basiert auf allen Aufgaben
    
    def save_tasks(self):
        """Speichert alle Aufgaben"""
        success = self.data_manager.save_tasks(self.tasks)
        if not success:
            QMessageBox.warning(
                self.view, 
                "Speicherfehler", 
                "Konnte Aufgaben nicht speichern!"
            )
    
    def load_tasks(self):
        """Lädt alle Aufgaben"""
        self.tasks = self.data_manager.load_tasks()
        self.update_view()
    
    def show(self):
        """Zeigt das Hauptfenster an"""
        self.view.show()
    
    def on_theme_changed(self, theme_name: str):
        """Behandelt Theme-Änderungen"""
        # Hier könnten wir das Theme in den Einstellungen speichern
        print(f"Theme geändert zu: {theme_name}")
    
    def close_event(self):
        """Wird beim Schließen der Anwendung aufgerufen"""
        self.save_tasks()