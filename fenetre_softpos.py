from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class SoftPosUI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # Fond bleu foncé + texte blanc
        self.setStyleSheet("background-color: #003366; color: white;")

        layout = QVBoxLayout()

        # Titre de la page
        label = QLabel("Page SoftPos")
        label.setFont(QFont("Arial", 24))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bouton retour vers le menu (index 0)
        back_btn = QPushButton("Retour")
        back_btn.setStyleSheet("background-color: yellow; font-size: 16px;")
        back_btn.clicked.connect(lambda: switch_page_callback(0))

        # Ajout des widgets dans le layout
        layout.addWidget(label)
        layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)