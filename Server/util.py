import json
import joblib
import numpy as np
import base64
import cv2
from wavelet import w2d

__class_name_to_number = {}
__class_number_to_name = {}

__model = None

def classify_image(image_base64_data, file_path = None):
    imgs = get_faces(file_path, image_base64_data)

    result = []

    for img in imgs:
        scaled_raw_img = cv2.resize(img, (32, 32))
        img_har =w2d(img, 'db1', 5)
        scaled_img_har = cv2.resize(img_har, (32, 32))
        combined_img = np.vstack((scaled_raw_img.reshape(32*32*3, 1), scaled_img_har.reshape(32*32, 1)))

        len_image_array = 32*32*3 + 32*32
        final = combined_img.reshape(1, len_image_array).astype(float)

        result.append({
            'class': class_number_to_name(__model.predict(final)[0]),
            'class_probability': np.round(__model.predict_proba(final) * 100, 2).tolist()[0],
            'class_dictionary': __class_name_to_number
        })


    return result


def load_server_artifacts():
    print("loading server artifacts...start")

    global __class_number_to_name
    global __class_name_to_number

    with open("./artifacts/class_dictionary.json", "r") as f:
        __class_name_to_number = json.load(f)
        __class_number_to_name = {v:k for k, v in __class_name_to_number.items()}

    global __model
    if __model is None:
        with open("./artifacts/model1.pkl", "rb") as f:
            __model = joblib.load(f)
    print("Loading server artifacts...done")

def class_number_to_name(class_num):
    return __class_number_to_name[class_num]


def getb64_string(b64str):
    '''
        Reference: https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library
    '''

    encoded_data = b64str.split(',')[-1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def get_faces(image_path, image_base64_data):
    face_cascade = cv2.CascadeClassifier("./opencv/haarcascades/haarcascade_frontalface_default.xml")
    if image_path:
        img = cv2.imread(image_path)
    else:
        img = getb64_string(image_base64_data)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(gray, 1.3, 5)

    cropped_faces = []

    for (x, y, w, h) in faces:
        roi_color = img[y:y+h, x:x+w]
        cropped_faces.append(roi_color)

    return cropped_faces

if __name__ == "__main__":
    load_server_artifacts()