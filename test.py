import os
import random
import shutil

# Set the path to the "data" folder
data_path = "data"

# Set the desired ratio of train to test data
train_ratio = 0.8

# Create the "train" and "test" folders inside "data"
train_path = os.path.join(data_path, "train")
test_path = os.path.join(data_path, "test")
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Loop through each fruit folder in "data"
for fruit_folder in os.listdir(data_path):
    # Check if the folder is a fruit folder (i.e. not "train" or "test")
    if os.path.isdir(os.path.join(data_path, fruit_folder)):
        # Create the corresponding fruit folder in "train" and "test"
        train_fruit_path = os.path.join(train_path, fruit_folder)
        test_fruit_path = os.path.join(test_path, fruit_folder)
        os.makedirs(train_fruit_path, exist_ok=True)
        os.makedirs(test_fruit_path, exist_ok=True)

        # Loop through each image file in the fruit folder
        fruit_folder_path = os.path.join(data_path, fruit_folder)
        for img_file in os.listdir(fruit_folder_path):
            img_path = os.path.join(fruit_folder_path, img_file)

            # Decide whether to copy the image to "train" or "test"
            if random.uniform(0, 1) < train_ratio:
                dest_path = os.path.join(train_fruit_path, img_file)
            else:
                dest_path = os.path.join(test_fruit_path, img_file)

            # Copy the image file to the appropriate destination
            shutil.copyfile(img_path, dest_path)
