from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class CombinationUI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        # Fond bleu foncé + texte blanc
        self.setStyleSheet("background-color: #003366; color: white;")

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)

        #  Barre supérieure : bouton retour + titre
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
        back_btn.clicked.connect(lambda: switch_page_callback(0))  # Retour au menu

        title = QLabel("Combination Test")
        title.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: white;")

        # Ajout dans la barre supérieure
        top_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        top_layout.addStretch()
        top_layout.addWidget(title)
        top_layout.addStretch()

        #  Layout pour les 3 boutons circulaires
        button_layout = QHBoxLayout()

        btn_lane = QPushButton("Lane5000")
        btn_lane.setFixedSize(140, 140)
        btn_lane.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                border-radius: 70px;
                font-size: 16px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #FFD700;
            }
        """)
        btn_lane.clicked.connect(lambda: switch_page_callback(3))  # Page Lane5000

        btn_move = QPushButton("Move5000")
        btn_move.setFixedSize(140, 140)
        btn_move.setStyleSheet(btn_lane.styleSheet())
        btn_move.clicked.connect(lambda: switch_page_callback(4))  # Page Move5000

        btn_move = QPushButton("Move5000")
        btn_move.setFixedSize(140, 140)
        btn_move.setStyleSheet(btn_lane.styleSheet())
        btn_move.clicked.connect(lambda: switch_page_callback(8))  # Page Move5000


        button_layout.addStretch()
        button_layout.addWidget(btn_lane)
        button_layout.addSpacing(40)
        button_layout.addWidget(btn_move)

 
        button_layout.addStretch()

        #  Layout pour les boutons rectangulaires en bas
        bottom_layout = QHBoxLayout()

        doc_btn = QPushButton("Création Document")
        doc_btn.setFixedSize(150, 80)
        doc_btn.setStyleSheet("""
            QPushButton {
                background-color: #E0E0E0;
                font-size: 14px;
                font-weight: bold;
                color: black;
                border: 2px solid black;
            }
            QPushButton:hover {
                background-color: #C0C0C0;
            }
        """)
        doc_btn.clicked.connect(lambda: switch_page_callback(5))  # Page Document

        sound_btn = QPushButton("Paramétrage\nSon")
        sound_btn.setFixedSize(150, 80)
        sound_btn.setStyleSheet(doc_btn.styleSheet())
        sound_btn.clicked.connect(lambda: switch_page_callback(6))  # Page Son

        robot_btn = QPushButton("Paramétrage\nTest")
        robot_btn.setFixedSize(150, 80)
        robot_btn.setStyleSheet(doc_btn.styleSheet())
        robot_btn.clicked.connect(lambda: switch_page_callback(7))  # Page Test

        bottom_layout.addWidget(doc_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        bottom_layout.addStretch()
        bottom_layout.addWidget(sound_btn)
        bottom_layout.addStretch()
        bottom_layout.addWidget(robot_btn, alignment=Qt.AlignmentFlag.AlignRight)

        #  Logo Thales en bas
        logo_label = QLabel("THALES\nIMT\nRF DEVELOPMENT TEAM")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet("color: white; font-size: 12px; margin-top: 20px;")

        #  Ajout des sections au layout principal
        main_layout.addLayout(top_layout)
        main_layout.addSpacing(30)
        main_layout.addLayout(button_layout)
        main_layout.addSpacing(50)
        main_layout.addLayout(bottom_layout)
        main_layout.addWidget(logo_label)

        self.setLayout(main_layout)