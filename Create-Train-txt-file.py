import os

image_files = []
os.chdir(os.path.join("images/", "obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        image_files.append("/content/drive/MyDrive/PS2_Mosaic/yoloseg/images/obj/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
