import pickle
import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Set the path and filename for the saved model
model_path = 'saved_models/'
model_filename = 'my_model.pkl'

# Load the saved model
with open(model_path + model_filename, 'rb') as file:
    model = pickle.load(file)

# Define the command-line arguments for the input image path
parser = argparse.ArgumentParser()
parser.add_argument('image_path', help='Path to the input image file')
args = parser.parse_args()

# Load the input image
img = load_img(args.image_path, target_size=(100, 100))
img_array = img_to_array(img) / 255.
img_array = np.expand_dims(img_array, axis=0)

# Make the prediction using the loaded model
prediction = model.predict(img_array)
print(prediction)
# Get the fruit label from the prediction
label_map = {
    0: 'apple',
    1: 'banana',
    2: 'kiwi',
    3: 'not a fruit',
    4: 'orange',
    5: 'tomato'
}

predicted_label = label_map[np.argmax(prediction)]

# Output the predicted fruit label
print('The predicted fruit is: {}'.format(predicted_label))
