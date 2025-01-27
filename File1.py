import cv2; #opencv
import os;
import time;
import uuid;

IMAGES_PATH='RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages'
labels=['hello','thanks','yes','no','iloveyou']
number_imgs=15

for label in labels:

    label_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(label_path, exist_ok=True)
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error:Could not access the camera.")
    print('Collecting Images for {}'.format(label))
    time.sleep(5)


    for imagename in range(number_imgs):
        ret,frame=cap.read()

        
        imagename=os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    cap.release()

#"C:\Users\sehga\RealTimeObjectDetection\Tensorflow\workspace\images\collectedimages"