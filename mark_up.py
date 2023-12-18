import sys

import cv2
import numpy as np


def mark_object(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    objects = cascade_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image


def edit_markup(image: object) -> object:
    cv2.imshow('Markup Editor', image)
    cv2.waitKey(0)
    if cv2.waitKey(1) == 27:
        sys.exit()


image = cv2.imread("C:\\Users\\lenay\\PycharmProjects\\image_markup\\second_img.webp")
marked_image = mark_object(image)
edit_markup(marked_image)
