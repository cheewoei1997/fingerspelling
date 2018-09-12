import os
import cv2

# Folder name
path = "imagetest"

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
        # Reads the images in the subdirectories
        array_img = cv2.imread(os.path.join(directories, image))
        # Convert them to greyscale
        grey_img = cv2.cvtColor(array_img, cv2.COLOR_BGR2GRAY)
        # Save them after renaming them
        cv2.imwrite(os.path.join(directories, image[:3] + 'greyscale.jpg'), grey_img)