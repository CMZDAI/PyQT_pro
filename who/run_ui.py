# coding = utf-8
# Author: Happy curiosity
# Write time：2022/10/6 11:30
# Dear Egger
# File : run_ui.py

from who import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(Ui_MainWindow, QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())