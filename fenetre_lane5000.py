from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QComboBox, QLineEdit, QGridLayout
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize
from GROUPS_File import GroupePositions

from Automatique import ModeAuto     # IMPORT MODE AUTOMATIQUE


class Lane5000UI(QWidget,GroupePositions):
    def __init__(self, switch_page_callback):
        super().__init__()
        self.saved_colors = {}  # dictionnaire des couleurs sauvegardées
        
        # ----- RESET COMPLET À L'ENTRÉE DE LA PAGE -----
        self.auto = ModeAuto(self)
        self.saved_colors.clear()
        self.auto.init_csv()
        
        self.setStyleSheet("background-color: #003366; color: white;")
        self.setFixedSize(900, 700)

        print(">>> RESET COMPLET : CSV vidé + couleurs remises à zéro")




        # =====================================================
        # LAYOUT PRINCIPAL
        # =====================================================
        root = QVBoxLayout(self)
        root.setContentsMargins(20, 16, 20, 16)
        root.setSpacing(12)

        # =====================================================
        # HEADER
        # =====================================================
        header = QHBoxLayout()
        header.setSpacing(10)

        self.combo_group = QComboBox()
        self.combo_group.addItems(["A", "B", "C", "D", "E"])
        self.combo_group.setStyleSheet("QComboBox { background-color: white; color: black; font-weight: bold; }")
        self.combo_group.setFixedWidth(90)
        self.combo_group.currentTextChanged.connect(self.update_grid)

        title = QLabel("Lane5000")
        title.setFont(QFont("Arial", 28, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        rightHeader = QHBoxLayout()
        rightHeader.setSpacing(8)

        # ---- CARTE ----
        self.combo_card = QComboBox()                      # IMPORTANT
        self.combo_card.addItems(["Card 1", "Card 2", "Card 3"])
        self.combo_card.setStyleSheet("QComboBox { background-color: white; color: black; font-weight: bold; }")
        self.combo_card.setFixedWidth(120)

        # créer la liste des cartes
        self.optionListCard = [self.combo_card.itemText(i) for i in range(self.combo_card.count())]

        # ---- MODE ----
        self.combo_mode = QComboBox()
        self.combo_mode.addItems(["Automatique", "Manuel"])
        self.combo_mode.setStyleSheet("QComboBox { background-color: white; color: black; font-weight: bold; }")
        self.combo_mode.setFixedWidth(130)

        # ---- BOUTON RETOUR ----

        rightHeader.addWidget(self.combo_card)
        rightHeader.addWidget(self.combo_mode)


        header.addWidget(self.combo_group)
        header.addStretch()
        header.addWidget(title)
        header.addStretch()
        header.addLayout(rightHeader)

        root.addLayout(header)

        # =====================================================
        # GRILLE DE CERLES
        # =====================================================
        root.addStretch(1)

        center = QHBoxLayout()
        center.addStretch()

        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(22)
        self.grid_layout.setVerticalSpacing(22)
        self.auto = ModeAuto(self)
        self.auto.load_csv_colors()

        self.circle_buttons = []
        self.update_grid("A")

        center.addLayout(self.grid_layout)
        center.addStretch()
        root.addLayout(center)

        root.addStretch(1)

                # =====================================================
        # BAS DE PAGE : BOUTON RETOUR + BOUTON RUN
        # =====================================================
        bottom = QHBoxLayout()
        bottom.setSpacing(30)

        # ---- BOUTON RETOUR ----
        btn_back = QPushButton("RETOUR")
        btn_back.setStyleSheet(
            "QPushButton { background-color: #FF4444; color: white; font-size: 18px; font-weight: bold;"
            " border-radius: 10px; padding: 12px 26px; }"
            "QPushButton:hover { background-color: #DD3333; }"
        )
        btn_back.clicked.connect(lambda: switch_page_callback(2))

        # ---- BOUTON RUN ----
        self.btn_run = QPushButton("RUN")
        self.btn_run.setStyleSheet(
            "QPushButton { background-color: #00FF66; color: black; font-size: 18px; font-weight: bold;"
            " border-radius: 10px; padding: 12px 26px; }"
            "QPushButton:hover { background-color: #00DD55; }"
        )
        self.btn_run.clicked.connect(self.launch_automatic_script)

        bottom.addWidget(btn_back)
        bottom.addStretch()
        bottom.addWidget(self.btn_run)

        root.addLayout(bottom)

    # =====================================================
    # BOUTONS DESACTIVÉS
    # =====================================================
    def disable_button(self):
        self.combo_card.setEnabled(False)
        self.combo_group.setEnabled(False)
        self.combo_mode.setEnabled(False)
        self.btn_run.setEnabled(False)
        
    
    # =====================================================
    # BOUTONS ACTIVÉS
    # =====================================================
        
    def enable_button(self):
        self.combo_card.setEnabled(True)
        self.combo_group.setEnabled(True)
        self.combo_mode.setEnabled(True)
        self.btn_run.setEnabled(True)
        
    # =====================================================
    # LANCEMENT DU MODE AUTOMATIQUE
    # =====================================================
    def launch_automatic_script(self):
        print("\n>>> DÉBUT MODE AUTOMATIQUE\n")
        self.saved_colors.clear()
        self.auto.init_csv()
        self.auto = ModeAuto(self)
        self.disable_button()
        self.auto.load_csv_colors()
        self.auto.run()
      

    # =====================================================
    # RETROUVER UN BOUTON AVEC SA POSITION
    # =====================================================
    def get_button_at(self, row, col):
        item = self.grid_layout.itemAtPosition(row, col)
        if item:
            return item.widget()
        return None

    # =====================================================
    # METTRE UN CERCLE A UNE COULEUR
    # =====================================================
    def set_color(self, button, color):
        mapping = {
            "green": "green",
            "red": "red",
            "yellow": "yellow",
            "default": "#DDDDDD"
        }
        button.setStyleSheet(
            f"QPushButton {{ background-color: {mapping.get(color, '#DDDDDD')}; border-radius: 25px; }}"
        )

    # =====================================================
    # SIMULATION DE lecture_son()
    # =====================================================
    def lecture_son(self):
        v=True
        return v

    # =====================================================
    # METTRE A JOUR LA GRILLE
    # =====================================================
    def update_grid(self, group_name):

        # Effacer la grille
        for i in reversed(range(self.grid_layout.count())):
            w = self.grid_layout.itemAt(i).widget()
            if w:
                w.setParent(None)

        # Recréer les boutons
        for row, col in self.groups_positions[group_name]:
            btn = QPushButton()
            btn.setFixedSize(50, 50)

            # Chercher la couleur depuis saved_colors
            color = self.saved_colors.get((group_name, row, col), "default")

            if color == "default":
                btn.setStyleSheet("QPushButton { background-color: #DDDDDD; border-radius: 25px; }")
            else:
                btn.setStyleSheet(f"QPushButton {{ background-color: {color}; border-radius: 25px; }}")

            self.grid_layout.addWidget(btn, row, col)
