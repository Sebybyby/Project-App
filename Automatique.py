import csv
import os
from datetime import datetime
from PySide6.QtCore import QTimer
from GROUPS_File import GroupePositions
from datetime import datetime





class ModeAuto(GroupePositions):

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.points = []
        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.step)

        self.csv_file = "resultats_lane.csv"
        
        self.group_order = ["A", "B", "C", "D", "E"]
        self.current_group_index = 0


    # -------------------------
    # CSV
    # -------------------------
    def init_csv(self):
        with open(self.csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "group", "index", "row", "col", "trans"])
        print("[CSV] Réinitialisé :", self.csv_file)


    def write_csv(self, group, index, row, col, trans):
        with open(self.csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                group,
                index,
                row,
                col,
                trans
            ])
        print(f"[CSV] → Enregistré : {group} / {index} / ({row},{col}) / {trans}")
        
    def load_csv_colors(self):
        # Si le CSV n'existe pas encore, ne rien faire
        if not os.path.exists(self.csv_file):
            return

        with open(self.csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for line in reader:
                group = line["group"]
                row = int(line["row"])
                col = int(line["col"])
                trans = line["trans"]

                # Convertir en couleur
                if trans == "True":
                    color = "green"
                elif trans == "False":
                    color = "red"
                else:
                    color = "yellow"

                # Stocker dans l'UI
                self.ui.saved_colors[(group, row, col)] = color





    # -------------------------
    # START
    # -------------------------
    def run(self):
        print("=== MODE AUTOMATIQUE DÉMARRÉ ===")

        # On ne réinitialise pas le CSV si tu veux conserver l'historique
        # self.init_csv(force=True)

        # Charger toutes les couleurs depuis le CSV

        self.load_csv_colors()

        self.current_group_index = 0
        self.load_group()




    # -------------------------
    # CHARGER UN GROUPE
    # -------------------------
    def load_group(self):
        if self.current_group_index >= len(self.group_order):
            print("=== FIN DE TOUS LES GROUPES ===")
            self.timer.stop()
            
            self.ui.enable_button()
            return

        self.group = self.group_order[self.current_group_index]
        print(f"\n=== NOUVEAU GROUPE : {self.group} ===")

        self.points = self.groups_positions[self.group]
        self.index = 0

        # Affichage visuel du groupe
        self.ui.combo_group.setCurrentText(self.group)
        self.ui.update_grid(self.group)

        # Lancer le timer (1 point / 200 ms)
        self.timer.start(200)


    # -------------------------
    # TRAITER UN POINT
    # -------------------------
    def step(self):
        if self.index >= len(self.points):
            print(f"--- Groupe {self.group} terminé ---")
            self.current_group_index += 1
            self.load_group()
            return

        row, col = self.points[self.index]
        print(f"[{self.group}] point {self.index} → {row},{col}")

        btn = self.ui.get_button_at(row, col)

        # Lire TRANS
        Trans = self.ui.lecture_son()
        print("Trans =", Trans)
        if Trans is True:
            self.ui.set_color(btn, "green")
            color = "green"
        elif Trans is False:
            self.ui.set_color(btn, "red")
            color = "red"
        else:
            self.ui.set_color(btn, "yellow")
            color = "yellow"
        
        
        # Sauvegarder la couleur
        self.ui.saved_colors[(self.group, row, col)] = color

        # Écrire dans le CSV
        self.write_csv(self.group, self.index, row, col, Trans)

        self.index += 1
