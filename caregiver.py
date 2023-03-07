from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
import cv2

import pymysql

class Caregiver:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")


        # ======================== Variables =====================

        self.var_working_mode = StringVar()
        self.var_gender = StringVar()
        self.var_care_recipient = StringVar()
        self.var_state = StringVar()
        self.var_caregiverID = StringVar()
        self.var_caregiver_name = StringVar()
        self.var_Mo_no = StringVar()
        self.var_email = StringVar()
        self.var_age = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.Var_Emergency_no = StringVar()
        self.var_adress = StringVar()
        self.var_recipient_disease = StringVar()

    
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
        left_frame.place(x=10,y=10,width=600,height=500)

        # img_left=Image.open(r"C:\hello\python-project\images\img2.png")
        # img_left=img_left.resize((580,130),Image.ANTIALIAS)  #ANTILIAS converts high level img to low level
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=580,height=130)

        # basic details
        basic_details_frame = LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Basic Details",font=("arial",12,"bold"))
        basic_details_frame.place(x=5,y=10,width=585,height=110)

        # basic details content
        # Working mode
        time_lbl = Label(basic_details_frame,text="Working Mode",font=("arial",10,"bold"),bg='white')
        time_lbl.grid(row=0,column=0,padx=10)

        time_combo = ttk.Combobox(basic_details_frame,textvariable=self.var_working_mode, font=("arial",10,"bold"),width=17,state="readonly")
        time_combo["values"]=("select","Full Time","Part Time")
        time_combo.current(0)
        time_combo.grid(row=0,column=1,padx=5,pady=10)

        # Gender
        gender_lbl = Label(basic_details_frame,text="Gender",font=("arial",10,"bold"),bg='white')
        gender_lbl.grid(row=0,column=2,padx=10)

        gender_combo = ttk.Combobox(basic_details_frame,textvariable=self.var_gender,font=("arial",10,"bold"),width=17,state="readonly")
        gender_combo["values"]=("select","Male","Female","Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=0,column=3,padx=5,pady=10)
        
         # Care recipient
        care_recipient_lbl = Label(basic_details_frame,text="Care Recepient",font=("arial",10,"bold"),bg='white')
        care_recipient_lbl.grid(row=1,column=0,padx=10)

        care_recipient_combo = ttk.Combobox(basic_details_frame,textvariable=self.var_care_recipient,font=("arial",10,"bold"),width=17,state="readonly")
        care_recipient_combo["values"]=("select","Elderly(over 60)","Adult with a disability(18 to 59)","child(under 15)")
        care_recipient_combo.current(0)
        care_recipient_combo.grid(row=1,column=1,padx=5,pady=10)
        
         # Care recipient
        state_lbl = Label(basic_details_frame,text="State",font=("arial",10,"bold"),bg='white')
        state_lbl.grid(row=1,column=2,padx=10)

        state_combo = ttk.Combobox(basic_details_frame,textvariable=self.var_state,font=("arial",10,"bold"),width=17,state="readonly")
        state_combo["values"]=("select","Maharashtra","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Uttar Pradesh","Uttarakhand","West Bengal")
        state_combo.current(0)
        state_combo.grid(row=1,column=3,padx=5,pady=10)
        
     #   ================== Extra information =======================
        Extra_info_frame = LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Extra Information",font=("arial",12,"bold"))
        Extra_info_frame.place(x=5,y=120,width=585,height=350)

        # caregiverId
        caregiverId_lbl = Label(Extra_info_frame,text="CaregiversID",font=("arial",10,"bold"),bg='white')
        caregiverId_lbl.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        caregiverId_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_caregiverID,width=20,font=("arial",10,"bold"))
        caregiverId_entry.grid(row=0,column=1,padx=0,sticky=W)

        # Caregiver name
        caregiver_name_lbl = Label(Extra_info_frame,text="Caregiver's Name",font=("arial",10,"bold"),bg='white')
        caregiver_name_lbl.grid(row=0,column=2,padx=10,pady=7,sticky=W)

        caregiver_name_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_caregiver_name,width=20,font=("arial",10,"bold"))
        caregiver_name_entry.grid(row=0,column=3,padx=0,sticky=W)

        # mobile no
        mobile_no_lbl = Label(Extra_info_frame,text="Mobile No",font=("arial",10,"bold"),bg='white')
        mobile_no_lbl.grid(row=1,column=0,padx=10,pady=7,sticky=W)

        mobile_no_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_Mo_no,width=20,font=("arial",10,"bold"))
        mobile_no_entry.grid(row=1,column=1,padx=0,sticky=W)

          # Caregiver email
        email_lbl = Label(Extra_info_frame,text="Email",font=("arial",10,"bold"),bg='white')
        email_lbl.grid(row=1,column=2,padx=10,pady=7,sticky=W)

        email_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_email,width=20,font=("arial",10,"bold"))
        email_entry.grid(row=1,column=3,padx=0,sticky=W)

        # age
        age_lbl = Label(Extra_info_frame,text="Age",font=("arial",10,"bold"),bg='white')
        age_lbl.grid(row=2,column=0,padx=10,pady=7,sticky=W)

        age_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_age,width=20,font=("arial",10,"bold"))
        age_entry.grid(row=2,column=1,padx=0,sticky=W)


         # date of birth
        dob_lbl = Label(Extra_info_frame,text="Date Of Birth",font=("arial",10,"bold"),bg='white')
        dob_lbl.grid(row=2,column=2,padx=10,pady=7,sticky=W)

        dob_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_dob,width=20,font=("arial",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=0,sticky=W)


        # date of joining
        doj_lbl = Label(Extra_info_frame,text="Date of joining",font=("arial",10,"bold"),bg='white')
        doj_lbl.grid(row=3,column=0,padx=10,pady=7,sticky=W)

        doj_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_doj,width=20,font=("arial",10,"bold"))
        doj_entry.grid(row=3,column=1,padx=0,sticky=W)


         # emergency no
        city_lbl = Label(Extra_info_frame,text="Emergency No",font=("arial",10,"bold"),bg='white')
        city_lbl.grid(row=3,column=2,padx=10,pady=7,sticky=W)

        city_entry = ttk.Entry(Extra_info_frame,textvariable=self.Var_Emergency_no,width=20,font=("arial",10,"bold"))
        city_entry.grid(row=3,column=3,padx=0,sticky=W)

         # adreess
        address_lbl = Label(Extra_info_frame,text="Address",font=("arial",10,"bold"),bg='white')
        address_lbl.grid(row=4,column=0,padx=10,pady=7,sticky=W)

        address_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_adress,width=20,font=("arial",10,"bold"))
        address_entry.grid(row=4,column=1,padx=0,sticky=W)

         # recipient dises
        disease_lbl = Label(Extra_info_frame,text="Recipient Disease",font=("arial",10,"bold"),bg='white')
        disease_lbl.grid(row=4,column=2,padx=10,pady=7,sticky=W)

        disease_entry = ttk.Entry(Extra_info_frame,textvariable=self.var_recipient_disease,width=20,font=("arial",10,"bold"))
        disease_entry.grid(row=4,column=3,padx=0,sticky=W)


        # ==================== radio buttton ==============

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Extra_info_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=2,pady=2)

        
        radiobtn2 = ttk.Radiobutton(Extra_info_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=2,pady=2)


        # ==================== button frame ===================

        btn_frame = LabelFrame(Extra_info_frame,bg="white",bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=580,height=30)

        save_btn = Button(btn_frame,command=self.add_data,text="Save",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,command=self.update_data,text="Update",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

         # back button
        back_btn = Button(bgimg_lbl,text="back",cursor="hand2",font=("arial",10,"bold"),bg="white",fg="darkred")
        back_btn.place(x=1100,y=0,width=100,height=42)
        
            ################# frame for take a photo button ################
        btn2_frame = LabelFrame(Extra_info_frame,bg="white",bd=2,relief=RIDGE)
        btn2_frame.place(x=0,y=240,width=580,height=30)

        take_photo_btn = Button(btn2_frame,command=self.generate_dataset,text="Take photo sample",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=35)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn2_frame,command=self.generate_dataset,text="Update photo sample",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=35)
        update_photo_btn.grid(row=0,column=2)

















        # ==================== right side label frame ==================
        right_frame = LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Caregiver Details",font=("arial",12,"bold"))
        right_frame.place(x=620,y=10,width=625,height=580)

        # ============================== searching systm ==============================

        search_frame = LabelFrame(right_frame,bg="white",bd=2,relief=RIDGE,text="Search System",font=("arial",12,"bold"))
        search_frame.place(x=5,y=7,width=610,height=70)

        search_lbl = Label(search_frame,text="Search By",font=("arial",12,"bold"),bg='red',fg="white")
        search_lbl.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("arial",10,"bold"),width=15,state="readonly")
        search_combo["values"]=("select","CaregiverID","Mobile No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=20,font=("arial",10,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=10)
        search_btn.grid(row=0,column=3,padx=5)

        show_all_btn = Button(search_frame,text="Show All",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=10)
        show_all_btn.grid(row=0,column=4)


        # ===================== table frame ============================
        table_frame = Frame(right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=80,width=610,height=350)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.caregiver_table = ttk.Treeview(table_frame,column=("caregiverID","working_mode","gender","care_recipient","state","caregiver_name","mobile_no","email","age","dob","date_of_joining","emergency_no","address","recipient_disease","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.caregiver_table.xview)
        scroll_y.config(command=self.caregiver_table.yview)

        self.caregiver_table.heading("caregiverID",text="CaregiversID")
        self.caregiver_table.heading("working_mode",text="Working Mode")
        self.caregiver_table.heading("gender",text="Gender")
        self.caregiver_table.heading("care_recipient",text="Care Recipient")
        self.caregiver_table.heading("state",text="State")
        self.caregiver_table.heading("caregiver_name",text="Caregiver Name")
        self.caregiver_table.heading("mobile_no",text="Mobile No")
        self.caregiver_table.heading("email",text="Email")
        self.caregiver_table.heading("age",text="Age")
        self.caregiver_table.heading("dob",text="DOB")
        self.caregiver_table.heading("date_of_joining",text="Date Of Joining")
        self.caregiver_table.heading("emergency_no",text="Emergency No")
        self.caregiver_table.heading("address",text="Address")
        self.caregiver_table.heading("recipient_disease",text="Recipient Disease")
        self.caregiver_table.heading("photo",text="Photo")
        self.caregiver_table["show"]="headings"

        self.caregiver_table.column("caregiverID",width=100)
        self.caregiver_table.column("working_mode",width=100)
        self.caregiver_table.column("gender",width=100)
        self.caregiver_table.column("care_recipient",width=100)
        self.caregiver_table.column("state",width=100)
        self.caregiver_table.column("caregiver_name",width=100)
        self.caregiver_table.column("mobile_no",width=100)
        self.caregiver_table.column("email",width=100)
        self.caregiver_table.column("age",width=100)
        self.caregiver_table.column("dob",width=100)
        self.caregiver_table.column("date_of_joining",width=100)
        self.caregiver_table.column("emergency_no",width=100)
        self.caregiver_table.column("address",width=100)
        self.caregiver_table.column("recipient_disease",width=100)
        self.caregiver_table.column("photo",width=100)

        self.caregiver_table.pack(fill=BOTH,expand=1)
        self.caregiver_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

#    =========================== Function =====================

    def add_data(self):
        if self.var_working_mode.get() == "Select working_mode" or self.var_caregiver_name.get() == ""  or self.var_caregiverID.get() == "":
            messagebox.showerror("Error","All fields are required",parent =self.root)
        else:
            try:
                # messagebox.showinfo("Done","Registration Successful") 
                # conn = mysql.connector.connect(host="localhost",username="root",password="Yuvraj@5587", database="face_recognition")

                conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)

                my_cursor=conn.cursor()
                my_cursor.execute("insert into caregiver values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                self.var_working_mode.get(),
                                                                self.var_gender.get(),
                                                                self.var_care_recipient.get(),
                                                                self.var_state.get(),
                                                                self.var_caregiverID.get(),
                                                                self.var_caregiver_name.get(),
                                                                self.var_Mo_no.get(),
                                                                self.var_email.get(),
                                                                self.var_age.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.Var_Emergency_no.get(),
                                                                self.var_adress.get(),
                                                                self.var_recipient_disease.get(),
                                                                self.var_radio1.get()
                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Caregiver details has been added Successfully",parent=self.root)   

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

# ========================== fetch data =======================

    def fetch_data(self):
        conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)
        my_cursor=conn.cursor()

        my_cursor.execute("select * from caregiver")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.caregiver_table.delete(*self.caregiver_table.get_children())
            for i in data:
                self.caregiver_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# ======================= get cursor =======================

    def get_cursor(self,name):
        print(name)
        cursor_focus = self.caregiver_table.focus()
        content = self.caregiver_table.item(cursor_focus)
        data = content["values"] 

        self.var_working_mode.set(data[0]),              
        self.var_gender.set(data[1]),              
        self.var_care_recipient.set(data[2]),              
        self.var_state.set(data[3]),              
        self.var_caregiverID.set(data[4]),              
        self.var_caregiver_name.set(data[5]),              
        self.var_Mo_no.set(data[6]),              
        self.var_email.set(data[7]),              
        self.var_age.set(data[8]),              
        self.var_dob.set(data[9]),              
        self.var_doj.set(data[10]),              
        self.Var_Emergency_no.set(data[11]),              
        self.var_adress.set(data[12]),              
        self.var_recipient_disease.set(data[13]),
        self.var_radio1.set(data[14])
             

#  ====================== update ======================
# 
    def update_data(self):
        if self.var_working_mode.get() == "Select working_mode" or self.var_caregiver_name.get() == ""  or self.var_caregiverID.get() == "":
            messagebox.showerror("Error","All fields are required",parent =self.root)
        else:
            try:
                update= messagebox.askyesno("Update","Do you want to update this caregiver details",parent=self.root)
                if update>0:
                    conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)
                    my_cursor=conn.cursor()

                    my_cursor.execute("update caregiver set Working_Mode=%s,Gender=%s,Care_Recepient=%s,State=%s,Caregiver_Name=%s,Mobile_No=%s,Email=%s,Age=%s,DOB=%s,DOJ=%s,Emergency_No=%s,Address=%s,Recepient_Disease=%s,PhotoSample=%s where CaregiverID=%s",(

                                                                self.var_working_mode.get(),
                                                                self.var_gender.get(),
                                                                self.var_care_recipient.get(),
                                                                self.var_state.get(),
                                                                self.var_caregiver_name.get(),
                                                                self.var_Mo_no.get(),
                                                                self.var_email.get(),
                                                                self.var_age.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.Var_Emergency_no.get(),
                                                                self.var_adress.get(),
                                                                self.var_recipient_disease.get(),
                                                                self.var_radio1.get(),
                                                                self.var_caregiverID.get()
                                                 ))
                    

                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Caregiver details successfully updated",parent=self.root)              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ======================= detete details ======================
    def delete_data(self):
        if self.var_caregiverID.get() == "":
            messagebox.showerror("Error","Student id required",parent= self.root)
        else:
            try:
                delete= messagebox.askyesno("Update","Do you want to delete this caregiver details",parent=self.root)
                if delete>0:
                    conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)
                    my_cursor=conn.cursor()
                    sql = "delete from caregiver where CaregiverID=%s"
                    val=(self.var_caregiverID.get())
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted caregivers details",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

# ================ Reset ==============

    def reset_data(self):
        self.var_working_mode.set("select")
        self.var_gender.set("select")
        self.var_care_recipient.set("select")
        self.var_state.set("select")
        self.var_caregiverID.set("")
        self.var_caregiver_name.set("")
        self.var_Mo_no.set("")
        self.var_email.set("")
        self.var_age.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.Var_Emergency_no.set("")
        self.var_adress.set("")
        self.var_recipient_disease.set("")
        self.var_radio1.set("")

# ====================  take a photo sample ====================

    def generate_dataset(self):
        if self.var_working_mode.get() == "Select working_mode" or self.var_caregiver_name.get() == ""  or self.var_caregiverID.get() == "":
            messagebox.showerror("Error","All fields are required",parent =self.root)
        else:
            try:
                conn =  pymysql.connect(host="localhost",database="face_recognition",user="root",password="Yuvraj@5587",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("select * from caregiver")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update caregiver set Working_Mode=%s,Gender=%s,Care_Recepient=%s,State=%s,Caregiver_Name=%s,Mobile_No=%s,Email=%s,Age=%s,DOB=%s,DOJ=%s,Emergency_No=%s,Address=%s,Recepient_Disease=%s,PhotoSample=%s where CaregiverID=%s",(

                                                                self.var_working_mode.get(),
                                                                self.var_gender.get(),
                                                                self.var_care_recipient.get(),
                                                                self.var_state.get(),
                                                                self.var_caregiver_name.get(),
                                                                self.var_Mo_no.get(),
                                                                self.var_email.get(),
                                                                self.var_age.get(),
                                                                self.var_dob.get(),
                                                                self.var_doj.get(),
                                                                self.Var_Emergency_no.get(),
                                                                self.var_adress.get(),
                                                                self.var_recipient_disease.get(),
                                                                self.var_radio1.get(),
                                                                self.var_caregiverID.get() == id+1
                                                 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                
                # haar cascade algorithm to detect the object
                # ========== load predefine data on face frontal from opencv ========

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor == 1.3
                    # minimum neighbour == 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                #  opening camera  
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path ="data/user."+str(id)+"."+ str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    # here 13 is when we click on enter window will close AND 100 image sample
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release() 
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets complete succesfully!!",parent=self.root) 

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj = Caregiver(root)
    root.mainloop()