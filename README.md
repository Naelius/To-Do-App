# 📋 Meine To-Do-Liste

Eine moderne, funktionsreiche To-Do-Anwendung mit grafischer Benutzeroberfläche, entwickelt in Python mit PyQt5.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### ✨ Kern-Funktionen
- **Aufgaben erstellen, bearbeiten und löschen**
- **Prioritäten** (Hoch, Normal, Niedrig) mit Farbkodierung
- **Fälligkeitsdaten** mit integriertem Kalender
- **Detaillierte Beschreibungen** für jede Aufgabe
- **Kategorien-System** (Allgemein, Arbeit, Privat, Einkaufen, Gesundheit, Hobby, Familie)

### 🔍 Erweiterte Features
- **Echtzeit-Suchfunktion** - Durchsucht Titel, Beschreibung und Kategorien
- **Umfassende Filter** - Nach Status, Priorität und Kategorien
- **Fortschrittsbalken** - Zeigt erledigte Aufgaben in Prozent
- **Persistente Speicherung** - Automatisches Speichern in JSON-Format

### 🎨 20 Verschiedene Themes
- **Klassisch**: Hell, Dunkel, Blau, Grün, Lila, Orange
- **Speziell**: Rainbow (Regenbogen-Farbverläufe), Hacker (Matrix-Style), Retro (80er Jahre)
- **Thematisch**: Cyborg, Viking, Fallout, Biohazard, Cyberpunk, Steampunk, Vampire, Alien, Wasteland, Neon

## 🚀 Installation

### Voraussetzungen
- Python 3.7 oder höher
- PyQt5

### Schritt-für-Schritt Installation

1. **Repository klonen**
```bash
git clone https://github.com/IhrBenutzername/To-Do-App.git
cd To-Do-App
```

2. **PyQt5 installieren**
```bash
pip install PyQt5
```

3. **Anwendung starten**
```bash
cd src
python main.py
```

## 📁 Projektstruktur

```
To-Do-App/
├── 📁 config/
│   └── settings.json          # Anwendungseinstellungen
├── 📁 data/
│   └── tasks.json            # Gespeicherte Aufgaben
└── 📁 src/
    ├── 📁 models/            # Datenmodelle
    │   ├── __init__.py
    │   └── todo_item.py      # TodoItem Klasse
    ├── 📁 views/             # GUI-Komponenten
    │   ├── __init__.py
    │   ├── main_window.py    # Hauptfenster
    │   ├── todo_list_widget.py # Aufgabenliste Widget
    │   └── add_task_dialog.py  # Dialog für Aufgaben-Details
    ├── 📁 controllers/       # Geschäftslogik (MVC Pattern)
    │   ├── __init__.py
    │   └── todo_controller.py # Hauptcontroller
    ├── 📁 utils/             # Hilfsfunktionen
    │   ├── __init__.py
    │   ├── data_manager.py   # Daten laden/speichern
    │   ├── task_filter.py    # Filteroperationen
    │   └── theme_manager.py  # Theme-Verwaltung
    └── main.py               # Anwendungs-Einstiegspunkt
```

## 🎯 Verwendung

### Neue Aufgabe erstellen
1. Text in das Eingabefeld eingeben (optional)
2. **"+ Details"** klicken oder **Enter** drücken
3. Im Dialog alle Details ausfüllen:
   - Kategorie auswählen
   - Priorität festlegen
   - Fälligkeitsdatum setzen
   - Beschreibung hinzufügen
4. **OK** klicken

### Aufgaben verwalten
- **✅ Abhaken**: Checkbox anklicken
- **✏️ Bearbeiten**: Aufgabe auswählen → "Bearbeiten" Button
- **🗑️ Löschen**: Aufgabe auswählen → "Löschen" Button

### Suchen und Filtern
- **🔍 Suchen**: Text in Suchfeld eingeben für Echtzeit-Suche
- **📂 Filtern**: Dropdown-Menü für Status, Priorität oder Kategorie

### Themes wechseln
- Theme-Dropdown in der unteren Leiste verwenden
- Zwischen 20 verschiedenen Designs wählen

## 🏗️ Architektur

Die Anwendung folgt dem **Model-View-Controller (MVC)** Pattern:

- **Models** (`models/`): Datenstrukturen und -logik
- **Views** (`views/`): GUI-Komponenten und Benutzeroberfläche  
- **Controllers** (`controllers/`): Geschäftslogik und Datenfluss
- **Utils** (`utils/`): Wiederverwendbare Hilfsfunktionen

### Design Patterns
- **Separation of Concerns**: Klare Trennung der Verantwortlichkeiten
- **Signal-Slot Pattern**: PyQt5 Signal-basierte Kommunikation
- **Strategy Pattern**: Austauschbare Filter- und Theme-Strategien

## 🎨 Theme-System

### Standard Themes
- **Hell/Dunkel**: Klassische Designs
- **Farbthemes**: Blau, Grün, Lila, Orange mit Farbverläufen

### Spezielle Themes
- **🌈 Rainbow**: Regenbogen-Farbverläufe mit Glüheffekten
- **💻 Hacker**: Matrix-inspiriertes grün-auf-schwarz Design
- **📻 Retro**: 80er Jahre Synthwave-Ästhetik

### Thematische Themes
- **🤖 Cyborg**: Metallisch-futuristisch
- **⚔️ Viking**: Nordisch mit Holz und Gold
- **☢️ Fallout**: Post-apokalyptisch
- **☣️ Biohazard**: Giftgrün und gefährlich
- **🌃 Cyberpunk**: Neon Pink und Cyan
- **⚙️ Steampunk**: Viktorianisch-mechanisch
- **🧛 Vampire**: Düster und blutig
- **👽 Alien**: Außerirdisch mysteriös
- **🏜️ Wasteland**: Ödland-Ästhetik  
- **💫 Neon**: Glühende Neonlichter

## 📊 Kategorien-System

| Kategorie | Farbe | Verwendung |
|-----------|-------|------------|
| 🔘 Allgemein | Grau | Standard-Aufgaben |
| 💼 Arbeit | Blau | Berufliche Aufgaben |
| 🏠 Privat | Grün | Persönliche Aufgaben |
| 🛒 Einkaufen | Gelb | Shopping-Listen |
| ❤️ Gesundheit | Rot | Gesundheit & Fitness |
| 🎨 Hobby | Lila | Freizeitaktivitäten |
| 👨‍👩‍👧‍👦 Familie | Orange | Familiäre Verpflichtungen |

## 🔧 Konfiguration

Die Anwendung speichert Einstellungen in `config/settings.json`:

```json
{
  "app": {
    "name": "Meine To-Do-Liste",
    "version": "1.0",
    "theme": "Hell"
  },
  "data": {
    "file_path": "../data/tasks.json",
    "auto_save": true
  },
  "ui": {
    "window_width": 600,
    "window_height": 500
  }
}
```

## 💾 Datenformat

Aufgaben werden im JSON-Format gespeichert:

```json
{
  "text": "Einkaufen gehen",
  "category": "Einkaufen", 
  "priority": "Normal",
  "completed": false,
  "due_date": "2025-10-16",
  "description": "Milch, Brot und Äpfel kaufen",
  "created_date": "2025-10-15 10:30:00"
}
```

## 🚀 Erweiterungsmöglichkeiten

Das saubere MVC-Design ermöglicht einfache Erweiterungen:

- **Neue Themes**: Theme-Manager in `utils/theme_manager.py`
- **Zusätzliche Filter**: TaskFilter in `utils/task_filter.py`
- **Neue Kategorien**: AddTaskDialog in `views/add_task_dialog.py`
- **Weitere Datenfelder**: TodoItem Model in `models/todo_item.py`

## 🤝 Beitragen

1. Fork des Repositories
2. Feature Branch erstellen (`git checkout -b feature/AmazingFeature`)
3. Änderungen committen (`git commit -m 'Add some AmazingFeature'`)
4. Branch pushen (`git push origin feature/AmazingFeature`)
5. Pull Request öffnen

## 👨‍💻 Autor

Erstellt mit ❤️ und Python

## 🙏 Danksagungen

- **PyQt5** für die excellente GUI-Framework
- **Python Community** für die großartige Unterstützung
- **GitHub Copilot** für die Entwicklungsunterstützung

---

⭐ **Gefällt Ihnen das Projekt? Geben Sie uns einen Stern!** ⭐
