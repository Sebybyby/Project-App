from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys
from ui_menu import MenuUI
from fenetre_softpos import SoftPosUI
from fenetre_combination import CombinationUI
from fenetre_document import DocumentUI
from fenetre_lane5000 import Lane5000UI
from fenetre_move5000 import Move5000UI
from fenetre_sound import SoundUI
from fenetre_test import TestUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Principal")
        self.setFixedSize(900, 700)
        # QStackedWidget permet de gérer plusieurs pages dans la même fenêtre
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        
        # Appliquer le fond bleu foncé à la fenêtre principale
        self.setStyleSheet("background-color: #003366;")  # Bleu marine


        # Création des pages et passage de la fonction switch_page pour la navigation
        menu_page = MenuUI(self.switch_page)
        softpos_page = SoftPosUI(self.switch_page)
        combination_page = CombinationUI(self.switch_page)
        Lane5000UI_page= Lane5000UI(self.switch_page)
        Move5000UI_page= Move5000UI(self.switch_page)
        DocumentUI_page= DocumentUI(self.switch_page)
        SoundUI_page= SoundUI(self.switch_page)
        TestUI_page= TestUI(self.switch_page)

        # Ajout des pages dans le stack (index 0 = menu, 1 = SoftPos, 2 = Combination)

        self.stack.addWidget(menu_page)        # index 0
        self.stack.addWidget(softpos_page)     # index 1
        self.stack.addWidget(combination_page) # index 2
        self.stack.addWidget(Lane5000UI_page)  # index 3
        self.stack.addWidget(Move5000UI_page)# index 4
        self.stack.addWidget(DocumentUI_page) # index 5
        self.stack.addWidget(SoundUI_page)     # index 6
        self.stack.addWidget(TestUI_page)      # index 7


    # Fonction pour changer de page en fonction de l'index
    def switch_page(self, index):
        self.stack.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
