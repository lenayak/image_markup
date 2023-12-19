import sys

import cv2
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage

import main_window
import mark_up


class Window(QtWidgets.QMainWindow, main_window.Ui_image_markup):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.img_filename = " "
        self.path_to_save = " "
        self.img = None
        self.widget = None
        self.tmp = None  # фотография
        self.marked_image = None
        self.get_img_btn.clicked.connect(self.load_image)  # загружаем фотографию
        self.mark_up_btn.clicked.connect(self.mark_up)  # размечаем фотографию
        self.save_btn.clicked.connect(self.save_img)  # сохраняем

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
        if self.img is not None:
            self.get_img_btn.close()
            self.mark_up_btn.close()
            self.save_btn.show()
            try:
                self.marked_image = mark_up.mark_image(self.img)
                self.set_photo(self.marked_image)
            except:
                self.image.setText("<center>Something is wrong</center>")
                # если что-то вдруг пошло не так
        else:
            self.image.setText("<center>You didn't select the image. Try again.</center>")

    def save_img(self):
        try:
            self.path_to_save = "marked_image.jpg"  # исправить захардкоженный путь
            mark_up.save_marked_image(self.path_to_save, self.marked_image)
            self.image.setText("<center>Thank you for using this app!</center>")
        except:
            self.image.setText("<center>Something is wrong</center>")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
