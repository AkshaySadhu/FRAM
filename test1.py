import os
import cv2
import numpy as np

subjects = ["", "Akshay sadhu", "Nithish","Dinesh"]

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.13, minNeighbors=5);
    #print(len(faces))
    if (len(faces) == 0):
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=5);
        if (len(faces) == 0):
            return None
    
    return  faces


def prepare_training_data(data_folder_path):
    dirs = os.listdir(data_folder_path)
    faces = []
    labels = []

    for dir_name in dirs:
        if not dir_name.startswith('s'):
            continue
        label = int(dir_name.replace('s',''))
        subject_dir_path = os.path.join(data_folder_path, dir_name)
        subject_image_names = os.listdir(subject_dir_path)

        for image_name in subject_image_names:
            if image_name.startswith('.'):	#ignore system files like .DS_Store
                continue
            image_path = os.path.join(subject_dir_path,image_name)
            image = cv2.imread(image_path)
            resized_img = cv2.resize(image,(240,320))
            img = resized_img
            # cv2.imshow('Training on image...', image)
            #cv2.waitKey(10)
            facess = detect_face(image)
            if facess is None:
                print(subject_dir_path,"/",image_name)
                continue
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            (x,y,w,h) = facess[0]
            face = gray[y:y+w, x:x+h]
            if face is not None:
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, labels



def draw_rect(img,list1):
    for i in range(len(list1)):
        (x, y, w, h) = list1[i][1]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(img, list1[i][0], (x, y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
 



print("Preparing data...")
faces, labels = prepare_training_data("./training-data")
#print("\n")
#print(faces)
print("Data prepared")

#print total faces and labels
print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

#print(labels)
#create our LBPH face recognizer 
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
print("trained successfully...")

def predict(test_img):
   img = test_img.copy()
   faces = detect_face(img)
   #print(len(faces))
   #cv2.imshow("ori",img)
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   face_list=[]
   if faces is None:
       print("something went wrong\nunable to detect face \ntry with different image".upper())
       return None
   if (len(faces) is not None):
       for i in range(len(faces)):
           rect = faces[i]
           (x,y,w,h) = rect
           face = gray[y:y+w, x:x+h]
           #cv2.imshow("face",face)
           label, confidence = face_recognizer.predict(face)
           print("label = ",label)
           print("confidence = ",confidence )
           face_list.append([subjects[label],rect])
       #print(face_list)

   return face_list


print("Predicting images...")

#load test images
test_img1 = cv2.imread("test-data/t2.jpg")
rt_img = cv2.resize(test_img1,(240,320))
test_img1 = rt_img
test_img2 = cv2.imread("test-data/2.jpg")

#perform a prediction
predicted_list_img1 = predict(test_img1)

if predicted_list_img1 is not None:
    draw_rect(test_img1,predicted_list_img1 )
    cv2.imshow("test_img1", test_img1)
    print("Prediction complete")
    cv2.waitKey(0)
    cv2.destroyAllWindows()



