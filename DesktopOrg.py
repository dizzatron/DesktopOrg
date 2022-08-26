import os
import shutil

print(os.getcwd())

os.chdir("/Users/murph/Desktop")

destinationPDF = "/Users/murph/Desktop/PDF"
destinationPNG = "/Users/murph/Desktop/PNG"
destinationWORD = "/Users/murph/Desktop/WORD"
destinationJPG = "/Users/murph/Desktop/JPG"
destinationURL = "/Users/murph/Desktop/Program Shortcuts"
destinationSVG = "/Users/murph/Desktop/SVG"
print(os.getcwd())
for file in os.listdir():

    name, ext = os.path.splitext(file)
    print(name)
    print(ext)

    if ext == '.pdf':
        shutil.move(file, destinationPDF)

    if ext == '.png':
        shutil.move(file, destinationPNG)

    if ext == '.doc' or ext == '.docx':
        shutil.move(file, destinationWORD)

    if ext == '.jpg':
        shutil.move(file, destinationJPG)

    if ext == '.url':
        shutil.move(file, destinationURL)

    if ext == '.svg':
        shutil.move(file, destinationSVG)

