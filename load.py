import os
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from keras.utils import np_utils
from keras.models import load_model

import tensorflow as tf
from tensorflow import keras


model = load_model('hand_gestures.h5')

model.predict(y_train)