import cv2
import numpy as np
import os

# Folder name
path = "greyscale_images"
# Desired resolution
width = 64
height = 64
# Save location
save = "64x64_images"
save_folder = os.path.join(os.getcwd(), save)

# student_id = "1141128570"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

# Iterates through imagetest
for filename in filenames:
    directories = os.path.join(folder, filename)
    directory = os.listdir(directories)

    # Iterates through the subdirectories in imagetest
    for image in directory:
        if image == 'desktop.ini':
            continue
        letter = image[9]
        save_foldernew = os.path.join(save_folder, letter)
        print("Currently at: ", image)

        # Reads the images in the subdirectories
        array_img = cv2.imread(os.path.join(directories, image))

        resized_image = cv2.resize(array_img, (width, height))
        cv2.imwrite(os.path.join(save_foldernew, image[:3] + '_sized_%s_%s.jpg' % (letter, image[12:22])), resized_image)
