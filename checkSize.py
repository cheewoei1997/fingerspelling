import cv2
import numpy as np
import os

# Folder name
path = "cropped_images"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

a = []
# Iterates through imagetest
for filename in filenames:
    directories = os.path.join(folder, filename)
    directory = os.listdir(directories)

    # Iterates through the subdirectories in imagetest
    for image in directory:
        # Reads the images in the subdirectories
        array_img = cv2.imread(os.path.join(directories, image))

        height, width, channels = array_img.shape
        a.append(height)

print(min(a))