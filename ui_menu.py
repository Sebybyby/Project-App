from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MenuUI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # Style général : fond bleu foncé
        self.setStyleSheet("background-color: #003366;")

        # Layout principal vertical
        main_layout = QVBoxLayout()

        # Titre centré en haut
        title = QLabel("UR5 TEST Menu Principal")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: white; margin-top: 30px;")

        # Layout horizontal pour les deux boutons
        button_layout = QHBoxLayout()

        # Bouton SoftPos
        btn_softpos = QPushButton("SoftPos")
        btn_softpos.setFixedSize(160, 160)
        btn_softpos.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                border-radius: 80px; /* Rond */
                font-size: 18px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #FFD700; /* Hover doré */
            }
        """)
        # Action : aller à la page SoftPos (index 1)
        btn_softpos.clicked.connect(lambda: switch_page_callback(1))

        # Bouton CombinationTest
        btn_combination = QPushButton("CombinationTest")
        btn_combination.setFixedSize(160, 160)
        btn_combination.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                border-radius: 80px;
                font-size: 16px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #FFD700;
            }
        """)
        # Action : aller à la page CombinationTest (index 2)
        btn_combination.clicked.connect(lambda: switch_page_callback(2))

        # Ajout des boutons dans le layout horizontal
        button_layout.addStretch()
        button_layout.addWidget(btn_softpos)
        button_layout.addSpacing(60)
        button_layout.addWidget(btn_combination)
        button_layout.addStretch()

        # Ajout du titre et des boutons dans le layout principal
        main_layout.addWidget(title)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)