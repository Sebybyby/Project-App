from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import openpyxl
from PySide6.QtWidgets import QFileDialog

class SoundUI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()
        self.setStyleSheet("background-color: #003366; color: white;")

        layout = QVBoxLayout()

        label = QLabel("Paramétrage Son")
        label.setFont(QFont("Arial", 24))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bouton Choix du leceur 
        layoutmid = QVBoxLayout()


        Noise_lect = QPushButton("Choix du lecteur")
        Noise_lect.setStyleSheet("background-color: yellow; font-size: 32px;")
        Noise_lect.setFixedSize(300, 100)

        Noise_lect.clicked.connect(lambda: self.ouvrir_excel_lecteur())
        layoutmid.addWidget(Noise_lect, alignment=Qt.AlignmentFlag.AlignCenter)







        layoutbot = QVBoxLayout()




        back_btn = QPushButton("Retour")
        back_btn.setStyleSheet("background-color: yellow; font-size: 16px;")
        back_btn.clicked.connect(lambda: switch_page_callback(2))

        layoutbot.addWidget(label)
        layoutbot.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        layout.addLayout(layoutmid)
        layout.addLayout(layoutbot)

    def ouvrir_excel_lecteur(self):
        chemin_fichier = QFileDialog.getOpenFileName(self, "Sélectionner le lecteur par son fichier Excel", "", "Fichiers Excel (*.xlsx *.xls)")

        try : 
            classeur = openpyxl.load_workbook(chemin_fichier)

            feuille = classeur.active

            valeur1 = feuille['A1'].value
            print("Valeur A1 :", valeur1)

            valeur2 = feuille['B2'].value
            print("Valeur B2 :", valeur2)

            valeur3 = feuille['C3 '].value
            print("Valeur C3 :", valeur3)
        except Exception as e:
            print("Erreur lors de l'ouverture du fichier Excel :", e)
        
