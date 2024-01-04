from PySide6.QtGui import QMouseEvent, QAction, QPalette, QColor, QRegularExpressionValidator
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

        self.dms_layout = QGridLayout()
        self.dd_layout = QGridLayout()
        self.ddm_layout = QGridLayout()

        self.dms_ns_layout = QHBoxLayout()
        self.dms_ew_layout = QHBoxLayout()

        self.ddm_ns_layout = QHBoxLayout()
        self.ddm_ew_layout = QHBoxLayout()

        self.layout.addLayout(self.dms_layout)
        self.layout.addLayout(self.dd_layout)
        self.layout.addLayout(self.ddm_layout)

        # only allow floating point numbers
        validator = QRegularExpressionValidator((r'[0-9]+.[0-9]+'), self)

        self.dms_label    = QLabel("DMS (Degrees, Minutes, Seconds)")
        self.dms_label.setStyleSheet("font-weight: bold")
        self.dms_lat      = QLabel("Latitude")
        self.dms_long     = QLabel("Longitude")
        self.dms_units    = [QLabel('"'), QLabel('"')]
        self.dms_lat_inp  = [QLineEdit(), QLineEdit(), QLineEdit()]
        self.dms_long_inp = [QLineEdit(), QLineEdit(), QLineEdit()]
        self.dms_convert  = QPushButton("Convert")
        self.dms_convert.clicked.connect(self.do_dms_convert)

        self.dms_ns_group = QButtonGroup(self)
        self.dms_ew_group = QButtonGroup(self)

        self.ddm_ns_group = QButtonGroup(self)
        self.ddm_ew_group = QButtonGroup(self)

        self.dms_radio_n  = QRadioButton("N")
        self.dms_radio_s  = QRadioButton("S")
        self.dms_radio_e  = QRadioButton("E")
        self.dms_radio_w  = QRadioButton("W")

        self.ddm_radio_n  = QRadioButton("N")
        self.ddm_radio_s  = QRadioButton("S")
        self.ddm_radio_e  = QRadioButton("E")
        self.ddm_radio_w  = QRadioButton("W")

        self.dms_radio_n.setChecked(True)
        self.dms_radio_e.setChecked(True)
        self.ddm_radio_n.setChecked(True)
        self.ddm_radio_e.setChecked(True)

        
        self.dms_ns_layout.addWidget(self.dms_radio_n)
        self.dms_ns_layout.addWidget(self.dms_radio_s)

        self.dms_ew_layout.addWidget(self.dms_radio_e)
        self.dms_ew_layout.addWidget(self.dms_radio_w)

        self.dms_ns_group.addButton(self.dms_radio_n, 0)
        self.dms_ns_group.addButton(self.dms_radio_s, 1)
        self.dms_ew_group.addButton(self.dms_radio_e, 0)
        self.dms_ew_group.addButton(self.dms_radio_w, 1)

        self.ddm_ns_group.addButton(self.ddm_radio_n, 0)
        self.ddm_ns_group.addButton(self.ddm_radio_s, 1)
        self.ddm_ew_group.addButton(self.ddm_radio_e, 0)
        self.ddm_ew_group.addButton(self.ddm_radio_w, 1)

        self.ddm_ns_layout.addWidget(self.ddm_radio_n)
        self.ddm_ns_layout.addWidget(self.ddm_radio_s)

        self.ddm_ew_layout.addWidget(self.ddm_radio_e)
        self.ddm_ew_layout.addWidget(self.ddm_radio_w)

        self.dd_label    = QLabel("DD (Decimal Degrees)")
        self.dd_label.setStyleSheet("font-weight: bold")
        self.dd_lat      = QLabel("Latitude")
        self.dd_long     = QLabel("Longitude")
        self.dd_lat_inp  = [QLineEdit()]
        self.dd_long_inp = [QLineEdit()]
        self.dd_convert  = QPushButton("Convert")
        self.dd_convert.clicked.connect(self.do_dd_convert)

        self.ddm_label    = QLabel("DDM (Degrees, Decimal Minutes)")
        self.ddm_label.setStyleSheet("font-weight: bold")
        self.ddm_lat      = QLabel("Latitude")
        self.ddm_long     = QLabel("Longitude")
        self.ddm_units    = [QLabel("'"), QLabel("'")]
        self.ddm_lat_inp  = [QLineEdit(), QLineEdit()]
        self.ddm_long_inp = [QLineEdit(), QLineEdit()]
        self.ddm_convert  = QPushButton("Convert")
        self.ddm_convert.clicked.connect(self.do_ddm_convert)

        # set all validators 
        for each in self.dms_lat_inp:  each.setValidator(validator)
        for each in self.dms_long_inp: each.setValidator(validator)
        for each in self.dd_lat_inp:   each.setValidator(validator)
        for each in self.dd_long_inp:  each.setValidator(validator)
        for each in self.ddm_lat_inp:  each.setValidator(validator)
        for each in self.ddm_long_inp: each.setValidator(validator)
        

        self.dms_layout.addWidget(self.dms_label,       0,0,1,3,QtCore.Qt.AlignLeft)
        self.dms_layout.addWidget(self.dms_lat,         1,0)
        self.dms_layout.addWidget(self.dms_long,        2,0)

        self.dms_layout.addWidget(self.dms_lat_inp[0],  1,1)
        self.dms_layout.addWidget(self.dms_long_inp[0], 2,1)
        self.dms_layout.addWidget(self.dms_lat_inp[1],  1,2)
        self.dms_layout.addWidget(self.dms_long_inp[1], 2,2)
        self.dms_layout.addWidget(self.dms_lat_inp[2],  1,3)
        self.dms_layout.addWidget(self.dms_long_inp[2], 2,3)
        
        self.dms_layout.addWidget(self.dms_units[0],    1,4)
        self.dms_layout.addWidget(self.dms_units[1],    2,4)
        self.dms_layout.addWidget(self.dms_convert,     3,0)
        self.dms_layout.addLayout(self.dms_ns_layout,   1,5)
        self.dms_layout.addLayout(self.dms_ew_layout,   2,5)

        self.dd_layout.addWidget(self.dd_label,       0,0,1,3,QtCore.Qt.AlignLeft)
        self.dd_layout.addWidget(self.dd_lat,         1,0)
        self.dd_layout.addWidget(self.dd_long   ,     2,0)
        self.dd_layout.addWidget(self.dd_lat_inp[0],  1,1)
        self.dd_layout.addWidget(self.dd_long_inp[0], 2,1)
        self.dd_layout.addWidget(self.dd_convert,     3,0)

        self.ddm_layout.addWidget(self.ddm_label,       0,0,1,3,QtCore.Qt.AlignLeft)
        self.ddm_layout.addWidget(self.ddm_lat,         1,0)
        self.ddm_layout.addWidget(self.ddm_long,        2,0)
        self.ddm_layout.addWidget(self.ddm_lat_inp[0],  1,1)
        self.ddm_layout.addWidget(self.ddm_long_inp[0], 2,1)
        self.ddm_layout.addWidget(self.ddm_lat_inp[1],  1,2)
        self.ddm_layout.addWidget(self.ddm_long_inp[1], 2,2)
        self.ddm_layout.addWidget(self.ddm_units[0],    1,3)
        self.ddm_layout.addWidget(self.ddm_units[1],    2,3)
        self.ddm_layout.addWidget(self.ddm_convert,     3,0)
        self.ddm_layout.addLayout(self.ddm_ns_layout,   1,4)
        self.ddm_layout.addLayout(self.ddm_ew_layout,   2,4)


        self.show()

    def do_dms_convert(self):
        print("DMS convert button pressed")
        self.check_empty(self.dms_lat_inp, self.dms_long_inp)
        print(self.dms_ns_group.checkedId())
        print(self.dms_ew_group.checkedId())

    def do_dd_convert(self):
        print("DD convert button pressed")
        self.check_empty(self.dd_lat_inp, self.dd_long_inp)

    def do_ddm_convert(self):
        print("DDM convert button pressed")
        self.check_empty(self.ddm_lat_inp, self.ddm_long_inp)
        print(self.ddm_ns_group.checkedId())
        print(self.ddm_ew_group.checkedId())

    
    def check_empty(self, lat_inps, long_imps):
        for (a,b) in zip(lat_inps, long_imps):
            if (a.text() == "" or b.text() == ""):
                self.empty_input_warning()
                break
            else:
                print(float(a.text()) + float(b.text()))

    def empty_input_warning(self):
        mbox = QMessageBox()
        mbox.setText("You have one or more empty inputs.")
        mbox.exec_()

class alina_compliments(QWidget):
    def __init__(self):
        super().__init__()
        self.comps = ["your eyes", 
                      "how strong you are", 
                      "your pretty face", 
                      "the way you search up songs by some lyric you remember instead of their name that you can't remember lool",
                      "the way you fit against me",
                      "your smile (I love it actually)",
                      "how you told me about your chopstick training and skills and then dropped a wonton on your lap immediately after",
                      "your laugh",
                      "how kind you are (to me at least :p)",
                      "how I can see your love for your family",
                      "your concentration when playing games haha",
                      "when you hug me",
                      "that sometimes you'll take a selfie/photo and send it because I asked you to",
                      "rock climbing with you (can we go again pls)",
                      "your hair, I feel like it suits you a lot you look really good with it down",
                      "(really like) how you brought akela to meet me when we went to rondeau",
                      "(LOVE) the clay pot you painted for me",
                      "that you bought me flowers :3",
                      "(love love love) eating / sharing food with you :D"]
        

        self.button = QPushButton("AKELA")
        self.text = QLabel("I like")
        self.text.setWordWrap(True)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.shuffle)

    def shuffle(self):
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


'''

class MoodExample(QGroupBox):

    def __init__(self):
        super(MoodExample, self).__init__()

        # Create an array of radio buttons
        moods = [QRadioButton("Happy"), QRadioButton("Sad"), QRadioButton("Angry")]

        # Set a radio button to be checked by default
        moods[0].setChecked(True)

        # Radio buttons usually are in a vertical layout
        button_layout = QVBoxLayout()

        # Create a button group for radio buttons
        self.mood_button_group = QButtonGroup()

        for i in xrange(len(moods)):
            # Add each radio button to the button layout
            button_layout.addWidget(moods[i])
            # Add each radio button to the button group & give it an ID of i
            self.mood_button_group.addButton(moods[i], i)
            # Connect each radio button to a method to run when it's clicked
            self.connect(moods[i], SIGNAL("clicked()"), self.radio_button_clicked)

        # Set the layout of the group box to the button layout
        self.setLayout(button_layout)

    #Print out the ID & text of the checked radio button
    def radio_button_clicked(self):
        print(self.mood_button_group.checkedId())
        print(self.mood_button_group.checkedButton().text())


'''