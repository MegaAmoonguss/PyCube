import math
from PIL import Image

def genimage(s, cubesize):
    cube_image = Image.new("RGB", (300, 225))
    squaresize = math.floor(75 / cubesize)
    print(squaresize)
    
    rows = [line.strip() for line in s.split("newline")]
    img = [row.split() for row in rows]
    for r in range(len(img) - 1):
        for c in range(len(img[0])):
            if img[r][c] != "empty":
                color = Image.open("../images/" + img[r][c])
                color.thumbnail((squaresize, squaresize), Image.ANTIALIAS)
                cube_image.paste(color, (squaresize * c, squaresize * r))
    return cube_image