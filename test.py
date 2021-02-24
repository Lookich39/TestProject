from PyQt5 import QtGui, QtWidgets, uic
from untitled import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):

    def init(self):
       # super(mywindow, self).init()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
