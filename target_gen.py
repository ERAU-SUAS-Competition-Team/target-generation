""" 
TODO Add functional formatting and set up parameters in order to control outputs better
TODO Add metadata output for training
"""

imgwidth = 32
cap = 10

import os
import random as r

if not os.path.exists('./png/'):
    os.mkdir('./png/')

# COLORS
# white, black, gray, red, blue, green, yellow, purple, brown, orange
color_list = ['#FFF8DC', '#000000', '#A9A9A9', '#DC143C', '#0000CD', '#32CD32', '#FFD700', '#9400D3', '#A0522D', '#FF8C00'];

# Strings can be indexed, so it's all put into a string for now
alphanumerics = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Number of images to generate!

iteration = 0

targets =  ['circle.svg',
            'hexagon1.svg',
            'hexagon2.svg',
            'octagon1.svg',
            'octagon2.svg',
            'pentagon.svg',
            'plus.svg',
            'quartercircle.svg',
            'rect_h.svg',
            'rect_v.svg',
            'semicircle.svg',
            'septagon.svg',
            'square.svg',
            'star.svg',
            'trapezoid.svg']


if os.path.exists("./labels.csv"):
    os.remove("./labels.csv")

CSV = open("./labels.csv", "w")

while iteration < cap:
    select = r.randint(0,11)
    match select:
        case 0:
            index = 0
        case 1:
            index = 1 + r.randint(0,1)
        case 2:
            index = 3 + r.randint(0,1)
        case 3:
            index = 5
        case 4:
            index = 6
        case 5:
            index = 7
        case 6:
            index = 8 + r.randint(0,1)
        case 7:
            index = 10
        case 8:
            index = 11
        case 9:
            index = 12
        case 10:
            index = 13
        case 11:
            index = 14

    file = targets[index]

    if os.path.exists("./buffer.svg"):
        os.remove("./buffer.svg")
    shape_color = color_list[r.randint(0,9)]
    while True:
        text_color = color_list[r.randint(0,9)]
        if text_color != shape_color:break
    
    svg_code = open(f"./svg/{file}", "r")
    img = svg_code.read()
    img = img.replace("A", alphanumerics[ r.randint(0,35) ])
    img = img.replace('#000000', shape_color, -1)
    img = img.replace('#FFFFFF', text_color, -1)
    
    out = open(f"./buffer.svg", "w")
    out.write(img)
    out.close()
        
    os.system(f'dbus-run-session inkscape --export-type="png" --export-width={imgwidth:d} --export-height={imgwidth:d} --export-filename="./png/{iteration:5d}.png" buffer.svg > /dev/null 2>&1')
    
    CSV.write(f"{iteration:d}.png, {select:d}\n")
    iteration += 1

CSV.close()