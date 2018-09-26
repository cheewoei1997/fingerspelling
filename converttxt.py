import os
import numpy as np
import cv2
from PIL import Image

alphabet = "4"

#Open images and save as txt
matrix = []

for i in range(0,100):
    img = cv2.imread(('%03d_sized_' + alphabet +'_1141128570.jpg') % i)
    print(img)
    img = np.array(img)
    X = img[:, 0]
    X = np.reshape(X, (-1, 1))
    X = X.T
    matrix.append(X)
    
matrix = np.array(matrix)
print(matrix.shape)
np.savetxt(('test_data%s.txt') % alphabet, X)

#Convert to matrix in one txt


# for i in range(0, 100):
#     data = np.loadtxt(('test_data%03d.txt') % i)
#     matrix.append(data)
#     #print(data)
#     #print(matrix)

# matrix = np.array(matrix)
# np.savetxt('testdata1.txt', matrix)
# # print(matrix)
# # print(matrix.shape)
