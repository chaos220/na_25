import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox


# some other widgets: QLineEdit, QRadioButton, QComboBox, QCheckBox, QMenuBar, QToolBar, QTab, QScrollBar
#                     QSplitter, QDock


# Layouts and themes: QBoxLayout, QGridLayout

def dialog():
  mbox = QMessageBox()
  mbox.setText("Your allegiance has been noted")
  mbox.setDetailedText("Please report to headquarters within the next 18 hrs")
  mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

  mbox.exec_()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  app.setStyle("Fusion")
  w   = QWidget()
  w.resize(300,300)
  w.setWindowTitle("Alina HoJung Na")

  label = QLabel(w)
  label.setText("Welcome to Akela World")
  label.move(75,100)
  label.show()

  btn = QPushButton(w)
  btn.setText("Pledge Allegiance")
  btn.move(87,120)
  btn.show()
  btn.clicked.connect(dialog)
  #widget.signal.connect(slot)

  w.show()
  sys.exit(app.exec_())


