import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

#Open images and save as txt
for i in range(1,8):
    img = Image.open(('{}.jpg').format(i))
    img = np.array(img)
    X = img[:, 0]
    X = np.reshape(X, (-1, 1))
    X = X.T
    np.savetxt(('test_data{}.txt').format(i), X)


#Convert to matrix in one txt
matrix = []

for i in range(1, 8):
    data = np.loadtxt(('test_data{}.txt').format(i))
    matrix.append(data)
    #print(data)
    #print(matrix)

matrix = np.array(matrix)
np.savetxt('testdata.txt'.format(i), matrix)
print(matrix)
print(matrix.shape)
