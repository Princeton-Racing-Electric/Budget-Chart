from PIL import Image
import sys

filename = '2021-2022 Budget.PNG'
img = Image.open(r"C:\Users\dsymo\Desktop\2021-2022 Budget.PNG")
img = img.convert('RGBA')
data = img.getdata()

converted = []

for pix in data:
    if pix[0] == 255 and pix[1] == 255 and pix[2] == 255:
        converted.append((0, 0, 0, 0))
    else:
        converted.append(pix)

output = Image.new('RGBA', img.size)
output.putdata(converted)

name, afterDot = filename.split('.')
output.save(f'C:/Users/dsymo/Desktop/{name}_Transparent.png', 'PNG')
