
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import numpy as np
import pymysql

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        
        # to add img
        # image 1 of header
        img=Image.open(r"C:\hello\python-project\images\img1-unsplash.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=382,height=130)

        # image2 of the header
        img1=Image.open(r"C:\hello\python-project\images\img7.jpg")
        img1=img1.resize((300,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=300,y=0,width=300,height=130)

        # image3 of the header of homepage
        img2=Image.open(r"C:\hello\python-project\images\img4.png")
        img2=img2.resize((400,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=600,y=0,width=382,height=130)

        # image4 of the header of homepage
        img3=Image.open(r"C:\hello\python-project\images\img2.png")
        img3=img3.resize((600,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=980,y=0,width=300,height=130)

        # img4 = Image.open(r"C:\hello\python-project\images\img4.png")

        # backgroound image
        img4=Image.open(r"C:\hello\python-project\images\face-detection-bg.webp")
        img4=img4.resize((1530,710),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg4=ImageTk.PhotoImage(img4)

        bgimg_lbl=Label(self.root,image=self.photoimg4)
        bgimg_lbl.place(x=0,y=130,width=1300,height=670)


        # title label
        title_lbl = Label(bgimg_lbl,text="FACE RECOGNITION",font=("arial",25,"bold"),bg="white",fg="green")
        title_lbl.place(relx=0.5,rely=0.03,width=1530,height=45,anchor=CENTER)

        # back button
        back_btn = Button(bgimg_lbl,text="back",cursor="hand2",font=("arial",10,"bold"),bg="white",fg="darkred")
        back_btn.place(x=10,y=0,width=100,height=42)

         #  image
        img5=Image.open(r"C:\hello\python-project\images\face1.webp")
        img5=img5.resize((250,250),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg5=ImageTk.PhotoImage(img5)

        face_lbl=Label(bgimg_lbl,image=self.photoimg5)
        face_lbl.place(x=500,y=100,width=250,height=250)

         # face detector button
        back_btn = Button(bgimg_lbl,command=self.face_recog,text="Face Detector",cursor="hand2",font=("arial",15,"bold"),bg="white",fg="darkred")
        back_btn.place(x=500,y=350,width=250,height=42)

        
    # ========================= function ======================

    def face_recog(self):
        def draw_boundray(img,classifier,sacleFactor,minNeighbours,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,sacleFactor,minNeighbours) 

            coord = []
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300))) 

                conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)
                my_cursor=conn.cursor()

                my_cursor.execute("select Caregiver_Name from caregiver where CaregiverID="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Address from caregiver where CaregiverID="+str(id))
                a = my_cursor.fetchone()
                a="+".join(a)
 
                my_cursor.execute("select Mobile_No from caregiver where CaregiverID="+str(id))
                m = my_cursor.fetchone()
                m="+".join(m)
 

                if confidence>77:
                    cv2.putText(img,f"Caregiver_Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Address:{a}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Mobile_No:{m}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord 

        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()
               

        
        
      
        


if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition(root)
    root.mainloop()   