from cairosvg import svg2png
import os
import random as r

# COLORS
# white, black, gray, red, blue, green, yellow, purple, brown, orange
color_list = ['#FFF8DC', '#000000', '#A9A9A9', '#DC143C', '#0000CD', '#32CD32', '#FFD700', '#9400D3', '#A0522D', '#FF8C00'];

# Strings can be indexed, so it's all put into a string for now
alphanumerics = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for file in os.listdir("svg"):
    shape_color = color_list[r.randint(0,9)]
    while True:
        text_color = color_list[r.randint(0,9)]
        if text_color != shape_color:
            break

    svg_code = open(f"./svg/{file}", "r")
    img = svg_code.read()
    img = img.replace("A", alphanumerics[ r.randint(0,35) ])
    img = img.replace('#000000', shape_color, -1)
    img = img.replace('#FFFFFF', text_color, -1)
    svg2png(bytestring=img, write_to=f'./png/{file.replace(".svg","")}.png')