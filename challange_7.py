from PIL import Image

im = Image.open("./inputs/oxygen.png")
width, height = im.size
half_height = height / 2

set_of_pixels = []

for i in range(0, width, 7):
    set_of_pixels.append(im.getpixel((i, half_height)))

l = []
for pixel in set_of_pixels:
    # print(pixel)
    if pixel[0] == pixel[1] == pixel[2]:
        l.append(pixel[0])
print(l)
print("".join(map(chr, l)))

# [105, 110, 116, 101, 103, 114, 105, 116, 121]
ll = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join(map(chr, ll)))  # integrity
