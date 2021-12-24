# Importing Image and ImageChops module from PIL package
from PIL import Image, ImageChops


# L, RGB
# creating a image1 object
im1 = Image.open(r"A.png").convert("1")

# creating a image2 object
im2 = Image.open(r"B.png").convert("1")


# applying logical_xor method, both must have mode '1'!!
im3 = ImageChops.logical_xor(im1, im2)

im3.show()

# im3.save("Lösung.png")
