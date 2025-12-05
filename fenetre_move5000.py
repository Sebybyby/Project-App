from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Move5000UI(QWidget):
    def __init__(self, switch_page_callback):
        super().__init__()
        self.setStyleSheet("background-color: #003366; color: white;")

        layout = QVBoxLayout()

        label = QLabel("Page Move5000")
        label.setFont(QFont("Arial", 24))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        back_btn = QPushButton("Retour")
        back_btn.setStyleSheet("background-color: yellow; font-size: 16px;")
        back_btn.clicked.connect(lambda: switch_page_callback(2))

        layout.addWidget(label)
        layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)