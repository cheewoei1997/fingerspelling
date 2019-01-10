import os
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from keras.utils import np_utils

import tensorflow as tf
from tensorflow import keras


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
image_data = np.array(image_data)
# np.savetxt('dataset.txt', image_data)

# a = np.asarray(image_data)
# np.savetxt("dataset.csv", a, delimiter=",")

# img_data_scaled = image_data.reshape(image_data.shape[0], img_rows, img_cols, num_col)
# print(img_data_scaled)
num_samples = len(filenames)
label=np.ones((num_samples,),dtype = str)
label[0:500]=1
label[501:1000]=2
label[1001:1500]=3
label[1501:2000]=4
label[2001:2500]=5
label[2501:3000]=6
label[3001:3500]=7
label[3501:3400]=8
label[4001:4500]=9
label[4501:5000]=10
label[5001:5500]=11
label[5501:6000]=12
label[6001:6500]=13
label[6501:7000]=14
label[7001:7500]=15
label[7501:8000]=16
label[8001:8500]=17
label[8501:9000]=18
label[9001:9500]=19
label[9501:10000]=20
label[10001:10500]=21
label[10501:11000]=22
label[11001:11500]=23
label[11501:12000]=24
label[12001:12500]=25
label[12501:13000]=26
label[13001:13500]=27
label[13501:14000]=28
label[14001:14500]=29
label[14501:15000]=30
label[15001:15500]=31
label[15501:16000]=32
label[16001:16500]=33

class_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y']


# image_data = array()
data, Label = shuffle(image_data, label, random_state=2)
train_data = [data, Label]
(X, y) = (train_data[0],train_data[1])
# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
img_data_scaled = image_data.reshape(image_data.shape[0], image_data.shape[1], image_data.shape[2], 1)
print(img_data_scaled.shape)
print('Labels: ', Label.shape)
print('X_train: ', X_train.shape)
print('X_test: ', X_test.shape)
print('y_train: ', y_train.shape)
print('y_test: ', y_test.shape)

X_train = X_train / 255.0
X_test = X_test / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(64, 64)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(33, activation=tf.nn.softmax)
])


model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=5, batch_size=16)

# Save the model
# model_save_path = os.path.join('hand_gestures.h5')
# model.save(model_save_path)
# print("Saved to ", model_save_path)



predictions = model.predict(X_test)
print(predictions)

# num_rows = 5
# num_cols = 3
# num_images = num_rows*num_cols
# plt.figure(figsize=(2*2*num_cols, 2*num_rows))
# for i in range(num_images):
#   plt.subplot(num_rows, 2*num_cols, 2*i+1)
#   plot_image(i, predictions, y_test, y_train)
#   plt.subplot(num_rows, 2*num_cols, 2*i+2)
#   plot_value_array(i, predictions, y_test)



# Evaluate accuracy
test_loss, test_acc = model.evaluate(X_train, X_test)

print('Test accuracy:', test_acc)


# plt.figure(figsize=(10,10))
# for i in range(25):
#   plt.subplot(5, 5, i+1)
#   plt.xticks([])
#   plt.yticks([])
#   plt.grid(False)
#   plt.imshow(train_images[i], cmap=plt.cm.binary)
#   plt.xlabel(class_names[train_labels[i]])

  