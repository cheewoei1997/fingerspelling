import os
import numpy as np
import cv2
from PIL import Image

# Folder name
path = "64x64_images"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)


# Iterates through imagetest
for filename in filenames:
    directories = os.path.join(folder, filename)
    directory = os.listdir(directories)
    matrix = []

    # Iterates through the subdirectories in imagetest
    for image in directory:

        
        alphabet = image[10]

        # img = cv2.imread(('%03d_sized_%s_1141128570.jpg') % (i, alphabet))
        img = cv2.imread(os.path.join(directories, image))
        img = np.array(img)
        # print(img.shape)
        X = img[:, 0]
        # print(X.shape)
        X = np.reshape(X, (-1, 1))
        # print(X.shape)
        X = X.T
        # print(X.shape)
        matrix.append(X)
            
    matrix = np.array(matrix)
    print(filename, matrix.shape)
    np.savetxt(('dataset/test_data%s.csv') % alphabet, X)
