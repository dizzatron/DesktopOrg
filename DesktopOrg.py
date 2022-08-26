import os
import shutil

print(os.getcwd())

os.chdir("/Users/murph/Desktop")
source = os.getcwd()
destinationPDF = "/Users/murph/Desktop/PDF"
destinationPNG = "/Users/murph/Desktop/PNG"
destinationWORD = "/Users/murph/Desktop/WORD"
print(os.getcwd())
for file in os.listdir():

    name, ext = os.path.splitext(file)

    if ext == '.pdf':
        shutil.move(file, destinationPDF)

    if ext == '.png':
        shutil.move(file, destinationPNG)

    if ext == '.doc' or ext == '.docx':
        shutil.move(file, destinationWORD)



