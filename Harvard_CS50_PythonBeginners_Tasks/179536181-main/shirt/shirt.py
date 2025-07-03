import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    else:
        beforePic = sys.argv[1]
        afterPic = sys.argv[2]
        beforeFormat = beforePic.split(".")
        afterFormat = afterPic.split(".")

    if beforeFormat[1].lower() != afterFormat[1].lower():
        sys.exit("Formats are not the same")
    else:
        addShirt(beforePic, afterPic)

def addShirt(beforePic, afterPic):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(beforePic) as image:
            shirtSize = shirt.size
            croppedImage = ImageOps.fit(image, shirtSize)
            croppedImage.paste(shirt, (0,0), mask = shirt)
            croppedImage.save(afterPic)
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()
