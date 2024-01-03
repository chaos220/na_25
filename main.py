from PySide6.QtGui import QMouseEvent, QAction, QPalette, QColor
from PySide6.QtWidgets import *
from PySide6 import QtCore

import sys, random

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class coordinates(QWidget):

    def __init__(self):
        super(coordinates, self).__init__()

        self.layout = QVBoxLayout(self)

        dms_layout = QGridLayout()
        dd_layout = QGridLayout()
        ddm_layout = QGridLayout()

        self.layout.addLayout(dms_layout)
        self.layout.addLayout(dd_layout)
        self.layout.addLayout(ddm_layout)

        dms_lat  = QLabel("Latitude")
        dms_long = QLabel("Longitude")
        dms_lat_inp  = QPlainTextEdit()
        dms_long_inp = QPlainTextEdit()

        dd_lat  = QLabel("Latitude")
        dd_long = QLabel("Longitude")
        dd_lat_inp  = QPlainTextEdit()
        dd_long_inp = QPlainTextEdit()

        ddm_lat  = QLabel("Latitude")
        ddm_long = QLabel("Longitude")
        ddm_lat_inp  = QPlainTextEdit()
        ddm_long_inp = QPlainTextEdit()


        dms_layout.addWidget(dms_lat,     0,0)
        dms_layout.addWidget(dms_long,    1,0)
        dms_layout.addWidget(dms_lat_inp, 0,1)
        dms_layout.addWidget(dms_long_inp,1,1)

        dd_layout.addWidget(dd_lat,     0,0)
        dd_layout.addWidget(dd_long,    1,0)
        dd_layout.addWidget(dd_lat_inp, 0,1)
        dd_layout.addWidget(dd_long_inp,1,1)

        ddm_layout.addWidget(ddm_lat,     0,0)
        ddm_layout.addWidget(ddm_long,    1,0)
        ddm_layout.addWidget(ddm_lat_inp, 0,1)
        ddm_layout.addWidget(ddm_long_inp,1,1)


        items = []
        for layout in (self.layout.itemAt(i) for i in range(self.layout.count())):
             for c in range(layout.count()):
                  items.append(layout.itemAt(c).widget())

        for i in items:
            if isinstance(i, QPlainTextEdit):
                i.setMaximumHeight(30)


        self.show()

class alina_compliments(QWidget):
    def __init__(self):
        super().__init__()
        self.comps = ["your eyes", 
                      "how strong you are", 
                      "your pretty face", 
                      "the way you search up songs by some lyric you remember instead of their name lool",
                      "the way you fit against me"]
        

        self.button = QPushButton("AKELA")
        self.text = QLabel("I like")
        self.text.setWordWrap(True)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.comps))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget1 = Color('red')

        self.setWindowTitle("Akela")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200,900)

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacked_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stacked_layout)

        self.button_r = QPushButton("RED")
        self.button_g = QPushButton("GREEN")
        self.button_b = QPushButton("BLUE")

        button_layout.addWidget(self.button_r)
        button_layout.addWidget(self.button_g)
        button_layout.addWidget(self.button_b)
        
        # self.stacked_layout.addWidget(coordinates())
        self.stacked_layout.addWidget(alina_compliments())
        self.stacked_layout.addWidget(coordinates())
        self.stacked_layout.addWidget(Color("blue"))

        self.button_r.pressed.connect(self.show_tab_r)
        self.button_g.pressed.connect(self.show_tab_g)
        self.button_b.pressed.connect(self.show_tab_b)

        container = QWidget()
        container.setLayout(page_layout)
        self.setCentralWidget(container)

        self.show()

    def show_tab_r(self):
        self.stacked_layout.setCurrentIndex(0)

    def show_tab_g(self):
        self.stacked_layout.setCurrentIndex(1)

    def show_tab_b(self):
        self.stacked_layout.setCurrentIndex(2)

    def button_clicked(self):
        print("Button was clicked")


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


"""
page 1 = lat/long conversions


page 2 = smth with akela, maybe picture slide show
pledge allegiance - some type of puzzle/code?

page 3 = song 

page 4 = to-do list or reminder 

"""