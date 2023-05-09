import cv2
import tensorflow as tf

model = tf.keras.models.load_model("Emotion.h5")
CATEGORIES = ['Angry','Happy','Neutral','Sad','Surprise']

def prepare(filepath):
    IMG_SIZE = 48  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
def GetResult():
    prediction = model.predict([prepare('face.jpg')])
    label=CATEGORIES[prediction.argmax()]
    print(label)
    return label # will be a list in a list.
#print(CATEGORIES[int(prediction[0][0])])
