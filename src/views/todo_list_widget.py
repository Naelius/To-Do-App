from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QListWidget, QListWidgetItem, 
                             QCheckBox, QComboBox, QProgressBar)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont


class TodoListWidget(QWidget):
    """Widget für die Aufgabenliste"""
    
    # Signals für Kommunikation mit Controller
    detailed_task_requested = pyqtSignal(str)  # Detaillierte Aufgabe mit vorgefülltem Text
    task_toggled = pyqtSignal(object)  # TodoItem das geändert wurde
    task_selected = pyqtSignal(int)  # Index der ausgewählten Aufgabe
    filter_changed = pyqtSignal(str)  # Neuer Filter
    search_changed = pyqtSignal(str)  # Neuer Suchtext
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        """Initialisiert die UI-Komponenten"""
        layout = QVBoxLayout()
        
        # Titel
        title_label = QLabel("Meine To-Do-Liste")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Fortschrittsbalken
        self.setup_progress_area(layout)
        
        # Eingabebereich
        self.setup_input_area(layout)
        
        # Suche
        self.setup_search_area(layout)
        
        # Filter
        self.setup_filter_area(layout)
        
        # Aufgabenliste
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)
        
        self.setLayout(layout)
    
    def setup_input_area(self, main_layout):
        """Richtet den Eingabebereich ein"""
        input_layout = QHBoxLayout()
        
        # Eingabefeld
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Neue Aufgabe eingeben (Enter für Details)...")
        self.task_input.returnPressed.connect(self.add_task)
        input_layout.addWidget(self.task_input)
        
        # Hinzufügen Button
        self.add_button = QPushButton("+ Details")
        self.add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.add_button)
        
        main_layout.addLayout(input_layout)
    
    def setup_progress_area(self, main_layout):
        """Richtet den Fortschrittsbereich ein"""
        progress_layout = QVBoxLayout()
        
        # Fortschritts-Label
        self.progress_label = QLabel("0 von 0 Aufgaben erledigt (0%)")
        self.progress_label.setAlignment(Qt.AlignCenter)
        progress_layout.addWidget(self.progress_label)
        
        # Fortschrittsbalken
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 3px;
            }
        """)
        progress_layout.addWidget(self.progress_bar)
        
        main_layout.addLayout(progress_layout)
    
    def setup_search_area(self, main_layout):
        """Richtet den Suchbereich ein"""
        search_layout = QHBoxLayout()
        
        # Suchfeld
        search_layout.addWidget(QLabel("🔍 Suchen:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Nach Aufgaben suchen...")
        self.search_input.textChanged.connect(self.on_search_changed)
        search_layout.addWidget(self.search_input)
        
        main_layout.addLayout(search_layout)
    
    def setup_filter_area(self, main_layout):
        """Richtet den Filterbereich ein"""
        filter_layout = QHBoxLayout()
        
        # Filter Label und Combo
        filter_layout.addWidget(QLabel("📂 Filter:"))
        self.filter_combo = QComboBox()
        self.filter_combo.addItems([
            "Alle", "Offen", "Erledigt", 
            "--- Priorität ---", "Hoch", "Normal", "Niedrig",
            "--- Kategorien ---", "Allgemein", "Arbeit", "Privat", "Einkaufen", "Gesundheit", "Hobby", "Familie"
        ])
        self.filter_combo.currentTextChanged.connect(self.on_filter_changed)
        filter_layout.addWidget(self.filter_combo)
        
        filter_layout.addStretch()
        main_layout.addLayout(filter_layout)
    
    def add_task(self):
        """Öffnet Detaildialog für neue Aufgabe"""
        text = self.task_input.text().strip()
        # Sende immer Signal für detaillierte Aufgabe (auch mit leerem Text)
        self.detailed_task_requested.emit(text)
        self.task_input.clear()
    
    def on_filter_changed(self):
        """Sendet Signal bei Filteränderung"""
        filter_text = self.filter_combo.currentText()
        # Ignoriere Trennlinien
        if not filter_text.startswith("---"):
            self.filter_changed.emit(filter_text)
    
    def on_search_changed(self):
        """Sendet Signal bei Suchänderung"""
        self.search_changed.emit(self.search_input.text())
    
    def update_task_list(self, tasks):
        """Aktualisiert die Aufgabenliste"""
        self.task_list.clear()
        
        for task in tasks:
            item = QListWidgetItem()
            
            # Widget für die Aufgabe erstellen
            widget = QWidget()
            layout = QHBoxLayout()
            layout.setContentsMargins(5, 2, 5, 2)
            
            # Checkbox
            checkbox = QCheckBox()
            checkbox.setChecked(task.completed)
            checkbox.stateChanged.connect(lambda state, t=task: self.task_toggled.emit(t))
            layout.addWidget(checkbox)
            
            # Aufgabentext
            task_label = QLabel(task.text)
            if task.completed:
                task_label.setStyleSheet("text-decoration: line-through; color: gray;")
            
            # Prioritätsfarben
            priority_colors = {"Hoch": "red", "Normal": "black", "Niedrig": "green"}
            if not task.completed:
                task_label.setStyleSheet(f"color: {priority_colors.get(task.priority, 'black')};")
            
            layout.addWidget(task_label)
            layout.addStretch()
            
            # Kategorie Badge
            category_label = QLabel(task.category)
            category_colors = {
                "Allgemein": "#6c757d", "Arbeit": "#007bff", "Privat": "#28a745",
                "Einkaufen": "#ffc107", "Gesundheit": "#dc3545", "Hobby": "#6f42c1", "Familie": "#fd7e14"
            }
            category_color = category_colors.get(task.category, '#6c757d')
            category_label.setStyleSheet(f"""
                background-color: {category_color}; 
                color: white; 
                padding: 2px 8px; 
                border-radius: 10px; 
                font-size: 9px;
                margin-right: 3px;
            """)
            layout.addWidget(category_label)
            
            # Fälligkeitsdatum
            if task.due_date:
                date_label = QLabel(f"📅 {task.due_date}")
                date_label.setStyleSheet("font-size: 10px; color: gray; margin-right: 3px;")
                layout.addWidget(date_label)
            
            # Priorität Badge
            priority_label = QLabel(task.priority)
            priority_color = priority_colors.get(task.priority, 'gray')
            priority_label.setStyleSheet(f"""
                background-color: {priority_color}; 
                color: white; 
                padding: 2px 5px; 
                border-radius: 3px; 
                font-size: 10px;
            """)
            layout.addWidget(priority_label)
            
            widget.setLayout(layout)
            
            item.setSizeHint(widget.sizeHint())
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, widget)
    
    def get_current_row(self):
        """Gibt die aktuell ausgewählte Zeile zurück"""
        return self.task_list.currentRow()
    
    def update_progress(self, all_tasks):
        """Aktualisiert den Fortschrittsbalken"""
        if not all_tasks:
            self.progress_label.setText("Keine Aufgaben vorhanden")
            self.progress_bar.setValue(0)
            return
            
        total_tasks = len(all_tasks)
        completed_tasks = len([task for task in all_tasks if task.completed])
        
        if total_tasks > 0:
            percentage = int((completed_tasks / total_tasks) * 100)
            self.progress_label.setText(f"{completed_tasks} von {total_tasks} Aufgaben erledigt ({percentage}%)")
            self.progress_bar.setValue(percentage)
        else:
            self.progress_label.setText("Keine Aufgaben vorhanden")
            self.progress_bar.setValue(0)