import cv2


def mark_image(img):
    """This function marks up a photo using trained models, and shows the user the marked up photo in a large format"""
    models = [r'C:\Users\lenay\PycharmProjects\image_markup\haarcascade_car.xml',
              r'C:\Users\lenay\PycharmProjects\image_markup\haarcascade_fullbody.xml']
    load_model = load_models(models)
    detected_objects = []
    for i in load_model:
        obj = i.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1)
        detected_objects.append(obj)
    for obj in detected_objects:
        for x, y, width, height in obj:
            cv2.rectangle(img, pt1=(x, y), pt2=(x + width, y + height), color=(50, 50, 50), thickness=1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    return img


def load_models(models: list):
    """This function load models to mark up"""
    loaded = []
    for i in models:
        load_model = cv2.CascadeClassifier(i)
        loaded.append(load_model)
    return loaded


def save_marked_image(path_to_save, img):
    """This function save the marked up image"""
    cv2.imwrite(path_to_save, img)
