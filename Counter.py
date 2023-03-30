import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *
import torch


# model=YOLO('yolov8s.pt')

path=r"C:\Users\shafaattahir\Desktop\Research work\Object detection model\yolov8_tracking-master\best.pt"
# model=YOLO(path)

model=torch.hub.load(path, 'yolov8s', pretrained=True)

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('finalvehicle.mp4')


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
#print(class_list)
count=0
tracker=Tracker()   
area=[(416,192),(424,194),(444,180),(432,174)]
area_c=set()
area1=[(501,224),(517,227),(542,216),(527,212)]
area_c1=set()





while True:    
    ret,frame = cap.read()
    if not ret:
        break
#    count += 1
#    if count % 3 != 0:
#        continue


    frame=cv2.resize(frame,(1020,500))

    results=model.predict(frame)
    print(results)
#     a=results[0].cpu().boxes.boxes
#     px=pd.DataFrame(a).astype("float")

# #    print(px)
#     list=[]
#     for index,row in px.iterrows():
# #        print(row)
 
#         x1=int(row[0])
#         y1=int(row[1])
#         x2=int(row[2])
#         y2=int(row[3])
#         d=int(row[5])
#         c=class_list[d]
# #        if 'person' in c:
#         list.append([x1,y1,x2,y2])
            
#     bbox_idx=tracker.update(list)
#     for bbox in bbox_idx:
#         x3,y3,x4,y4,id=bbox
#         cx=int(x3+x4)//2
#         cy=int(y3+y4)//2
        
#         results=cv2.pointPolygonTest(np.array(area,np.int32),((x4,y4)),False)
#         if results>=0:
#            cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
#            cv2.putText(frame,str(int(id)),(x3,y3),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
#            area_c.add(id)
#         results1=cv2.pointPolygonTest(np.array(area1,np.int32),((x4,y4)),False)
#         if results1>=0:
#            cv2.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
#            cv2.putText(frame,str(int(id)),(x3,y3),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
#            area_c1.add(id)   
        
#     area1_c=(len(area_c))
#     area2_c=(len(area_c1))    
#     cv2.putText(frame,str(int(area1_c)),(80,60),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2)
#     cv2.putText(frame,str(int(area2_c)),(180,60),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2)

#     cv2.polylines(frame,[np.array(area,np.int32)],True,(255,0,0),2)
#     cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,0,0),2)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()

