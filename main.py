from PyQt5 import QtWidgets, QtCore
from untitled import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
            super(mywindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowTitle("Converter")

            self.ui.pushButton.clicked.connect(self.btnClicked)

            self.ui.comboBox.addItem("Рублей")
            self.ui.comboBox.addItem("Долларов")
            self.ui.comboBox_2.addItem("Долларов")
            self.ui.comboBox_2.addItem("Рублей")

            self.textbox = self.ui.lineEdit
            self.combobox1 = self.ui.comboBox
            self.combobox2 = self.ui.comboBox_2

    def btnClicked(self):
            textboxValue = int(self.textbox.text())
            comboboxValue1 = self.combobox1.currentText()
            comboboxValue2 = self.combobox2.currentText()
            if comboboxValue1 == "Рублей" and comboboxValue2 == "Долларов":
                self.ui.lineEdit_2.setText(str(textboxValue / 74.35))

            if comboboxValue1 == "Долларов" and comboboxValue2 == "Рублей":
                self.ui.lineEdit_2.setText(str(textboxValue * 74.35))


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())