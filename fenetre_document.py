from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit,
    QVBoxLayout, QHBoxLayout, QFrame
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from Creation_Fichier_Excel import ExcelFileCreator


class DocumentUI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()

        self.setStyleSheet("background-color: #003366; color: white;")
        self.setFixedSize(900, 700)

        # Variables pour stocker les valeurs
        self.data = {"operateur": "", "antenne": "", "projet": ""}

        root = QVBoxLayout(self)
        root.setContentsMargins(30, 20, 30, 20)
        root.setSpacing(20)

        # =====================================================
        # HEADER + RETOUR JAUNE
        # =====================================================
        header = QHBoxLayout()

        back_btn = QPushButton("Retour")
        back_btn.setFixedSize(140, 45)
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

        header.addWidget(back_btn)
        header.addStretch()
        root.addLayout(header)

        # =====================================================
        # TITRE
        # =====================================================
        title = QLabel("Formulaire")
        title.setFont(QFont("Arial", 30, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        root.addWidget(title)

        root.addStretch()

        # =====================================================
        # CADRE DES CHAMPS
        # =====================================================
        frame = QFrame()
        frame.setFrameShape(QFrame.Panel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setLineWidth(3)
        frame.setStyleSheet("""
            QFrame {
                border: 3px solid white;
                background-color: #004A75;
            }
        """)

        frame_layout = QVBoxLayout(frame)
        frame_layout.setContentsMargins(40, 30, 40, 30)
        frame_layout.setSpacing(35)

        # ---- Opérateur ----
        lbl1 = QLabel("Opérateur :")
        lbl1.setFont(QFont("Arial", 20, QFont.Bold))
        self.input_operateur = QLineEdit()
        self.input_operateur.setFixedHeight(40)
        self.input_operateur.setStyleSheet("background-color: white; color: black; font-size: 18px;")

        row1 = QHBoxLayout()
        row1.addWidget(lbl1)
        row1.addWidget(self.input_operateur)
        frame_layout.addLayout(row1)

        # ---- Antenne ----
        lbl2 = QLabel("Antenne :")
        lbl2.setFont(QFont("Arial", 20, QFont.Bold))
        self.input_antenne = QLineEdit()
        self.input_antenne.setFixedHeight(40)
        self.input_antenne.setStyleSheet("background-color: white; color: black; font-size: 18px;")

        row2 = QHBoxLayout()
        row2.addWidget(lbl2)
        row2.addWidget(self.input_antenne)
        frame_layout.addLayout(row2)

        # ---- Projet ----
        lbl3 = QLabel("Nom du projet :")
        lbl3.setFont(QFont("Arial", 20, QFont.Bold))
        self.input_projet = QLineEdit()
        self.input_projet.setFixedHeight(40)
        self.input_projet.setStyleSheet("background-color: white; color: black; font-size: 18px;")

        row3 = QHBoxLayout()
        row3.addWidget(lbl3)
        row3.addWidget(self.input_projet)
        frame_layout.addLayout(row3)

        root.addWidget(frame)
        root.addStretch()

        # =====================================================
        # BOUTON VALIDER
        # =====================================================
        btn_valider = QPushButton("Valider")
        btn_valider.setFixedSize(220, 55)
        btn_valider.setStyleSheet("""
            QPushButton {
                background-color: yellow;
                font-size: 20px;
                font-weight: bold;
                color: black;
            }
            QPushButton:hover {
                background-color: #FFD700;
            }
        """)
        btn_valider.clicked.connect(self.save_values)

        bottom = QHBoxLayout()
        bottom.addStretch()
        bottom.addWidget(btn_valider)
        bottom.addStretch()
        root.addLayout(bottom)

        root.addStretch()

    # =====================================================
    # SAUVEGARDE DES VALEURS
    # =====================================================
    def save_values(self):
        self.data["operateur"] = self.input_operateur.text()
        self.data["antenne"] = self.input_antenne.text()
        self.data["projet"] = self.input_projet.text()
        self.creationfile = ExcelFileCreator(self.data.get("projet", "Sheet1"))
        self.creationfile.create_file()
        
        print("\n=== FORMULAIRE VALIDÉ ===")
        print(self.data)
