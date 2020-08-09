'''
sudo apt-get install libleptonica-dev 
sudo apt-get install libtesseract-dev
sudo apt-get install tesseract-ocr

or 

pip install tesseract
pip install tesseract-ocr

'''
# pytesseract library comprehension practice - week 2

from PIL import Image
from pytesseract import image_to_string

def binarize(image_to_transform, threshold):
    output_image=image_to_transform.convert("L")
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))< threshold:
                output_image.putpixel((x,y), 0)
            else:
                output_image.putpixel((x,y), 255)
    return output_image


# binarize, alternative method

image = Image.open("readonly/text.png")
image = binarize(image, 128)
#image.show()
text = image_to_string(image)
print(text + '\n')

# simple convert

#text = image_to_string(image)
#print(text + '\n')

# other method

image = Image.open("readonly/text2.png").convert('L')
#image.show()
text = image_to_string(image)
outfile = open("file.txt", "w")
outfile.write(text)
outfile.close()



