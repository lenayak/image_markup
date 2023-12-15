import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from main_window import Ui_image_markup

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    image_markup = QtWidgets.QMainWindow()
    ui = Ui_image_markup()
    ui.setupUi(image_markup)
    image_markup.show()
    sys.exit(app.exec_())
