# predict the fruit from the camera feed

# import the necessary packages
import pickle
import argparse
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import cv2

# Set the path and filename for the saved model
model_path = 'saved_models/'
model_filename = 'my_model.pkl'

# Load the saved model
with open(model_path + model_filename, 'rb') as file:
    model = pickle.load(file)

# Label map
label_map = {
    0: 'apple',
    1: 'banana',
    2: 'corn',
    3: 'kiwi',
    4: 'lemon',
    5: 'orange',
    6: 'strawberry'
}

# Initialize the camera
camera = cv2.VideoCapture(0)

# Main loop to predict the fruit
while True:
    # Capture the frame from the camera and resize it to 100x100 without distorting the image
    frame = camera.read()[1]
    frame = cv2.resize(frame, (100, 100), interpolation=cv2.INTER_AREA)

    # Convert the frame to an array
    frame_array = img_to_array(frame) / 255.
    frame_array = np.expand_dims(frame_array, axis=0)

    # Make the prediction using the loaded model
    prediction = model.predict(frame_array)

    # Get the fruit label from the prediction
    predicted_label = label_map[np.argmax(prediction)]

    # Output the predicted fruit label
    # print('The predicted fruit is: {}'.format(predicted_label))

    # Display the frame with the prediction text on it
    cv2.putText(frame, predicted_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow('frame', frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the camera and close all windows
cv2.destroyAllWindows()
