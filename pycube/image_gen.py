from PIL import Image

def genimage(s):
    cube_image = Image.new("RGB", (300, 225))
    
    rows = [line.strip() for line in s.split("newline")]
    img = [row.split() for row in rows]
    for r in range(len(img) - 1):
        for c in range(len(img[0])):
            if img[r][c] != "empty":
                cube_image.paste(Image.open("C:/Users/graha/workspace-py/pycube/scrambler/scrbg/" + img[r][c]), (25 * c, 25 * r))
    return cube_image