#!/usr/bin/env python3
"""
Meine To-Do-Liste - Haupteinstiegspunkt
"""

import sys
from PyQt5.QtWidgets import QApplication
from controllers.todo_controller import TodoController


def main():
    """Hauptfunktion der Anwendung"""
    # PyQt5 Anwendung erstellen
    app = QApplication(sys.argv)
    
    # App-Metadaten setzen
    app.setApplicationName("To-Do-Liste")
    app.setApplicationVersion("1.0")
    app.setApplicationDisplayName("Meine To-Do-Liste")
    
    # Controller erstellen und starten
    controller = TodoController()
    controller.show()
    
    # Event-Loop starten
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
