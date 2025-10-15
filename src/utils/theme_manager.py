from typing import Dict
class ThemeManager:
    """Verwaltet verschiedene Themes für die Anwendung"""
    def __init__(self):
        self.themes = {
            "Hell": self._light_theme(),
            "Dunkel": self._dark_theme(),
            "Blau": self._blue_theme(),
            "Grün": self._green_theme(),
            "Lila": self._purple_theme(),
            "Orange": self._orange_theme(),
            "Rainbow": self._rainbow_theme(),
            "Hacker": self._hacker_theme(),
            "Retro": self._retro_theme(),
            "Cyborg": self._cyborg_theme(),
            "Viking": self._viking_theme(),
            "Fallout": self._fallout_theme(),
            "Biohazard": self._biohazard_theme(),
            "Cyberpunk": self._cyberpunk_theme(),
            "Steampunk": self._steampunk_theme(),
            "Vampire": self._vampire_theme(),
            "Alien": self._alien_theme(),
            "Wasteland": self._wasteland_theme(),
            "Neon": self._neon_theme()
        }
    def get_theme(self, theme_name: str) -> str:
        """Gibt das CSS für das gewählte Theme zurück"""
        return self.themes.get(theme_name, self.themes["Hell"])
    def get_theme_names(self) -> list:
        """Gibt alle verfügbaren Theme-Namen zurück"""
        return list(self.themes.keys())
    def _light_theme(self) -> str:
        """Helles Standard-Theme"""
        return """
            QMainWindow {
                background-color: #f0f0f0;
                color: #000000;
            }
            QListWidget {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #e0e0e0;
                border: 1px solid #cccccc;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                padding: 8px;
                border-radius: 5px;
            }
            QComboBox {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                padding: 5px;
                border-radius: 5px;
            }
        """
    def _dark_theme(self) -> str:
        """Dunkles Theme"""
        return """
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QListWidget {
                background-color: #3c3c3c;
                border: 1px solid #555555;
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #404040;
                border: 1px solid #555555;
                color: #ffffff;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QLineEdit {
                background-color: #3c3c3c;
                border: 1px solid #555555;
                color: #ffffff;
                padding: 8px;
                border-radius: 5px;
            }
            QLabel {
                color: #ffffff;
            }
            QComboBox {
                background-color: #3c3c3c;
                border: 1px solid #555555;
                color: #ffffff;
                padding: 5px;
                border-radius: 5px;
            }
        """
    def _blue_theme(self) -> str:
        """Blaues Theme"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #e3f2fd, stop:1 #bbdefb);
                color: #0d47a1;
            }
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #2196f3;
                color: #0d47a1;
                border-radius: 8px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #64b5f6, stop:1 #2196f3);
                border: none;
                color: white;
                padding: 8px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #42a5f5, stop:1 #1976d2);
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #2196f3;
                padding: 8px;
                border-radius: 8px;
                color: #0d47a1;
            }
            QLabel {
                color: #0d47a1;
                font-weight: bold;
            }
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #2196f3;
                padding: 5px;
                border-radius: 8px;
                color: #0d47a1;
            }
        """
    def _green_theme(self) -> str:
        """Grünes Natur-Theme"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #e8f5e8, stop:1 #c8e6c9);
                color: #1b5e20;
            }
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #4caf50;
                color: #1b5e20;
                border-radius: 8px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #81c784, stop:1 #4caf50);
                border: none;
                color: white;
                padding: 8px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #66bb6a, stop:1 #388e3c);
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #4caf50;
                padding: 8px;
                border-radius: 8px;
                color: #1b5e20;
            }
            QLabel {
                color: #1b5e20;
                font-weight: bold;
            }
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #4caf50;
                padding: 5px;
                border-radius: 8px;
                color: #1b5e20;
            }
        """
    def _purple_theme(self) -> str:
        """Lila Eleganz-Theme"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #f3e5f5, stop:1 #e1bee7);
                color: #4a148c;
            }
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #9c27b0;
                color: #4a148c;
                border-radius: 8px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ba68c8, stop:1 #9c27b0);
                border: none;
                color: white;
                padding: 8px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ab47bc, stop:1 #7b1fa2);
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #9c27b0;
                padding: 8px;
                border-radius: 8px;
                color: #4a148c;
            }
            QLabel {
                color: #4a148c;
                font-weight: bold;
            }
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #9c27b0;
                padding: 5px;
                border-radius: 8px;
                color: #4a148c;
            }
        """
    def _orange_theme(self) -> str:
        """Orange Sonnenuntergang-Theme"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #fff3e0, stop:1 #ffcc80);
                color: #e65100;
            }
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #ff9800;
                color: #e65100;
                border-radius: 8px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ffb74d, stop:1 #ff9800);
                border: none;
                color: white;
                padding: 8px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ffa726, stop:1 #f57c00);
            }
            QLineEdit {
                background-color: #ffffff;
                border: 2px solid #ff9800;
                padding: 8px;
                border-radius: 8px;
                color: #e65100;
            }
            QLabel {
                color: #e65100;
                font-weight: bold;
            }
            QComboBox {
                background-color: #ffffff;
                border: 2px solid #ff9800;
                padding: 5px;
                border-radius: 8px;
                color: #e65100;
            }
        """
    def _rainbow_theme(self) -> str:
        """Buntes Rainbow Theme - Das Highlight!"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #ff6b6b, stop:0.16 #feca57, stop:0.33 #48dbfb, 
                    stop:0.5 #ff9ff3, stop:0.66 #54a0ff, stop:0.83 #5f27cd, 
                    stop:1 #00d2d3);
                color: #2f3640;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 rgba(255,255,255,0.9), stop:1 rgba(255,255,255,0.8));
                border: 3px solid;
                border-image: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff6b6b, stop:0.25 #feca57, stop:0.5 #48dbfb, 
                    stop:0.75 #ff9ff3, stop:1 #54a0ff);
                color: #2f3640;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff6b6b, stop:0.2 #feca57, stop:0.4 #48dbfb, 
                    stop:0.6 #ff9ff3, stop:0.8 #54a0ff, stop:1 #5f27cd);
                border: none;
                color: white;
                padding: 10px;
                border-radius: 10px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff5252, stop:0.2 #fdd835, stop:0.4 #29b6f6, 
                    stop:0.6 #e91e63, stop:0.8 #3f51b5, stop:1 #673ab7);
            }
            QLineEdit {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 rgba(255,255,255,0.9), stop:1 rgba(255,255,255,0.8));
                border: 3px solid;
                border-image: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff6b6b, stop:0.33 #feca57, stop:0.66 #48dbfb, stop:1 #ff9ff3);
                padding: 10px;
                border-radius: 10px;
                color: #2f3640;
                font-weight: bold;
            }
            QLabel {
                color: #2f3640;
                font-weight: bold;
            }
            QComboBox {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 rgba(255,255,255,0.9), stop:1 rgba(255,255,255,0.8));
                border: 3px solid;
                border-image: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff6b6b, stop:0.5 #feca57, stop:1 #48dbfb);
                padding: 8px;
                border-radius: 8px;
                color: #2f3640;
                font-weight: bold;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #2f3640;
            }
        """
    def _hacker_theme(self) -> str:
        """Matrix/Hacker Theme"""
        return """
            QMainWindow {
                background-color: #000000;
                color: #00ff00;
            }
            QListWidget {
                background-color: #001100;
                border: 2px solid #00ff00;
                color: #00ff00;
                border-radius: 5px;
                font-family: 'Courier New', monospace;
            }
            QPushButton {
                background-color: #003300;
                border: 1px solid #00ff00;
                color: #00ff00;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QPushButton:hover {
                background-color: #004400;
                border: 2px solid #00ff00;
            }
            QLineEdit {
                background-color: #001100;
                border: 1px solid #00ff00;
                padding: 8px;
                border-radius: 5px;
                color: #00ff00;
                font-family: 'Courier New', monospace;
            }
            QLabel {
                color: #00ff00;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QComboBox {
                background-color: #001100;
                border: 1px solid #00ff00;
                padding: 5px;
                border-radius: 5px;
                color: #00ff00;
                font-family: 'Courier New', monospace;
            }
        """
    def _retro_theme(self) -> str:
        """80er Jahre Retro Theme"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ff006e, stop:0.5 #8338ec, stop:1 #3a86ff);
                color: #ffffff;
            }
            QListWidget {
                background-color: #1a1a2e;
                border: 3px solid #eee;
                color: #eee;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #ff006e, stop:1 #8338ec);
                border: 2px solid #eee;
                color: #eee;
                padding: 10px;
                border-radius: 10px;
                font-weight: bold;
                text-}
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #d90058, stop:1 #6b2db8);
                border: 3px solid #eee;
            }
            QLineEdit {
                background-color: #1a1a2e;
                border: 2px solid #eee;
                padding: 10px;
                border-radius: 10px;
                color: #eee;
                font-weight: bold;
            }
            QLabel {
                color: #eee;
                font-weight: bold;
                text-}
            QComboBox {
                background-color: #1a1a2e;
                border: 2px solid #eee;
                padding: 8px;
                border-radius: 10px;
                color: #eee;
                font-weight: bold;
            }
        """
    def _cyborg_theme(self) -> str:
        """🤖 Cyborg Theme - Metallisch und futuristisch"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #1a1a1a, stop:0.3 #2d2d2d, stop:0.7 #404040, stop:1 #0f0f0f);
                color: #00ccff;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(0,0,0,0.8), stop:1 rgba(20,20,20,0.9));
                border: 3px solid #00ccff;
                color: #ffffff;
                border-radius: 10px;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #404040, stop:0.5 #606060, stop:1 #303030);
                border: 2px solid #00ccff;
                color: #00ccff;
                padding: 12px;
                border-radius: 8px;
                font-weight: bold;
                text-font-family: 'Arial Black', sans-serif;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #505050, stop:0.5 #707070, stop:1 #404040);
                color: #ffffff;
                border: 3px solid #00ccff;
            }
            QLineEdit {
                background: rgba(0,0,0,0.7);
                border: 2px solid #00ccff;
                padding: 10px;
                border-radius: 8px;
                color: #00ccff;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QLabel {
                color: #00ccff;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
            }
            QComboBox {
                background: rgba(0,0,0,0.7);
                border: 2px solid #00ccff;
                padding: 8px;
                border-radius: 8px;
                color: #00ccff;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
        """
    def _viking_theme(self) -> str:
        """⚔️ Viking Theme - Nordisch und rustikal"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #8B4513, stop:0.3 #A0522D, stop:0.7 #CD853F, stop:1 #8B4513);
                color: #FFD700;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 rgba(139, 69, 19, 0.9), stop:1 rgba(160, 82, 45, 0.8));
                border: 4px solid #8B4513;
                border-style: ridge;
                color: #FFFAF0;
                border-radius: 15px;
                font-family: 'Georgia', serif;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #CD853F, stop:0.5 #DEB887, stop:1 #D2691E);
                border: 3px solid #8B4513;
                border-style: outset;
                color: #8B0000;
                padding: 12px;
                border-radius: 10px;
                font-weight: bold;
                font-family: 'Georgia', serif;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #DEB887, stop:0.5 #F4A460, stop:1 #CD853F);
                border-style: inset;
                color: #800000;
            }
            QLineEdit {
                background: rgba(255, 248, 220, 0.9);
                border: 3px solid #8B4513;
                border-style: inset;
                padding: 10px;
                border-radius: 10px;
                color: #8B0000;
                font-family: 'Georgia', serif;
                font-weight: bold;
            }
            QLabel {
                color: #FFD700;
                font-weight: bold;
                font-family: 'Georgia', serif;
            }
            QComboBox {
                background: rgba(255, 248, 220, 0.9);
                border: 3px solid #8B4513;
                border-style: inset;
                padding: 8px;
                border-radius: 10px;
                color: #8B0000;
                font-family: 'Georgia', serif;
                font-weight: bold;
            }
        """
    def _fallout_theme(self) -> str:
        """☢️ Fallout Theme - Post-apokalyptisch"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #2F1B14, stop:0.5 #8B4513, stop:1 #654321);
                color: #FFD700;
            }
            QListWidget {
                background: qradial-gradient(circle, rgba(255,215,0,0.1) 0%, rgba(139,69,19,0.8) 100%);
                border: 3px solid #DAA520;
                color: #FFFAF0;
                border-radius: 12px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #B8860B, stop:0.5 #DAA520, stop:1 #CD853F);
                border: 2px solid #8B7355;
                color: #2F1B14;
                padding: 12px;
                border-radius: 8px;
                font-weight: bold;
                font-family: 'Courier New', monospace;
                text-}
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #DAA520, stop:0.5 #FFD700, stop:1 #B8860B);
                color: #000000;
                border: 3px solid #FFD700;
            }
            QLineEdit {
                background: rgba(218, 165, 32, 0.3);
                border: 2px solid #DAA520;
                padding: 10px;
                border-radius: 8px;
                color: #FFD700;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            QLabel {
                color: #FFD700;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QComboBox {
                background: rgba(218, 165, 32, 0.3);
                border: 2px solid #DAA520;
                padding: 8px;
                border-radius: 8px;
                color: #FFD700;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
        """
    def _biohazard_theme(self) -> str:
        """☣️ Biohazard Theme - Giftig und gefährlich"""
        return """
            QMainWindow {
                background: qradial-gradient(circle, #1a4c00 0%, #0d2600 50%, #000000 100%);
                color: #39ff14;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(0,0,0,0.9), stop:0.5 rgba(26,76,0,0.6), stop:1 rgba(0,0,0,0.9));
                border: 3px solid #39ff14;
                border-style: double;
                color: #39ff14;
                border-radius: 10px;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QPushButton {
                background: qradial-gradient(circle, #39ff14 0%, #2eb300 50%, #1a4c00 100%);
                border: 2px solid #39ff14;
                color: #000000;
                padding: 12px;
                border-radius: 10px;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
                text-}
            QPushButton:hover {
                background: qradial-gradient(circle, #4dff4d 0%, #39ff14 50%, #2eb300 100%);
                color: #000000;
                border: 3px solid #39ff14;
            }
            QLineEdit {
                background: rgba(0,0,0,0.8);
                border: 2px solid #39ff14;
                border-style: groove;
                padding: 10px;
                border-radius: 8px;
                color: #39ff14;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QLabel {
                color: #39ff14;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
            }
            QComboBox {
                background: rgba(0,0,0,0.8);
                border: 2px solid #39ff14;
                border-style: groove;
                padding: 8px;
                border-radius: 8px;
                color: #39ff14;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
        """
    def _cyberpunk_theme(self) -> str:
        """🌃 Cyberpunk Theme - Neon und High-Tech"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #0a0a0a, stop:0.3 #1a0033, stop:0.7 #330066, stop:1 #0a0a0a);
                color: #ff00ff;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(0,0,0,0.9), stop:0.5 rgba(51,0,102,0.5), stop:1 rgba(0,0,0,0.9));
                border: 3px solid #ff00ff;
                color: #00ffff;
                border-radius: 15px;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff00ff, stop:0.5 #00ffff, stop:1 #ff00ff);
                border: none;
                color: #000000;
                padding: 12px;
                border-radius: 12px;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
                text-}
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #00ffff, stop:0.5 #ff00ff, stop:1 #00ffff);
                border: 3px solid #ff00ff;
            }
            QLineEdit {
                background: rgba(0,0,0,0.8);
                border: 2px solid #00ffff;
                padding: 12px;
                border-radius: 12px;
                color: #ff00ff;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QLabel {
                color: #ff00ff;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
            }
            QComboBox {
                background: rgba(0,0,0,0.8);
                border: 2px solid #00ffff;
                padding: 10px;
                border-radius: 12px;
                color: #ff00ff;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
        """
    def _steampunk_theme(self) -> str:
        """⚙️ Steampunk Theme - Viktorianisch und mechanisch"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #8B4513, stop:0.3 #CD853F, stop:0.7 #D2691E, stop:1 #A0522D);
                color: #FFD700;
            }
            QListWidget {
                background: qradial-gradient(circle, rgba(205,133,63,0.8) 0%, rgba(160,82,45,0.9) 100%);
                border: 5px solid #B8860B;
                border-style: ridge;
                color: #2F1B14;
                border-radius: 20px;
                font-family: 'Times New Roman', serif;
                font-weight: bold;
            }
            QPushButton {
                background: qradial-gradient(circle, #DAA520 0%, #B8860B 70%, #8B7355 100%);
                border: 3px solid #654321;
                border-style: outset;
                color: #2F1B14;
                padding: 15px;
                border-radius: 15px;
                font-weight: bold;
                font-family: 'Times New Roman', serif;
                text-}
            QPushButton:hover {
                background: qradial-gradient(circle, #FFD700 0%, #DAA520 70%, #B8860B 100%);
                border-style: inset;
            }
            QLineEdit {
                background: rgba(255, 248, 220, 0.9);
                border: 4px solid #8B7355;
                border-style: groove;
                padding: 12px;
                border-radius: 15px;
                color: #2F1B14;
                font-family: 'Times New Roman', serif;
                font-weight: bold;
            }
            QLabel {
                color: #FFD700;
                font-weight: bold;
                font-family: 'Times New Roman', serif;
            }
            QComboBox {
                background: rgba(255, 248, 220, 0.9);
                border: 4px solid #8B7355;
                border-style: groove;
                padding: 10px;
                border-radius: 15px;
                color: #2F1B14;
                font-family: 'Times New Roman', serif;
                font-weight: bold;
            }
        """
    def _vampire_theme(self) -> str:
        """🧛 Vampire Theme - Düster und blutig"""
        return """
            QMainWindow {
                background: qradial-gradient(circle, #330000 0%, #1a0000 50%, #000000 100%);
                color: #cc0000;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 rgba(0,0,0,0.9), stop:0.5 rgba(51,0,0,0.7), stop:1 rgba(0,0,0,0.9));
                border: 3px solid #cc0000;
                color: #ffcccc;
                border-radius: 15px;
                font-family: 'Georgia', serif;
                font-weight: bold;
                font-style: italic;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #cc0000, stop:0.5 #990000, stop:1 #660000);
                border: 2px solid #330000;
                color: #ffcccc;
                padding: 12px;
                border-radius: 10px;
                font-weight: bold;
                font-family: 'Georgia', serif;
                font-style: italic;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #ff0000, stop:0.5 #cc0000, stop:1 #990000);
                color: #ffffff;
                border: 3px solid #cc0000;
            }
            QLineEdit {
                background: rgba(0,0,0,0.8);
                border: 2px solid #cc0000;
                padding: 10px;
                border-radius: 10px;
                color: #cc0000;
                font-family: 'Georgia', serif;
                font-weight: bold;
                font-style: italic;
            }
            QLabel {
                color: #cc0000;
                font-weight: bold;
                font-family: 'Georgia', serif;
                font-style: italic;
            }
            QComboBox {
                background: rgba(0,0,0,0.8);
                border: 2px solid #cc0000;
                padding: 8px;
                border-radius: 10px;
                color: #cc0000;
                font-family: 'Georgia', serif;
                font-weight: bold;
                font-style: italic;
            }
        """
    def _alien_theme(self) -> str:
        """👽 Alien Theme - Außerirdisch und mysteriös"""
        return """
            QMainWindow {
                background: qradial-gradient(circle, #001a33 0%, #003366 30%, #000d1a 100%);
                color: #66ffcc;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(0,26,51,0.8), stop:0.5 rgba(0,51,102,0.6), stop:1 rgba(0,13,26,0.8));
                border: 3px solid #66ffcc;
                border-style: dotted;
                color: #ccffff;
                border-radius: 20px;
                font-family: 'Arial', sans-serif;
                font-weight: bold;
            }
            QPushButton {
                background: qradial-gradient(circle, #66ffcc 0%, #33cc99 50%, #006633 100%);
                border: 2px solid #66ffcc;
                color: #000d1a;
                padding: 12px;
                border-radius: 20px;
                font-weight: bold;
                font-family: 'Arial', sans-serif;
                text-}
            QPushButton:hover {
                background: qradial-gradient(circle, #99ffdd 0%, #66ffcc 50%, #33cc99 100%);
                color: #000000;
                border: 3px solid #66ffcc;
            }
            QLineEdit {
                background: rgba(0,13,26,0.9);
                border: 2px solid #66ffcc;
                border-style: dashed;
                padding: 10px;
                border-radius: 15px;
                color: #66ffcc;
                font-family: 'Arial', sans-serif;
                font-weight: bold;
            }
            QLabel {
                color: #66ffcc;
                font-weight: bold;
                font-family: 'Arial', sans-serif;
            }
            QComboBox {
                background: rgba(0,13,26,0.9);
                border: 2px solid #66ffcc;
                border-style: dashed;
                padding: 8px;
                border-radius: 15px;
                color: #66ffcc;
                font-family: 'Arial', sans-serif;
                font-weight: bold;
            }
        """
    def _wasteland_theme(self) -> str:
        """🏜️ Wasteland Theme - Ödland und Staub"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #8B7355, stop:0.3 #A0522D, stop:0.7 #D2691E, stop:1 #654321);
                color: #F4A460;
            }
            QListWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(139,115,85,0.8), stop:1 rgba(160,82,45,0.9));
                border: 4px solid #8B4513;
                border-style: groove;
                color: #FFFAF0;
                border-radius: 5px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #D2691E, stop:0.5 #CD853F, stop:1 #A0522D);
                border: 3px solid #654321;
                border-style: ridge;
                color: #FFFAF0;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-family: 'Courier New', monospace;
                text-}
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #F4A460, stop:0.5 #DEB887, stop:1 #D2691E);
                border-style: inset;
            }
            QLineEdit {
                background: rgba(255, 248, 220, 0.7);
                border: 3px solid #8B4513;
                border-style: inset;
                padding: 8px;
                border-radius: 5px;
                color: #654321;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            QLabel {
                color: #F4A460;
                font-weight: bold;
                font-family: 'Courier New', monospace;
            }
            QComboBox {
                background: rgba(255, 248, 220, 0.7);
                border: 3px solid #8B4513;
                border-style: inset;
                padding: 6px;
                border-radius: 5px;
                color: #654321;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
        """
    def _neon_theme(self) -> str:
        """💫 Neon Theme - Glühende Neonlichter"""
        return """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #000014, stop:0.25 #1a0033, stop:0.5 #330066, 
                    stop:0.75 #1a0033, stop:1 #000014);
                color: #00ffff;
            }
            QListWidget {
                background: rgba(0,0,0,0.9);
                border: 3px solid #00ffff;
                color: #ffffff;
                border-radius: 15px;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff0080, stop:0.33 #00ff80, stop:0.66 #8000ff, stop:1 #ff0080);
                border: 2px solid #ffffff;
                color: #ffffff;
                padding: 12px;
                border-radius: 12px;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
                text-}
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #ff4da6, stop:0.33 #4dff99, stop:0.66 #a64dff, stop:1 #ff4da6);
                border: 3px solid #ffffff;
            }
            QLineEdit {
                background: rgba(0,0,0,0.8);
                border: 2px solid #00ffff;
                padding: 12px;
                border-radius: 12px;
                color: #00ffff;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
            QLabel {
                color: #00ffff;
                font-weight: bold;
                font-family: 'Arial Black', sans-serif;
            }
            QComboBox {
                background: rgba(0,0,0,0.8);
                border: 2px solid #00ffff;
                padding: 10px;
                border-radius: 12px;
                color: #00ffff;
                font-family: 'Arial Black', sans-serif;
                font-weight: bold;
            }
        """