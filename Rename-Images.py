import os
  
os.chdir('/content/drive/MyDrive/PS2_Mosaic/indian_plates/')
print(os.getcwd())
COUNT = 1
  
# Function to increment count 
# to make the files sorted.
def increment():
    global COUNT
    COUNT = COUNT + 1
  

for f in glob.iglob('/content/drive/MyDrive/PS2_Mosaic/indian_plates/*.png'):
      f_name, f_ext = os.path.splitext(f)
      f_name = "plate" + str(COUNT)
      increment()

      new_name = '{}{}'.format(f_name, f_ext)
      print(new_name)
      os.rename(f, new_name)
