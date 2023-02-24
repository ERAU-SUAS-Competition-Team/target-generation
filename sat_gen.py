"""  Script to slice inputted satellite data into useable images
     Written by tpasfieldERAU, 
     Last Modified: 2/23/2023
     
     Completely broken lmao
"""

import os
import random as r
import cv2 as cv
import numpy as np

if not os.path.exists('./sat_out/'):
    os.mkdir('./sat_out/')
    

# Generates a single tile from the image, in the default orientation    
def genTile(mat, res, size):
    img = mat
    x = int(r.randint(0, res[0]-(size + 1)))
    y = int(r.randint(0, res[1]-(size + 1)))    
    buf = img[y:y+size, x:x+size]
    return buf


# Randomly rotates an image by some multiple of 90 degrees
def randomRotate(mat):
    i = r.randint(0,3)
    if i == 0:
        pass
    elif i == 1:
        cv.rotate(mat, cv.ROTATE_90_CLOCKWISE)
    elif i == 2:
        cv.rotate(mat, cv.ROTATE_180)
    elif i == 3:
        cv.rotate(mat, cv.ROTATE_90_COUNTERCLOCKWISE)
    else:
        pass
    return mat


# Randomly saturates an image
def randomSaturation(mat):
    mat = cv.cvtColor(mat, cv.COLOR_BGR2HSV).astype("float32")
    sat = r.randrange(1, 3)
    [h, s, v] = cv.split(mat)
    s = s * sat
    s = np.clip(s, 0, 255)
    mat = cv.merge([h,s,v])
    mat = cv.cvtColor(mat.astype("uint8"), cv.COLOR_HSV2BGR)
    return mat


# Randomly changes the contrast of an image
def randomContrast(mat):
    temp = np.zeros(mat.shape, mat.dtype)
    alpha = 0.5 + 1.5 * r.random()
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            for c in range(mat.shape[2]):
                temp[y,x,c] = np.clip(alpha * mat[y,x,c], 0, 255)
    return temp


# Randomly changes the brightness of an image
def randomBrightness(mat):
    temp = np.zeros(mat.shape, mat.dtype)
    beta = r.randint(-15,15)
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            for c in range(mat.shape[2]):
                temp[y,x,c] = np.clip(mat[y,x,c] + beta, 0, 255)
    return temp


# Randomly changes both the brightness and the contrast of an image
def randomCB(mat):
    temp = np.zeros(mat.shape, mat.dtype)
    alpha = 0.5 + 1.5 * r.random()
    beta = r.randint(-15, 15)

    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            for c in range(mat.shape[2]):
                temp[y,x,c] = np.clip(alpha*mat[y,x,c] + beta, 0, 255)
    return temp


# Changes the scale of the image with some given input, for diagnostics
def scale(mat, size):
    mat = cv.resize(mat, [size,size], cv.INTER_AREA)
    return mat
    