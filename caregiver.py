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

        time_combo = ttk.Combobox(basic_details_frame,font=("arial",10,"bold"),width=17,state="readonly")
        time_combo["values"]=("select","Full Time","Part Time")
        time_combo.current(0)
        time_combo.grid(row=0,column=1,padx=5,pady=10)

        # Gender
        gender_lbl = Label(basic_details_frame,text="Gender",font=("arial",10,"bold"),bg='white')
        gender_lbl.grid(row=0,column=2,padx=10)

        gender_combo = ttk.Combobox(basic_details_frame,font=("arial",10,"bold"),width=17,state="readonly")
        gender_combo["values"]=("select","Male","Female","Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=0,column=3,padx=5,pady=10)
        
         # Care recipient
        care_recipient_lbl = Label(basic_details_frame,text="Care Recepient",font=("arial",10,"bold"),bg='white')
        care_recipient_lbl.grid(row=1,column=0,padx=10)

        care_recipient_combo = ttk.Combobox(basic_details_frame,font=("arial",10,"bold"),width=17,state="readonly")
        care_recipient_combo["values"]=("select","Elderly(over 60)","Adult with a disability(18 to 59)","child(under 15)")
        care_recipient_combo.current(0)
        care_recipient_combo.grid(row=1,column=1,padx=5,pady=10)
        
         # Care recipient
        state_lbl = Label(basic_details_frame,text="State",font=("arial",10,"bold"),bg='white')
        state_lbl.grid(row=1,column=2,padx=10)

        state_combo = ttk.Combobox(basic_details_frame,font=("arial",10,"bold"),width=17,state="readonly")
        state_combo["values"]=("select","Maharashtra","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Uttar Pradesh","Uttarakhand","West Bengal")
        state_combo.current(0)
        state_combo.grid(row=1,column=3,padx=5,pady=10)
        
     #   ================== Extra information =======================
        Extra_info_frame = LabelFrame(left_frame,bg="white",bd=2,relief=RIDGE,text="Extra Information",font=("arial",12,"bold"))
        Extra_info_frame.place(x=5,y=120,width=585,height=350)

        # caregiverId
        caregiverId_lbl = Label(Extra_info_frame,text="CaregiversID",font=("arial",10,"bold"),bg='white')
        caregiverId_lbl.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        caregiverId_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        caregiverId_entry.grid(row=0,column=1,padx=0,sticky=W)

        # Caregiver name
        caregiver_name_lbl = Label(Extra_info_frame,text="Caregiver's Name",font=("arial",10,"bold"),bg='white')
        caregiver_name_lbl.grid(row=0,column=2,padx=10,pady=7,sticky=W)

        caregiver_name_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        caregiver_name_entry.grid(row=0,column=3,padx=0,sticky=W)

        # mobile no
        mobile_no_lbl = Label(Extra_info_frame,text="Mobile No",font=("arial",10,"bold"),bg='white')
        mobile_no_lbl.grid(row=1,column=0,padx=10,pady=7,sticky=W)

        mobile_no_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        mobile_no_entry.grid(row=1,column=1,padx=0,sticky=W)

          # Caregiver email
        email_lbl = Label(Extra_info_frame,text="Email",font=("arial",10,"bold"),bg='white')
        email_lbl.grid(row=1,column=2,padx=10,pady=7,sticky=W)

        email_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        email_entry.grid(row=1,column=3,padx=0,sticky=W)

        # age
        age_lbl = Label(Extra_info_frame,text="Age",font=("arial",10,"bold"),bg='white')
        age_lbl.grid(row=2,column=0,padx=10,pady=7,sticky=W)

        age_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        age_entry.grid(row=2,column=1,padx=0,sticky=W)


         # date of birth
        dob_lbl = Label(Extra_info_frame,text="Date Of Birth",font=("arial",10,"bold"),bg='white')
        dob_lbl.grid(row=2,column=2,padx=10,pady=7,sticky=W)

        dob_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=0,sticky=W)


        # date of joining
        doj_lbl = Label(Extra_info_frame,text="Date of joining",font=("arial",10,"bold"),bg='white')
        doj_lbl.grid(row=3,column=0,padx=10,pady=7,sticky=W)

        doj_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        doj_entry.grid(row=3,column=1,padx=0,sticky=W)


         # emergency no
        city_lbl = Label(Extra_info_frame,text="Emergency No",font=("arial",10,"bold"),bg='white')
        city_lbl.grid(row=3,column=2,padx=10,pady=7,sticky=W)

        city_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        city_entry.grid(row=3,column=3,padx=0,sticky=W)

         # adreess
        address_lbl = Label(Extra_info_frame,text="Address",font=("arial",10,"bold"),bg='white')
        address_lbl.grid(row=4,column=0,padx=10,pady=7,sticky=W)

        address_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        address_entry.grid(row=4,column=1,padx=0,sticky=W)

         # recipient dises
        disease_lbl = Label(Extra_info_frame,text="Recipient Disease",font=("arial",10,"bold"),bg='white')
        disease_lbl.grid(row=4,column=2,padx=10,pady=7,sticky=W)

        disease_entry = ttk.Entry(Extra_info_frame,width=20,font=("arial",10,"bold"))
        disease_entry.grid(row=4,column=3,padx=0,sticky=W)


        # ==================== radio buttton ==============

        radiobtn1 = ttk.Radiobutton(Extra_info_frame,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=2,pady=2)

        radiobtn2 = ttk.Radiobutton(Extra_info_frame,text="No photo sample",value="Yes")
        radiobtn2.grid(row=5,column=1,padx=2,pady=2)


        # ==================== button frame ===================

        btn_frame = LabelFrame(Extra_info_frame,bg="white",bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=210,width=580,height=30)

        save_btn = Button(btn_frame,text="Save",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

            ################# frame for take a photo button ################
        btn2_frame = LabelFrame(Extra_info_frame,bg="white",bd=2,relief=RIDGE)
        btn2_frame.place(x=0,y=240,width=580,height=30)

        take_photo_btn = Button(btn2_frame,text="Take photo sample",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=35)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn2_frame,text="Update photo sample",font=("arial",10,"bold"),bg="RoyalBlue1",fg="white",width=35)
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


if __name__ == "__main__":
    root=Tk()
    obj = caregiver(root)
    root.mainloop()