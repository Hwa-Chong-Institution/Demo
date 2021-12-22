from PIL import Image
from scipy import stats
import numpy as np

img = Image.open("handwritten_2.jpeg")
img = img.convert("L")
# img.show()
img_numpy = np.array(img)

# Getting grayscale value of every pixel in image
x, y = (img_numpy > 0).nonzero()
data = img_numpy[x, y]

# Checking for the most common (grayscale) colour to be set as background
colour, count = stats.mode(data)    

# Correcting text colour to be black
corrected = np.where(data < colour - 30, 0, data)

print(x[(corrected == 0)], y[(corrected == 0)])
gamer = []

for i in range(len(x[(corrected == 0)])):
    if x[(corrected == 0)][i] + 1 not in x[(corrected == 0)]:
        print(x[(corrected == 0)][i])
        gamer.append(x[(corrected == 0)][i])

# for i in range(len(data)):
#     print(img_numpy[x[(data < colour - 30)], y[(data < colour - 30)]])


testing = Image.open("handwritten_2.jpeg").convert("L")
pixels = testing.load()

count = 0
for i in range(img.size[0]):
    for j in gamer:
        print(f"iterating {count}")
        pixels[i, j] = 0
        count += 1
    count += 1

# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         if colour - 30 > pixels[i, j]:
#             print(pixels[i, j])
#             pixels[i, j] = 0
#         elif pixels[i, j] > 130:
#             print(pixels[i, j])
#             pixels[i, j] = 255


# testing.save("./cool.png")
testing.show()

# for i in data:
#     if not colour - 30 < i:
#         testing 
#         print(i)