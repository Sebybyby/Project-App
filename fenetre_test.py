
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class TestUI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # Fond bleu foncé + texte blanc
        self.setStyleSheet("background-color: #003366; color: white;")

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Barre supérieure : bouton retour
        top_layout = QHBoxLayout()
        back_btn = QPushButton("Retour")
        back_btn.setFixedSize(100, 40)
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                font-size: 14px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #FFD700;
            }
        """)
        back_btn.clicked.connect(lambda: switch_page_callback(2))
        title = QLabel("Paramétrage du Robot")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))

        top_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        top_layout.addSpacing(70)  # Espace entre le bouton et le titre
        top_layout.addWidget(title,alignment=Qt.AlignmentFlag.AlignCenter) 
        top_layout.addStretch()
        

        # Layout centré pour titre + boutons
        center_layout = QVBoxLayout()
        center_layout.setSpacing(40)
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)



        # Style commun pour les boutons jaunes
        button_style = """
            QPushButton {
                background-color: yellow;
                font-size: 16px;
                font-weight: bold;
                color: black;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FFD700;
            }
        """

        btn_connexion = QPushButton("Connexion au robot")
        btn_connexion.setStyleSheet(button_style)
        btn_connexion.setFixedHeight(50)

        btn_param_manuel = QPushButton("Position 0 : paramétrage manuel")
        btn_param_manuel.setStyleSheet(button_style)
        btn_param_manuel.setFixedHeight(50)

        center_layout.addWidget(btn_connexion)
        center_layout.addWidget(btn_param_manuel)

        # Ajout dans le layout principal
        main_layout.addLayout(top_layout)
        main_layout.addStretch()  # Pour centrer verticalement
        main_layout.addLayout(center_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)
