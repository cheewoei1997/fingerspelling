import cv2
import numpy as np
import os

# Folder name
path = "greyscale"
# Desired resolution
width = 64
height = 64
# Save location
save = "greyscalesave"
save_folder = os.path.join(os.getcwd(), save)

# student_id = "1141128570"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

# Iterates through imagetest
for filename in filenames:
    directories = os.path.join(folder, filename)
    # directory = os.listdir(directories)

    # Iterates through the subdirectories in imagetest
    if filename == 'desktop.ini':
        continue
    letter = filename[9]
    print("Currently at: ", filename)

    # Reads the images in the subdirectories
    array_img = cv2.imread(os.path.join(folder, filename))
    # print(os.path.join(folder, filename))

    resized_image = cv2.resize(array_img, (width, height))
    cv2.imwrite(os.path.join(save_folder, filename[:3] + '_sized_%s_%s.jpg' % (letter, filename[12:21])), resized_image)
