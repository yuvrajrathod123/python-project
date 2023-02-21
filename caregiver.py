from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class caregiver:
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

        title_lbl = Label(bgimg_lbl,text="CAREGIVER MANAGEMENT SYSTEM",font=("arial",25,"bold"),bg="white",fg="black")
        title_lbl.place(relx=0.4,rely=0.03,width=1530,height=45,anchor=CENTER)


        # ====================== Frame =====================

        main_frame = Frame( bgimg_lbl,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1260,height=600)

        # ========================  left side label frame ============================

        left_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Caregiver Details",font=("arial",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=580)

        # img_left=Image.open(r"C:\hello\python-project\images\img2.png")
        # img_left=img_left.resize((580,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=580,height=130)

        # basic details
        left_frame = LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Basic Details",font=("arial",12,"bold"))
        left_frame.place(x=5,y=10,width=585,height=150)

        


        # right side label frame
        right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Caregiver Details",font=("arial",12,"bold"))
        right_frame.place(x=620,y=10,width=625,height=580)


if __name__ == "__main__":
    root=Tk()
    obj = caregiver(root)
    root.mainloop()