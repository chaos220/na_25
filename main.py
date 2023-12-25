from PySide6.QtWidgets import *

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Akela")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200,900)

        button = QPushButton("Press me")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

        self.show()

    def button_clicked(self):
        print("Button was clicked")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()