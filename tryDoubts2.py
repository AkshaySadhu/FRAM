import cv2,os
import numpy as np
from PIL import Image 
import pymysql

conn = pymysql.connect('localhost', 'root' ,'munna115', 'Attendance')
cur = conn.cursor()
image_paths = []

def paths_baba(path):
    for f in os.listdir(path):
        image_paths.append(os.path.join(path, f))


def get_images_and_labels():
     #image_paths = []
     #image_paths = [os.path.join(path, f) for f in os.listdir(path)]
     #for f in os.listdir(path):
      #    image_paths.append(os.path.join(path, f))
     # images will contains face images
    
     for image_path in image_paths:
         print(image_path)
         nbr = (os.path.split(image_path)[1]).split(".")[0]
         #nbr=int(''.join(str(ord(c)) for c in nbr))
         print (nbr)
         # Detect the face in the image
         

query = "SELECT folderName FROM TRAINIMAGES"
cur.execute(query)

row = cur.fetchone()
while row is not None:
    #print(row)
    paths_baba(row[0])
    row = cur.fetchone()
get_images_and_labels()

cv2.destroyAllWindows()
