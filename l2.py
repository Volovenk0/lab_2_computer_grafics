from PIL import Image, ImageDraw
image = Image.new('L', (960, 540), 255)
imageDraw = ImageDraw.Draw(image)
with open("D:\lab_2_computer_grafics\DS4.txt", "r") as file:
    for line in file:
        coordinates = line.split()
        i = int(coordinates[1])
        j = int(coordinates[0])
        imageDraw.line((i, 540 - j, i + 1, 540 - (j + 1)))
image.show()
image.save('result.png')
