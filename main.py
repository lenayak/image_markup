import sys

import cv2
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage

import main_window
import save_question


class Window(QtWidgets.QMainWindow, main_window.Ui_image_markup):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.img_filename = " "
        self.img = None
        self.widget = None
        self.tmp = None  # фотография, с которой мы будем работать
        self.get_img_btn.clicked.connect(self.load_image)  # загружаем фотографию
        self.mark_up_btn.clicked.connect(self.mark_up)  # размечаем фотографию
        self.done_btn.clicked.connect(self.show_widget)  # спрашиваем про сохранение

    def load_image(self):
        """This function load the user selected image and set it to
           label using setPhoto function.
        """
        try:
            self.img_filename = QFileDialog.getOpenFileName(filter='Image (*.*)')[0]
            self.img = cv2.imread(self.img_filename)
            self.set_photo(self.img)
        except:
            self.img_filename = None
            self.tmp = None
            self.image.setText("<center>Could not open file. Try again.</center>")

    def set_photo(self, image):
        """This function take image input and resize it
           only for display purpose and convert it to QImage to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image, width=371)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.image.setPixmap(QtGui.QPixmap.fromImage(image))

    def mark_up(self):
        """This function mark up the photo"""
        if self.tmp is not None:
            self.get_img_btn.close()
            self.edit_btn.show()
            self.mark_up_btn.close()
            self.done_btn.show()
            try:
                self.image.setText("<center> Loading... </center>")
                # функция для разметки фотографии
            except:
                self.image.setText("<center>Something is wrong</center>")
                # если что-то вдруг пошло не так
        else:
            self.image.setText("<center>You didn't select the image. Try again.</center>")

    def show_widget(self):
        """This function shows the window with a question about saving a file"""
        self.widget = Widget()
        self.widget.show()

class Widget(QtWidgets.QWidget, save_question.Ui_Save_question):
    def __init__(self):
        super(Widget, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
