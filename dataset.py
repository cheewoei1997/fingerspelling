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

    # Iterates through the subdirectories in imagetest
    for image in directory:

        matrix = []
        alphabet = image[10]
        print(alphabet)

        # img = cv2.imread(('%03d_sized_%s_1141128570.jpg') % (i, alphabet))
        img = cv2.imread(os.path.join(directories, image))
        print(os.path.join(directories, image))
        img = np.array(img)
        X = img[:, 0]
        X = np.reshape(X, (-1, 1))
        X = X.T
        matrix.append(X)
            
    matrix = np.array(matrix)
    print(matrix)
    print(matrix.shape)
    np.savetxt(('test_data%s.txt') % alphabet, X)
    #     # Reads the images in the subdirectories
    #     img = cv2.imread(os.path.join(directories, image))
    #     # print(img)
    #     # cv2.imshow('img', img)
    #     # img = Image.open(os.path.join(directories, image))
    #     img = np.array(img)

    #     X = img[:, 0]
    #     X = np.reshape(X, (-1, 1))
    #     X = X.T

    #     dataset.append(X)

    #     # print(type(img))
    #     # print(img.shape)              # 64 64 3
    #     # print(image)
    #     # print(img)
    #     # data = np.asarray(img, dtype="uint8")
    #     # dataset.append(data)
    #     # train_images = np.asarray(dataset, dtype="uint8")

    # # dataset = np.array(dataset)
    # print(type(dataset))
    # np.savetxt(("train_images%s.txt" % image[10]), dataset)

# dataset = np.array(dataset)
# dataset = map(lambda t: list(t), dataset)
# print(dataset)




#Open images and save as txt


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
