import os
import numpy as np
import cv2
from PIL import Image

# Folder name
path = "greyscalesave"

# Get address of current working directory
folder =  os.path.join(os.getcwd(), path)
# Gets all contents of the address of folder
filenames = os.listdir(folder)


matrix = []
i = 0
# Iterates through imagetest
for filename in filenames:
    directory = os.path.join(folder, filename)
    print(directory)
    
    
    # print(len(directory))

    # Iterates through the subdirectories in imagetest
    
    if filename == 'desktop.ini':
        continue
    
    alphabet = filename[9]
    print(directory)

    # img = cv2.imread(('%03d_sized_%s_1141128570.jpg') % (i, alphabet))
    img = cv2.imread(directory)
    img = np.array(img)
    matrix.append(img)
    # print(img.shape)
    # X = img[:, 0]
    # # print(X.shape)
    # X = np.reshape(X, (-1, 1))
    # # print(X.shape)
    # X = X.T
    # print(X.shape)
    # matrix.append(X)
    # np.savetxt(('dataset/%s/test_data%s.csv') % (alphabet, i), X)
    # print(' Saving dataset/%s/test_data%s.csv' % (alphabet, i))
    # i += 1
            
    # matrix = np.array(matrix)
    # print(filename, matrix.shape)
    # np.savetxt('dataset/test_data.csv', matrix)

image_data = np.array(matrix)
# image_data = image_data.astype('float32')
# image_data /= 255
image_data = image_data[:, :, :, 0]
image_data = image_data.astype('float32')
image_data /= 255
print(image_data.shape)