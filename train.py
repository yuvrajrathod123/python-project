
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2

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


        train_frame = LabelFrame(bg="white",bd=2)
        train_frame.place(x=300,y=50,width=700,height=500)


        # photo_frame = LabelFrame(train_frame,bg="white",bd=2,border="red")
        # photo_frame.place(x=300,y=50,width=200,height=130)

        # image3 of the header of homepage

        img2=Image.open(r"C:\hello\python-project\images\img7.jpg")
        img2=img2.resize((200,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

       
        f_lbl=Label(train_frame,image=self.photoimg2)
        f_lbl.place(x=250,y=12,width=200,height=130)


if __name__ == "__main__":
    root=Tk()
    obj = Train(root)
    root.mainloop()        