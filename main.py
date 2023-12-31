from PySide6.QtGui import QMouseEvent, QAction, QPalette, QColor
from PySide6.QtWidgets import *

import sys

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget1 = Color('red')

        self.setWindowTitle("Akela")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200,900)

        self.button = QPushButton("Press me")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))
        
        layout1.addLayout(layout2)

        layout3.addWidget(Color('purple'))
        layout3.addWidget(Color('orange'))
        layout3.addWidget(self.button)

        layout1.addLayout(layout3)
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        # layout.addWidget(self.button)
        layout.addWidget(self.widget1)

        container = QWidget()
        container.setLayout(layout1)

        self.setCentralWidget(container)

        self.show()

    def button_clicked(self):
        print("Button was clicked")

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos()) 
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()