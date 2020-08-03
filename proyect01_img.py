# Week One Assignment - Jupyter Notebook

# José Alejandro Castro (castroj@ula.ve)

import PIL
from PIL import Image
from PIL import ImageEnhance, ImageFont, ImageDraw

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.png").convert('RGB')

# build a list of 9 images which have different color
image_new = []
text_tag = []

for i in range(3):       
    for j in 0.1, 0.5, 0.9:
        rgb_intensity = list(image.split())
        rgb_intensity[i] = rgb_intensity[i].point(lambda x: x * j)
        image_new.append(Image.merge(image.mode, rgb_intensity))
        text_tag.append('channel {} intensity {}'.format(i, j))
        

# build a list of 9 colors RBG in different pixeles

pixel_color = []

for i in image_new:
        pix = i.load()
        pixel_color.append(pix[0,0])

#print(pixel_color) 

# load font  
font_text = ImageFont.truetype("readonly/fanwood-webfont.ttf",75)

# create a contact sheet from different colors
first_image = image_new[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3 + 245))

x = 0
y = 0
i = 0

draw = ImageDraw.Draw(contact_sheet)

for img in image_new:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    draw.text((x, y + first_image.height), text_tag[i], font=font_text, fill=pixel_color[i])
    i += 1
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height + 80
    else:
        x = x + first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
#display(contact_sheet)

# view final image
contact_sheet.show()