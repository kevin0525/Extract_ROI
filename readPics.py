import csv
import numpy as np
import cv2

path = '/home/kevin/workspace/SSD/object-detection/images_deck/'

with open(r'/home/kevin/workspace/SSD/object-detection/images_deck/train_labels.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        #print(row[0])
        imgpath=path+'origin/'+row[0]
        partimg=path+'result_lengthLongerThan64/'+row[0]
        #print(imgpath)
        img = cv2.imread(imgpath)
        if(type(img) is np.ndarray):
            #cv2.imshow('image',img)
            
            width = int(row[6]) - int(row[4])
            height = int(row[7]) - int(row[5])
            if(width>height): 
                length=width
            else:
                length=height
            img_roi = img[int(row[5]):(int(row[5])+length),int(row[4]):(int(row[4])+length)]
            #sp = img_roi.shape   #图片的宽 高 深度 https://blog.csdn.net/qq_15505637/article/details/78539240
            #print (sp[0]) #width
            #print(sp[1])  #height
            #if(length>64):
                #cv2.imwrite(partimg,img_roi)
            
            #cv2.imshow('img_roi',img_roi)
            #cv2.waitKey()
            
cv2.destroyAllWindows()
        
