# Ref: https://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html

from PIL import Image, ImageDraw
import sys

RED = "#ff0000"

def main():
    origImag = ''
    outdirectory = ''
    if len(sys.argv) < 2:
        print("Usage: python DrawStraightLines.py <input image> <output folder>")
        sys.exit(1)

    count = 0
    for args in sys.argv:
        count = count + 1
        if (count == 2):
            origImag = args
        if (count == 3):
            outdirectory = args

    try:
        im = Image.open(origImag)
        filenamecounter = 1

        x1 = 580
        y1 = 1080
        x3 = 2180

        for i in range(x1, x3, 100):
            draw = ImageDraw.Draw(im)
            x4 = x1 + filenamecounter*100
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1

        filenamecounter+=1
        draw = ImageDraw.Draw(im)
        draw.line([x1, y1, 2300, y1], width=10, fill=RED)
        outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
        im.save(outImage)

        im = Image.open(outImage)

        x1 = 580
        y1 = 1630
        x3 = 2180

        anothercounter = 1
        for i in range(x1, x3, 100):
            draw = ImageDraw.Draw(im)
            x4 = x1 + anothercounter*100
            draw.line([x1, y1, x4, y1], width=10, fill=RED)
            outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
            # im.show()
            im.save(outImage)
            filenamecounter += 1
            anothercounter += 1

        draw = ImageDraw.Draw(im)
        draw.line([x1, y1, 2300, y1], width=10, fill=RED)
        outImage = outdirectory + "Image" + '{:03d}'.format(filenamecounter) + ".png"
        im.save(outImage)


    except IOError as e:
        print("IO Error ")
        print(e)
        pass


if __name__ == "__main__":
    main() 
