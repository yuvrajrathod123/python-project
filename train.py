
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import numpy as np
import pymysql

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        # backgroound image
        img1=Image.open(r"C:\hello\python-project\images\gradient_img5 (1).png")
        img1=img1.resize((1530,710),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg1=ImageTk.PhotoImage(img1)

        bgimg_lbl=Label(self.root,image=self.photoimg1)
        bgimg_lbl.place(x=0,y=0,width=1530,height=710)

        # back button

        back_btn = Button(bgimg_lbl,text="back",cursor="hand2",font=("arial",10,"bold"),bg="white",fg="red")
        back_btn.place(x=10,y=10,width=150,height=40)


        train_frame = LabelFrame(bgimg_lbl,bg="white",bd=2)
        train_frame.place(x=300,y=50,width=700,height=500)


        # photo_frame = LabelFrame(train_frame,bg="white",bd=2,border="red")
        # photo_frame.place(x=300,y=50,width=200,height=130)

        # image3 of the header of homepage

        img2=Image.open(r"C:\hello\python-project\images\face-recognition.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(train_frame,image=self.photoimg2)
        f_lbl.place(x=290,y=12,width=100,height=100)

        title_lbl = Label(train_frame,text="Training Data For Facial Recognition",font=("arial",20,"bold"),bg="white",fg="black")
        title_lbl.place(x=100,y=200)

        title_lbl = Label(train_frame,text="Optimize your facial recognition models for accuracy with the best quality image data",font=("arial",13,"bold"),bg="white",fg="black")
        title_lbl.place(x=20,y=250)


        train_btn = Button(train_frame,command=self.train_classifier,text="Train Data",cursor="hand2",font=("arial",10,"bold"),bg="royalblue",fg="white")
        train_btn.place(x=270,y=350,width=150,height=40)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Traing",imageNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # ============= train the classifier ==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!!",parent=self.root)            

if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()        