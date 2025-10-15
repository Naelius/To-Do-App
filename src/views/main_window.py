from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QComboBox, QLabel
from PyQt5.QtCore import pyqtSignal
from views.todo_list_widget import TodoListWidget
from utils.theme_manager import ThemeManager


class MainWindow(QMainWindow):
    """Hauptfenster der Anwendung"""
    
    # Signals für Controller-Kommunikation
    delete_requested = pyqtSignal()
    edit_requested = pyqtSignal()
    save_requested = pyqtSignal()
    theme_changed = pyqtSignal(str)  # Theme Name als Parameter
    
    def __init__(self):
        super().__init__()
        self.theme_manager = ThemeManager()
        self.current_theme = "Hell"
        self.init_ui()
    
    def init_ui(self):
        """Initialisiert die Benutzeroberfläche"""
        self.setWindowTitle("Meine To-Do-Liste")
        self.setGeometry(100, 100, 600, 500)
        
        # Zentrales Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Hauptlayout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Todo-Liste Widget
        self.todo_widget = TodoListWidget()
        main_layout.addWidget(self.todo_widget)
        
        # Control Buttons
        self.setup_control_buttons(main_layout)
        
        # Standard Theme anwenden  
        self.apply_theme("Hell")
    
    def setup_control_buttons(self, main_layout):
        """Richtet die Steuerungsbuttons ein"""
        button_layout = QHBoxLayout()
        
        # Löschen Button
        self.delete_button = QPushButton("Löschen")
        self.delete_button.clicked.connect(self.delete_requested.emit)
        button_layout.addWidget(self.delete_button)
        
        # Bearbeiten Button
        self.edit_button = QPushButton("Bearbeiten")
        self.edit_button.clicked.connect(self.edit_requested.emit)
        button_layout.addWidget(self.edit_button)
        
        # Theme Auswahl
        theme_label = QLabel("Theme:")
        button_layout.addWidget(theme_label)
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(self.theme_manager.get_theme_names())
        self.theme_combo.setCurrentText("Hell")
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        button_layout.addWidget(self.theme_combo)
        
        button_layout.addStretch()
        
        # Speichern Button
        self.save_button = QPushButton("Speichern")
        self.save_button.clicked.connect(self.save_requested.emit)
        button_layout.addWidget(self.save_button)
        
        main_layout.addLayout(button_layout)
    
    def on_theme_changed(self, theme_name: str):
        """Wird aufgerufen wenn Theme geändert wird"""
        self.current_theme = theme_name
        self.apply_theme(theme_name)
        self.theme_changed.emit(theme_name)
    
    def apply_theme(self, theme_name: str):
        """Wendet das gewählte Theme an"""
        theme_css = self.theme_manager.get_theme(theme_name)
        self.setStyleSheet(theme_css)
    
    def get_todo_widget(self):
        """Gibt das Todo-Widget zurück"""
        return self.todo_widget
    
    def set_theme(self, theme_name: str):
        """Setzt das Theme von außen"""
        self.theme_combo.setCurrentText(theme_name)
        self.apply_theme(theme_name)