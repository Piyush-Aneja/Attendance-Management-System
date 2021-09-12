import cv2
import face_recognition
import os,numpy
from gtts import gTTS
import playsound


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
    while True:
        
        # voice_command("Smile Please","selfieintro")
       
            
        success,myimg=cap.read()
        if success==True:
            
           
            cv2.imshow("WebCam",myimg)
           
        try:
            myimgEncode=face_recognition.face_encodings(myimg)[0]
            myfaceloc=face_recognition.face_locations(myimg)[0]
            x1,y1,x2,y2=myfaceloc[3],myfaceloc[0],myfaceloc[1],myfaceloc[2]
            cv2.rectangle(myimg,(x1,y2),(x2,y2+30),color=(255,0,0),thickness=-1) #for result 
        
            count=0
            result=False
            drawrectangle(myimg,myfaceloc)
            
           
            
            for trainencode in trainEncodings:
                
                result=face_recognition.compare_faces([trainencode],myimgEncode)
                
                if result[0]==True:
                    
                    print(f'Face matched with->{classname[count]}..!!!')
                    
                    cv2.putText(myimg,f"{classname[count].upper()}",(x1,y2+30),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,255,255),thickness=1)
                   
                    cv2.imshow("webcam image",myimg)
                   
                    # voice_command(f"{classname[count]}","result") #audio
                  
                    break
                count=count+1
            
            else:
                print("Face not matched with anyone")
               
                cv2.putText(myimg,"Not Matched",(x1,y2+30),cv2.FONT_HERSHEY_DUPLEX,1,color=(255,255,255),thickness=1)
               
                cv2.imshow("webcam image",myimg)
                
        except:
            
            # voice_command("Face not found in webcam","result")
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
    
    
# print(dir(face_recognition))
trainpath=r"D:/images"
readfile(trainpath) 
print(classname)
trainEncodings=findencoding(trainpath) 
print("Encoding done..!!!")
testPath="D:/testingImage"
# compare_face(trainEncodings,testPath)
takemypic(trainEncodings)



    
