from cairosvg import svg2png
import os

for file in os.listdir("svg"):
    svg_code = open(f"./svg/{file}", "r")

    svg2png(bytestring=svg_code.read(),write_to=f'./png/{file.replace(".svg","")}.png')