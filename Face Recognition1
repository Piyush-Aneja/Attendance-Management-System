import cv2
import face_recognition
import os,numpy
from gtts import gTTS
import playsound
import time
from datetime import datetime

classname=[]
def readfile(path):
    for file in os.listdir(path):
        name=file.split('.')[0]
        classname.append(name)
        
def drawrectangle(image,faceloc):
    y1,x2,y2,x1=faceloc[0],faceloc[1],faceloc[2],faceloc[3]
    cv2.rectangle(image,(x1,y1),(x2,y2),color=(0,255,0),thickness=1)
    

def findencoding(path):
    encodings=[]
    # facelocations=[]
    for file in os.listdir(path):
        name=file.split('.')[0]
        image=cv2.imread(f'{path}/{file}')
      
        encode=face_recognition.face_encodings(image)[0]
        faceloc=face_recognition.face_locations(image)[0]
       
        drawrectangle(image,faceloc)
        encodings.append(encode)
    return encodings

def findencodingTest(path,encodings):
    
    # facelocations=[]
    for file in os.listdir(path):
        name=file.split('.')[0]
        image=cv2.imread(f'{path}/{file}')
        image=cv2.resize(image,(0,0),None,0.75,0.75)
       
        encode=face_recognition.face_encodings(image)[0]
        faceloc=face_recognition.face_locations(image)[0]
    
        drawrectangle(image,faceloc)
        count=0
        for trainencode in encodings:
            
            result=face_recognition.compare_faces([trainencode],encode)
            if result[0]==True:
                
                print(f'Face matched with->{classname[count]}..!!!')
                cv2.putText(image,f"{classname[count].upper()}",(30,30),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,0,0),thickness=1)
                cv2.imshow("image",image)
                
                voice_command(f"Face matched with->{classname[count]}","result")
                cv2.waitKey(0)
            count=count+1
    
def takemypic(trainEncodings):
    voice_command("Smile Please","selfieintro")
    print("Get ready..!!!!")
    cap=cv2.VideoCapture(0)
    
    flag1=0
    while True:
       
        success,myimg=cap.read()
        if success==True:
            
            cv2.imshow("webcam image",myimg)
           
        # try:
            
        myfacelocAll=face_recognition.face_locations(myimg)
        myimgEncodeAll=face_recognition.face_encodings(myimg,myfacelocAll)
        
        count=0
        # result=False
        
        
        flag,flag1=0,0
        for myimgEncode,myfaceloc in zip(myimgEncodeAll,myfacelocAll):
            count=0
            drawrectangle(myimg,myfaceloc)
            
            x1,y1,x2,y2=myfaceloc[3],myfaceloc[0],myfaceloc[1],myfaceloc[2]
            cv2.rectangle(myimg,(x1,y2),(x2,y2+30),color=(255,0,0),thickness=-1) #for result 
            
            result=face_recognition.compare_faces(trainEncodings,myimgEncode)
            face_dist=face_recognition.face_distance(trainEncodings,myimgEncode)
        
            
            for res in result:
                if res==True:
                    flag,flag1=1,1
                    
                    print(f'Face matched with->{classname[count]}..!!!')
                    mark_attendance(classname[count])
                    acc=round(100-(min(face_dist)*100),2)
                    cv2.putText(myimg,f"{classname[count].upper()} {acc}%",(x1,y2+30),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,255,255),thickness=1)
                    # cv2.putText(myimg,f"{classname[count].upper()}",(x1,y2+30),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,255,255),thickness=1)
                    # cv2.imshow("webcam image",myimg)
                    
                    # voice_command(f"{classname[count]}","result") #audio
       
                count=count+1
                
            cv2.imshow("webcam image",myimg)
            
            if flag==0:
                flag1=1
                print("Face not matched with anyone")
        
                cv2.putText(myimg,"Not Matched",(x1,y2+30),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,255,255),thickness=1)
            
                cv2.imshow("webcam image",myimg)
                
        # except:
        if flag1==0:
            # voice_command("Face not found in webcam","result")
            print("Face not  found..!!!")
            cv2.rectangle(myimg,(50,50-30),(400,50),color=(255,0,0),thickness=-1)
            cv2.putText(myimg,"Face not  found..!!!",(50,50),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,255,255),thickness=1)
               
            cv2.imshow("webcam image",myimg)
            
            print("Face not found in webcam..!!!")
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            cv2.destroyAllWindows()
            break
        # cv2.waitKey(100)
   
def compare_face(encodings,testPath):
    
    findencodingTest(testPath,encodings)
    
    
def voice_command(txt,filename):
    voice_path="D:/voice_python"
    voice_path=os.path.join(voice_path,filename)
    voice_path=voice_path+".mp3"
    gTTS_obj=gTTS(txt,lang='en')
    gTTS_obj.save(voice_path)
    playsound.playsound(voice_path)
    os.remove(voice_path)

namelist=[]
def mark_attendance(name):
    with open("attendance.csv",'r+') as f:
        mydata=f.readlines()
        for line in mydata:
            str=line.split(',')[0] #name stored in csv file
            namelist.append(str)
        if name not in namelist:
            time=datetime.now()
            date=time.strftime("%d/%m/%Y")
            cur_time=time.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{date},{cur_time}")
    
# print(dir(face_recognition))
trainpath=r"D:/images"
readfile(trainpath) 
print(classname)
trainEncodings=findencoding(trainpath) 
print("Encoding done..!!!")
testPath="D:/testingImage"
# compare_face(trainEncodings,testPath)
takemypic(trainEncodings)



    
