"""  Script to slice inputted satellite data into useable images
     Written by tpasfieldERAU, 
     Last Modified: 2/23/2023
     
     Completely broken lmao
"""

IMAGE_COUNT = 100
SIZE = 60
CB_VAR = False

# For diagnostic purposes
SCALE_OUT = True
OUT_SIZE = 400


import os
import random as r
import cv2 as cv
import numpy as np

if not os.path.exists('./sat_out/'):
    os.mkdir('./sat_out/')
    
    
def genSquare(mat, res, size):
    img = mat
    x = int(r.randint(0, res[0]-(size + 1)))
    y = int(r.randint(0, res[1]-(size + 1)))    
    buf = img[y:y+size, x:x+size]
    return buf


img = cv.imread('./sat_in/stmary.png')
img = cv.cvtColor(img, cv.COLOR_BGR2HSV).astype("float32")
wid = img.shape[1]
hei = img.shape[0]
res = [wid, hei]

n=0
while n < IMAGE_COUNT:
    buf = genSquare(img, res, SIZE)
    
    i = r.randint(0,3)
    if i == 0:
        pass
    elif i == 1:
        cv.rotate(buf, cv.ROTATE_90_CLOCKWISE)
    elif i == 2:
        cv.rotate(buf, cv.ROTATE_180)
    elif i == 3:
        cv.rotate(buf, cv.ROTATE_90_COUNTERCLOCKWISE)

    sat = r.randrange(1, 3)
    [h, s, v] = cv.split(buf)
    s = s * sat
    s = np.clip(s, 0, 255)
    buf = cv.merge([h,s,v])
    buf = cv.cvtColor(buf.astype("uint8"), cv.COLOR_HSV2BGR)
    
    if CB_VAR:
        temp = np.zeros(buf.shape, buf.dtype)
        alpha = 0.5 + 1.5 * r.random()
        beta = r.randint(-10, 10)
    
        for y in range(buf.shape[0]):
            for x in range(buf.shape[1]):
                for c in range(buf.shape[2]):
                    temp[y,x,c] = np.clip(alpha*buf[y,x,c] + beta, 0, 255)
        buf = temp
    
    if SCALE_OUT:
        buf = cv.resize(buf, [OUT_SIZE, OUT_SIZE], cv.INTER_AREA)
    cv.imwrite('./sat_out/' + str(n) + '.png' , buf)
    n+=1

print("complete.")