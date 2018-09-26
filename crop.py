#####   Notes   ####
#
#  Run this file in the master folder 
#  where you store all the 33 folders 
#  for the signs
#  Make sure all the original images 
#  are renamed properly before proceeding
#
#####   Notes   ####


import cv2
import numpy as np
import os


#####   Edit here   ####
#if you use use front camera, enable the vertical flip (True)
VerticalFlip = False

# #resize to this size
# ReduceSizeRatio = 7

#Start Number
startNum = 000

#Folder Name aka Alphabet/Number
orig_img = "original_images"
alphabet = "Q"
letter = "q"

#Your ID
stud_id = "1141128570"
#####   Edit here   ####


currpath =  os.path.join(os.getcwd(), orig_img)
filenames = os.listdir(currpath + '\\' + alphabet)
i = 1

#Resize image
height = 300
width = 400

for filename in filenames:
    #Read image
    targetpath = currpath + '\\' + alphabet
    im = cv2.imread(targetpath + '\\' + filename)
    im2 = cv2.resize(im,(width, height))
    
    if VerticalFlip:
        im2 = cv2.flip(im2, 1)
    
    # #Select ROI
    r = cv2.selectROI(im2)

    #Crop image
    imCrop = im2[int(r[1]):int(r[1]+int((r[3]+r[2])/2)), int(r[0]):int(r[0]+int((r[3]+r[2])/2))]

    #Convert to grayscale
    # imGrayScale = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)

    # Save image
    cv2.imwrite(os.path.join(targetpath , filename[:3] + "_crop_%s_%s.jpg" %(letter,stud_id) ), imCrop)
    startNum += 1