"""
USAGE:
python shirt.py muppets/before1.jpg after1.jpg

DESCRIPTION:
Implement a program that expects exactly two command-line arguments:
- in sys.argv[1], the name (or path) of a JPEG or PNG
to read (i.e., open) as input
- in sys.argv[2], the name (or path) of a JPEG or PNG
to write (i.e., save) as output
- The program should then overlay shirt.png (which has a transparent background)
on the input after resizing and cropping the input to be the same size,
saving the result as its output.

EXAMPLE:
$ python shirt.py muppets/before1.jpg after1.jpg
<produces a new image called after1.jpg>
"""

import sys
from PIL import Image, ImageOps


def main():
    # Check number of input are 2
    if len(sys.argv) < 3:
        sys.exit("To few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many comman-line arguments")
    # Check image inputs are .jpg or .png
    nlen1 = len(sys.argv[1])
    nlen2 = len(sys.argv[2])
    # not minimum number of characters required for a proper name
    if nlen1 < 5 or nlen2 < 5:
        sys.exit("Not a JPG or PNG file")
    # Not valid extension
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if sys.argv[1][nlen1-4:] not in valid_extensions:
        sys.exit("Invalid input")
    if sys.argv[2][nlen2-4:] not in valid_extensions:
        sys.exit("Invalid output")
    # Inputs have different extensions
    if sys.argv[1][nlen1-4:] != sys.argv[2][nlen2-4:]:
        sys.exit("Input and output have diffeent extensions")

    # Overlay the shirt over the image
    overlay_img(sys.argv[1], sys.argv[2])


def overlay_img(oldfile, newfile):
    """(str,str)->None
    """
    # open images
    try:
        pic = Image.open(oldfile)
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # images info
    shirt_size = shirt.size
    pic_size = pic.size
    print(f"pic size={pic_size}, shirt size={shirt_size}")

    # resize pic image to shirt size
    pic_resized = ImageOps.fit(pic, shirt_size)
    print(f"pic resized={pic_resized.size}")

    # overlay
    pic_resized.paste(shirt, shirt)

    # save new image
    pic_resized.save(newfile)

if __name__ == "__main__":
    main()