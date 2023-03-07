from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from caregiver import Caregiver
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_recognition_sys:
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
        img1=Image.open(r"C:\hello\python-project\images\img3.jpg")
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

        img4 = Image.open(r"C:\hello\python-project\images\img4.png")

        # backgroound image
        img5=Image.open(r"C:\hello\python-project\images\gradient_img5 (1).png")
        img5=img5.resize((1530,710),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg5=ImageTk.PhotoImage(img5)

        bgimg_lbl=Label(self.root,image=self.photoimg5)
        bgimg_lbl.place(x=0,y=130,width=1530,height=710)

        # title label

        title_lbl = Label(bgimg_lbl,text="IDENTIFICATION OF CAREGIVERS USING FACE RECOGNITION",font=("arial",25,"bold"),bg="white",fg="black")
        title_lbl.place(relx=0.4,rely=0.03,width=1530,height=45,anchor=CENTER)
        

        # ================== buttons =========================

        # caregiver button
        img6=Image.open(r"C:\hello\python-project\images\caregiver_img1.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg6=ImageTk.PhotoImage(img6)

        btn1 = Button(bgimg_lbl,image=self.photoimg6,cursor="hand2",command=self.caregiver_details)
     
        btn1.place(x=70,y=80,width=150,height=150)

        btn1_1 = Button(bgimg_lbl,text="Caregiver Details",cursor="hand2",font=("arial",10,"bold"),bg="darkblue",fg="white",command= self.caregiver_details)
        btn1_1.place(x=70,y=220,width=150,height=40)


        # detectface button
        img7=Image.open(r"C:\hello\python-project\images\face_detector.jpeg")
        img7=img7.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg7=ImageTk.PhotoImage(img7)

        btn2 = Button(bgimg_lbl,command=self.detect_face,image=self.photoimg7,cursor="hand2")
        btn2.place(x=260,y=80,width=150,height=150)

        btn2_2 = Button(bgimg_lbl,command=self.detect_face,text="Face Detector",cursor="hand2",font=("arial",10,"bold"),bg="darkblue",fg="white")
        btn2_2.place(x=260,y=220,width=150,height=40)


        # regular status button
        img8=Image.open(r"C:\hello\python-project\images\regular_status.webp")
        img8=img8.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg8=ImageTk.PhotoImage(img8)

        btn3 = Button(bgimg_lbl,image=self.photoimg8,cursor="hand2",command=self.attendance)
        btn3.place(x=455,y=80,width=150,height=150)

        btn3_3 = Button(bgimg_lbl,text="Regular Status",cursor="hand2",command=self.attendance,font=("arial",10,"bold"),bg="darkblue",fg="white")
        btn3_3.place(x=455,y=220,width=150,height=40)


         # photos button
        img9=Image.open(r"C:\hello\python-project\images\gallary.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg9=ImageTk.PhotoImage(img9)

        btn4 = Button(bgimg_lbl,command=self.open_img,image=self.photoimg9,cursor="hand2")
        btn4.place(x=655,y=80,width=150,height=150)

        btn4_4 = Button(bgimg_lbl,command=self.open_img,text="Photos",cursor="hand2",font=("arial",10,"bold"),bg="darkblue",fg="white")
        btn4_4.place(x=655,y=220,width=150,height=40)


         # help desk button
        img10=Image.open(r"C:\hello\python-project\images\help_desk.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg10=ImageTk.PhotoImage(img10)

        btn5 = Button(bgimg_lbl,image=self.photoimg10,cursor="hand2")
        btn5.place(x=855,y=80,width=150,height=150)

        btn5_5 = Button(bgimg_lbl,text="Help Desk",cursor="hand2",font=("arial",10,"bold"),bg="darkblue",fg="white")
        btn5_5.place(x=855,y=220,width=150,height=40)


         # Exit button
        img11=Image.open(r"C:\hello\python-project\images\exit.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg11=ImageTk.PhotoImage(img11)

        btn6 = Button(bgimg_lbl,image=self.photoimg11,cursor="hand2")
        btn6.place(x=1050,y=80,width=150,height=150)

        btn6_6 = Button(bgimg_lbl,text="Exit",cursor="hand2",font=("arial",10,"bold"),bg="darkblue",fg="white")
        btn6_6.place(x=1050,y=220,width=150,height=40)

        # caregiver button
        img12=Image.open(r"C:\hello\python-project\images\img3.jpg")
        img12=img12.resize((150,150),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        self.photoimg12=ImageTk.PhotoImage(img12)

        btn7 = Button(bgimg_lbl,image=self.photoimg12,cursor="hand2",command= self.tarin_data)
        btn7.place(x=70,y=300,width=150,height=150)

        btn7_7 = Button(bgimg_lbl,text="Train Data",cursor="hand2",font=("arial",10,"bold"),bg="darkblue",fg="white",command= self.tarin_data)
        btn7_7.place(x=70,y=440,width=150,height=40)


    def open_img(self):
        os.startfile("data")

        # ================= Function button ======================

    def caregiver_details(self): 
        self.new_window = Toplevel(self.root)
        self.app = Caregiver(self.new_window)

    def tarin_data(self): 
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)    
        
    def detect_face(self): 
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)    
        
    def attendance(self): 
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)    
        
if __name__ == "__main__":
    root=Tk()
    obj = Face_recognition_sys(root)
    root.mainloop()

