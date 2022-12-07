import os

image_files = []
##
os.chdir(os.path.join("images", "test"))

for filename in os.listdir(os.getcwd()):
    #change the format to match your image format
    if filename.endswith(".png"):
        #change the path
        image_files.append("/content/drive/MyDrive/PS2_Mosaic/yoloseg/images/test/" + filename)
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
