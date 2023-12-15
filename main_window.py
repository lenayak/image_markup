import cv2
import imutils
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage


class Ui_image_markup(object):
    def setupUi(self, image_markup):
        image_markup.setObjectName("image_markup")
        image_markup.resize(450, 380)
        image_markup.setBaseSize(QtCore.QSize(0, 0))
        image_markup.setStyleSheet("background-color:rgb(236, 236, 236)")
        self.centralwidget = QtWidgets.QWidget(image_markup)
        self.centralwidget.setObjectName("centralwidget")
        self.mark_up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mark_up_btn.setGeometry(QtCore.QRect(230, 290, 181, 31))
        self.mark_up_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.mark_up_btn.setObjectName("mark_up_btn")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 20, 371, 251))
        self.image.setObjectName("image")
        self.get_img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_img_btn.setGeometry(QtCore.QRect(30, 290, 181, 31))
        self.get_img_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.get_img_btn.setObjectName("get_img_btn")
        image_markup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(image_markup)
        self.statusbar.setObjectName("statusbar")
        image_markup.setStatusBar(self.statusbar)

        self.retranslateUi(image_markup)
        self.get_img_btn.clicked.connect(self.loadImage)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(image_markup)

        self.img_filename = None  # hold path to image
        self.tmp = None  # hold temporary image for display

    def loadImage(self):
        """This function load the user selected image and set it to
           label using setPhoto function.
        """
        try:
            self.img_filename = QFileDialog.getOpenFileName(filter='Image (*.*)')[0]
            self.img = cv2.imread(self.img_filename)
            self.setPhoto(self.img)
        except:
            self.img_filename = None

    def setPhoto(self, image):
        """This function take image input and resize it
           only for display purpose and convert it to QImage to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image, width=371)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.image.setPixmap(QtGui.QPixmap.fromImage(image))

    def retranslateUi(self, image_markup):
        _translate = QtCore.QCoreApplication.translate
        image_markup.setWindowTitle(_translate("image_markup", "image markup"))
        self.mark_up_btn.setText(_translate("image_markup", "Mark up"))
        self.image.setText(_translate("image_markup", "<center> Your photo </center>"))
        self.get_img_btn.setText(_translate("image_markup", "Open"))
