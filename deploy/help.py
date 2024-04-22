from tensorflow.keras.models import Sequential, model_from_json
import tensorflow_hub as hub
from tensorflow.keras.optimizers import RMSprop
import cv2
import matplotlib.pylab as plt
import numpy as np
import joblib


def load_model():
    json_file = open('deploy\custome_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json, custom_objects={'KerasLayer': hub.KerasLayer})
    # load weights into new model
    loaded_model.load_weights("deploy\custome_model.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss='categorical_crossentropy',
            optimizer=RMSprop(learning_rate=1e-4),
            metrics=['accuracy'])
    return loaded_model

def predict_image(image_path):
    le=joblib.load('deploy\lables')
    model=load_model()
    image=cv2.imread(str(image_path))
    imageee=cv2.resize(image,(224,224))
    imageee=imageee/255.0
    res= model.predict(np.array([imageee]))
    return le.classes_[np.argmax(res)]





