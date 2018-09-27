import os
import numpy as np
import cv2
from PIL import Image

# Folder name
path = "dataset"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)

# Iterates through imagetest
for filename in filenames:
    directories = os.path.join(folder, filename)
    directory = os.listdir(directories)
    
    matrix = []
    # print(len(directory))

    # Iterates through the subdirectories in imagetest
    i=0
    for image in directory:
        if image == 'desktop.ini':
            continue
        
        alphabet = image[10]

        # img = cv2.imread(('%03d_sized_%s_1141128570.jpg') % (i, alphabet))
        img = cv2.imread(os.path.join(directories, image))
        img = np.array(img)
        # print(img.shape)
        matrix.append(img)
        
        # matrix.append(X)
        
        print('Saving dataset/%s/test_data%s.csv' % (alphabet, i))
        i += 1

    matrix = np.array(matrix)
    print(matrix.shape)
    np.savetxt(('dataset/%s/test_data.csv' % alphabet), matrix)
            
    # matrix = np.array(matrix)
    # print(filename, matrix.shape)
    # np.savetxt('dataset/test_data.csv', matrix)
