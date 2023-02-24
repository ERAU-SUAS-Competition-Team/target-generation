""" Main Generation Script
    This will eventually be constructed, but is a palceholder for now.
"""

import cv2 as cv
import numpy as np
import os

import sat_gen as sg

SIZE = 60

img = cv.imread('./sat_in/stmary.png')

wid = img.shape[1]
hei = img.shape[0]
res = [wid, hei]

tile = sg.genTile(img, res, SIZE)

cv.imshow('tile', tile)
cv.waitKey()