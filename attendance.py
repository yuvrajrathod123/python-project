from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import pymysql

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        
        self.var_caregiverID = StringVar()
        self.var_caregiver_name = StringVar()
        self.var_adress = StringVar()
        self.var_Mo_no = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()
       



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

        title_lbl = Label(bgimg_lbl,text="ATTENDANCE MANAGEMENT SYSTEM",font=("arial",25,"bold"),bg="white",fg="black")
        title_lbl.place(relx=0.4,rely=0.03,width=1530,height=45,anchor=CENTER)


        # ====================== Frame =====================

        main_frame = Frame( bgimg_lbl,bd=2,bg="white")
        main_frame.place(x=5,y=50,width=1260,height=600)

          # ========================  left side label frame ============================

        left_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Caregiver Attendance Details",font=("arial",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=500)

        # main_frame = Frame( left_frame,bd=2,relief=RIDGE,bg="white")
        # main_frame.place(x=5,y=50,width=585,height=400)


        # ************* entry **************

         # caregiverId
        caregiverId_lbl = Label(left_frame,text="CaregiversID:",font=("arial",10,"bold"),bg='white')
        caregiverId_lbl.grid(row=0,column=0,padx=10,pady=20,sticky=W)

        caregiverId_entry = ttk.Entry(left_frame,textvariable=self.var_caregiverID,width=20,font=("arial",10,"bold"))
        caregiverId_entry.grid(row=0,column=1,padx=0,sticky=W)

        # Caregiver name
        caregiver_name_lbl = Label(left_frame,text="Caregiver's Name:",font=("arial",10,"bold"),bg='white')
        caregiver_name_lbl.grid(row=0,column=2,padx=10,pady=7,sticky=W)

        caregiver_name_entry = ttk.Entry(left_frame,width=20,textvariable=self.var_caregiver_name,font=("arial",10,"bold"))
        caregiver_name_entry.grid(row=0,column=3,padx=0,sticky=W)

         # adress
        address_lbl = Label(left_frame,text="Address",font=("arial",10,"bold"),bg='white')
        address_lbl.grid(row=1,column=0,padx=10,pady=30,sticky=W)

        address_entry = ttk.Entry(left_frame,textvariable=self.var_adress,width=20,font=("arial",10,"bold"))
        address_entry.grid(row=1,column=1,padx=0,sticky=W)

          # mo no
        mo_no_lbl = Label(left_frame,text="Mo no",font=("arial",10,"bold"),bg='white')
        mo_no_lbl.grid(row=1,column=2,padx=10,pady=7,sticky=W)

        mo_no_entry = ttk.Entry(left_frame,textvariable=self.var_Mo_no,width=20,font=("arial",10,"bold"))
        mo_no_entry.grid(row=1,column=3,padx=0,sticky=W)

        # time
        time_lbl = Label(left_frame,text="Time",font=("arial",10,"bold"),bg='white')
        time_lbl.grid(row=2,column=0,padx=10,pady=7,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=20,font=("arial",10,"bold"))
        time_entry.grid(row=2,column=1,padx=0,sticky=W)

          # date
        date_lbl = Label(left_frame,text="Date",font=("arial",10,"bold"),bg='white')
        date_lbl.grid(row=2,column=2,padx=10,pady=7,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=20,font=("arial",10,"bold"))
        date_entry.grid(row=2,column=3,padx=0,sticky=W)


          # attendance
        attendance_lbl = Label(left_frame,text="Attendance Status",font=("arial",10,"bold"),bg='white')
        attendance_lbl.grid(row=3,column=0,padx=15,pady=30,sticky=W)

        time_combo = ttk.Combobox(left_frame,textvariable=self.var_attendance, font=("arial",10,"bold"),width=17,state="readonly")
        time_combo["values"]=("Status","Present","Absent")
        time_combo.current(0)
        time_combo.grid(row=3,column=1,padx=5,pady=10)


        # ///////////////////// buttons ///////////////////////

         # back button
        back_btn = Button(bgimg_lbl,text="back",cursor="hand2",font=("arial",10,"bold"),bg="white",fg="darkred")
        back_btn.place(x=1100,y=0,width=100,height=42)

        btn_frame = LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=580,height=30)

        import_btn = Button(btn_frame,text="Import csv",command=self.importCsv,font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export csv",command=self.exportCsv,font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        export_btn.grid(row=0,column=1)

        # update_btn = Button(btn_frame,text="Update",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        # update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        reset_btn.grid(row=0,column=3)


         # ==================== right side label frame ==================
        right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attendance Details",font=("arial",12,"bold"))
        right_frame.place(x=620,y=10,width=625,height=580)

         # ===================== table frame ============================
        table_frame = Frame(right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=610,height=420)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.caregiver_table = ttk.Treeview(table_frame,column=("caregiverID","caregiver_name","address","mobile_no","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.caregiver_table.xview)
        scroll_y.config(command=self.caregiver_table.yview)

        self.caregiver_table.heading("caregiverID",text="CaregiversID")
        self.caregiver_table.heading("caregiver_name",text="Caregiver Name")
        self.caregiver_table.heading("address",text="Address")
        self.caregiver_table.heading("mobile_no",text="Mobile No")
        self.caregiver_table.heading("time",text="Time")
        self.caregiver_table.heading("date",text="Date")
        self.caregiver_table.heading("attendance",text="Attendance")
        self.caregiver_table["show"]="headings"
        

        self.caregiver_table.column("caregiverID",width=100)
        self.caregiver_table.column("caregiver_name",width=100)
        self.caregiver_table.column("address",width=100)
        self.caregiver_table.column("mobile_no",width=100)
        self.caregiver_table.column("time",width=100)
        self.caregiver_table.column("date",width=100)
        self.caregiver_table.column("attendance",width=100)
       

        self.caregiver_table.pack(fill=BOTH,expand=1)
        self.caregiver_table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()

  # ===================== fetch data ==============
    def fetchData(self,rows):
        self.caregiver_table.delete(*self.caregiver_table.get_children())
        for i in rows:
            self.caregiver_table.insert("",END,values=i)


# import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in  csvread:
                mydata.append(i)
            self.fetchData(mydata)    

# export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("error","No data found",parent= self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                export_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)

                messagebox.showinfo("Data Export","Your data exporte to "+os.path.basename(file_name)+" successfully!!")

        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # ======================= get cursor =======================

    def get_cursor(self,name):
        print(name)
        cursor_focus = self.caregiver_table.focus()
        content = self.caregiver_table.item(cursor_focus)
        data = content["values"] 

        self.var_caregiverID.set(data[0]),              
        self.var_caregiver_name.set(data[1]),              
        self.var_adress.set(data[2]),              
        self.var_Mo_no.set(data[3]),              
        self.var_time.set(data[4]),              
        self.var_date.set(data[5]),              
        self.var_attendance.set(data[6])             

  #  ==================== reset ====================
    def reset_data(self):   
        self.var_caregiverID.set(" "),              
        self.var_caregiver_name.set(" "),              
        self.var_adress.set(" "),              
        self.var_Mo_no.set(" "),              
        self.var_time.set(" "),              
        self.var_date.set(" "),              
        self.var_attendance.set(" ")             
   
    # def update_data(self):
    #     if self.var_adress() == "Select working_mode" or self.var_caregiver_name.get() == ""  or self.var_caregiverID.get() == "":
    #         messagebox.showerror("Error","All fields are required",parent =self.root)
    #     else:
    #         try:
    #             update= messagebox.askyesno("Update","Do you want to update this caregiver details",parent=self.root)
    #             if update>0:
    #                 conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)
    #                 my_cursor=conn.cursor()

    #                 my_cursor.execute("update caregiver set Caregiver_Name=%s,Email=%s,Age=%s,DOB=%s,DOJ=%s,Emergency_No=%s,Address=%s,Recepient_Disease=%s,Attendance=%s where CaregiverID=%s",(

    #                                                             self.var_caregiver_name.get(),
    #                                                             self.var_adress.get(),
    #                                                             self.var_Mo_no.get(),
    #                                                             self.var_time.get(),
    #                                                             self.var_date.get(),
    #                                                             self.var_attendance.get(),
    #                                                             self.var_caregiverID.get()
    #                                              ))
                    

    #             else:
    #                 if not update:
    #                     return
    #             messagebox.showinfo("Success","Caregiver details successfully updated",parent=self.root)              
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

      


if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()