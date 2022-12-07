
#Imports 
from xml.dom import minidom
import os
import glob
import cv2

#Enter your mapping here
lut={}
lut["LP"]=0
'''If there are more than 1 objects 
lut["obj2"]=1
lut["obj3"]=2
.
.
'''


def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_xml2yolo( lut ):
    #Add paths of xml files and Image files respectively before "/*.xml" and "/*.png"
    for fname,image in zip(glob.iglob('/content/drive/MyDrive/PS2_Mosaic/yoloseg/ke/xml/*.xml'),glob.iglob("/content/drive/MyDrive/PS2_Mosaic/yoloseg/ke/images/*.png")):
#         image=cv2.imread(image)
#         print(fname)
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            width=image.shape[1]
            height=image.shape[0]

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                label_str = "0"

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s" % fname_out)


def main():
    convert_xml2yolo( lut )

#run main
if __name__ == '__main__':
    main()
