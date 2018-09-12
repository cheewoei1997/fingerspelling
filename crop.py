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
#resize to this size
x = 510
y = 1056
#Folder Name aka Alphabet/Number
alphabet = "1"
#Your ID
stud_id = "1141128429"
#####   Edit here   ####
currpath =  os.getcwd()
filenames = os.listdir(currpath + '\\' + alphabet)
i = 1
for filename in filenames:
    #Read image
    targetpath = currpath + '\\' + alphabet
    im = cv2.imread(targetpath + '\\' + filename)
    #Resize image 
    im2 = cv2.resize(im,(x, y))
    
    # #Select ROI
    r = cv2.selectROI(im2)
    #Crop image
    imCrop = im2[int(r[1]):int(r[1]+int((r[3]+r[2])/2)), int(r[0]):int(r[0]+int((r[3]+r[2])/2))]
    #Convert to grayscale
    imGrayScale = cv2.cvtColor(imCrop, cv2.COLOR_BGR2GRAY)
    # Save image
    cv2.imwrite(os.path.join(targetpath , filename[:3] + "_crop_%s_%s.jpg" % (alphabet, stud_id)), imGrayScale)
    #cv2.imwrite(os.path.join(targetpath , '%03d' % i + "_crop_%s_%s.jpg" % (alphabet, stud_id)), imCrop)
    i+=1