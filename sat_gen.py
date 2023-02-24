"""  Script to slice inputted satellite data into useable images
     Written by tpasfieldERAU, 
     Last Modified: 2/23/2023
     
     Completely broken lmao
"""


import os
import random as r
import cv2 as cv
# This is just for diagnostics

if not os.path.exists('./sat_out/'):
    os.mkdir('./sat_out/')
    
    
def genSquare(mat, res, size):
    img = mat
    x = int(r.randint(0, res[0]-(size + 1)))
    y = int(r.randint(0, res[1]-(size + 1)))    
    buf = img[y:y+size, x:x+size]
    # print('Image ' + str(n) + ': ' + str(x) + ', ' + str(y))
    return buf


img = cv.imread('./sat_in/stmary.png')
wid = img.shape[1]
hei = img.shape[0]
res = [wid, hei]
# print(str(wid) + ' ' + str(hei))

n=0
while n < 25:
    buf = genSquare(img, res, 60)
    cv.imwrite('./sat_out/' + str(n) + '.png' , buf)
    n+=1

print("complete.")