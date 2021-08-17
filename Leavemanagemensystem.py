from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from tkinter.ttk import *
from tkinter import ttk
import datetime


import pymysql


                      
win=Tk()
win.title("firstwindow")
win.geometry("1250x700+0+0")
image=ImageTk.PhotoImage(file='image/adminimg.jpg')
bgLabel=Label(win,image=image)
bgLabel.place(x=0,y=0)

title=Label(win,text="Student Leave Management System",font=("times new roman",40,"bold"))
title.pack(side=TOP,fill=X)

#title=Label(win,text="Student Leave Management System",relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
#title.pack(side=TOP,fill=X)
#title=Label(win,text="Student Leave Management System",relief=GROOVE,font=("times new roman",40,"bold"))
#title.place(x=50,y=30)

win.resizable(False,False)


frm=Frame(win)
frm.pack(padx=0,pady=0,anchor="nw")
#image=ImageTk.PhotoImage(file='image/adminimg.jpg')
#bgLabel=Label(win,image=image)
#bgLabel.place(x=0,y=0)

class Register:
    def __init__(self):
     global my4,top5,win
     global txt_sname
     
     #win.withdraw()
     top5=Toplevel()
     top5.title("Student Registration......")
     my4=ImageTk.PhotoImage(file="image/lapi4.jpg")   
     mylabel=Label(top5,image=my4).pack()
     frame1=Frame(top5)
     frame1.place(x=480,y=100,width=700,height=500)
     title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold")).place(x=50,y=30)
     scode=Label(frame1,text="Student code",font=("times new roman",15,"bold")).place(x=50,y=100)
     self.txt_scode=Entry(frame1,font=("times new roman",15))
     self.txt_scode.place(x=50,y=130,width=250)

     sname=Label(frame1,text="Student Name",font=("times new roman",15,"bold")).place(x=370,y=100)
     self.txt_sname=Entry(frame1,font=("times new roman",15))
     self.txt_sname.place(x=370,y=130,width=250)
        #---------------------------------------------------------row2

     contact=Label(frame1,text="Contact No",font=("times new roman",15,"bold")).place(x=50,y=170)
     self.txt_contact=Entry(frame1,font=("times new roman",15))
     self.txt_contact.place(x=50,y=200,width=250)
     dept=Label(frame1,text="Department",font=("times new roman",15,"bold")).place(x=370,y=170)
     self.dept=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
     self.dept['values']=("select","Computer Engineering","Electronics and Telecommunication","Electrical Engineering","Civil Engineering","Mechanical Engineering")
     self.dept.place(x=370,y=200,width=250)
     self.dept.current(0)
     Address=Label(frame1,text="Address",font=("times new roman",15,"bold")).place(x=50,y=240)
     self.txt_Address=Entry(frame1,font=("times new roman",15))
     self.txt_Address.place(x=50,y=270,width=250)
     email=Label(frame1,text="Email",font=("times new roman",15,"bold")).place(x=370,y=240)
     self.txt_email=Entry(frame1,font=("times new roman",15))
     self.txt_email.place(x=370,y=270,width=250)
        
      #==============================row4  
        
     password=Label(frame1,text="Password",font=("times new roman",15,"bold")).place(x=50,y=310)
     self.txt_password=Entry(frame1,show="*",font=("times new roman",15,"bold"))
     self.txt_password.place(x=50,y=340,width=250)
        
     c_pswd=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold")).place(x=370,y=310)
     self.txt_c_pswd=Entry(frame1,show="*",font=("times new roman",15))
     self.txt_c_pswd.place(x=370,y=340,width=250)
        
     self.var_chk=IntVar()
     chk=Checkbutton(frame1,text="I am Agree The terms and conditions",variable=self.var_chk,onvalue=1,offvalue=0).place(x=50,y=380)
     logout=Button(top5,text='LogOut',command=logOut4,compound=LEFT)
     logout.place(x=1100,y=20)
     btn_register=Button(frame1,text="Register Now",cursor="hand2",command=self.register_data,compound=LEFT).place(x=60,y=420)
    def  clear(self):
                self.txt_scode.delete(0,END),
                self.txt_sname.delete(0,END),
                self.txt_contact.delete(0,END),
                self.dept.current(0),
                self.txt_contact.delete(0,END),
                self.txt_Address.delete(0,END)
                self.txt_email.delete(0,END),
                self.txt_password.delete(0,END),
                self.txt_c_pswd.delete(0,END)
                


    def  register_data(self):

        
          if self.txt_scode.get()=="" or self.txt_sname.get()=="" or self.txt_contact.get()=="" or self.dept.get()=="select" or self.txt_Address.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_c_pswd.get()=="": 
              messagebox.showerror("error","all fields are required")
          elif self.txt_password.get()!=self.txt_c_pswd.get():
                 messagebox.showerror("Error","Password and Confirm password should be same") 
          elif self.var_chk.get()==0:
                 messagebox.showerror("Error","Please Agree The Terms And Conditons") 
          
          else:
              try:
                  con=pymysql.connect(host="localhost",user="root",password="",database="registration")
                  cur=con.cursor()
                  cur.execute("SELECT * FROM reg_info where email=%s",self.txt_email.get())
                  row=cur.fetchone()
                  print(row)
                  if row!=None:
                     messagebox.showerror("Error","User Already Exists please try with another email") 
                  else:
                       cur.execute("INSERT INTO reg_info(scode,sname,contact,dept,Address,email,password) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (self.txt_scode.get(),self.txt_sname.get(),self.txt_contact.get(),self.dept.get(),self.txt_Address.get(),self.txt_email.get(),self.txt_password.get())             )
                       con.commit()
                       con.close()
                       messagebox.showinfo("success","Registration successful") 
                       self.clear()
              except Exception as es:
                  messagebox.showerror("Error",f"Error due to: {str(es)}")
        
     
        
btn1 =Button(win,text ='Registration',command=Register,compound=LEFT)  
btn1.place(x=400,y=250) 

            
def logOut4():
    global top5
    top5.withdraw()
    print("logged out successfulyy")

    
def open():
    global my
    top=Toplevel()
    top.title("second window")
    my=ImageTk.PhotoImage(file="image/lapi4.jpg")   
    mylabel=Label(top,image=my).pack()
    style = Style() 
    style.configure('TButton', font=('calibri', 20, 'bold'), 
					borderwidth = '4') 
   
    btn1 = Button(top,text ='HOD Login',command=HODlogin,compound=LEFT)  
    btn1.place(x=400,y=250) 
    
    btn1 = Button(top,text ='Class Teacher Login',command=teacherlogin1,compound=LEFT)  
    btn1.place(x=650,y=250) 

    btn1 = Button(top,text ='Dean Student Login')  
    btn1.place(x=350,y=400) 
    btn1 = Button(top,text ='Student Login',command=studentlogin,compound=LEFT)  
    btn1.place(x=650,y=400) 

   

btn1=Button(win,text ='Login',command=open)  
btn1.place(x=650,y=250) 
class HODlogin(): 
    def __init__(self):
        global win
        win.withdraw()
         
        global my1
        top1=Toplevel()
        top1.title("Student Login")
        my1=ImageTk.PhotoImage(file="image/lapi4.jpg")   
        myl=Label(top1,image=my1).pack()
       
        frame_login=Frame(top1)
        frame_login.place(x=150,y=150,height=340,width=500)
        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold")).place(x=90,y=30)
        desc=Label(frame_login,text="HOD Login",font=("goudy old style",15,"bold")).place(x=90,y=100)
       #-----------username
  
        lbl_user=Label(frame_login,text="Username",font=("goudy old style",15,"bold")).place(x=90,y=140)
        self.txt_user=Entry(frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
      #---------------------password  
      
        lbl_pass=Label(frame_login,text="Password",font=("goudy old style",15,"bold")).place(x=90,y=210)
        self.txt_pass=Entry(frame_login,font=("times new roman",15),show="*")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
    #forget=Button(frame_login,text="Forget password?",font=("times new roman",12)).place(x=90,y=280) 
        login_btn=Button(top1,text="Sign In",command=self.HOD,compound=LEFT).place(x=300,y=470,width=180,height=40)
    userID='urEmailDomain'
   
    def HOD(self):
        global userID
        try:
            connection=pymysql.connect(host='localhost',user='root',password="",db='registration')
        except:  
             print("you are not connected to the server(localhost)")
        else:       
            print("connected successfully")
       # print("enter ur email and password")
        Email=self.txt_user.get()
        Password=self.txt_pass.get()
        cur=connection.cursor()
        query="SELECT username,password FROM hodlogin"
        cur.execute(query)
        for (email,pas) in cur:
              if Email==email and Password==pas:
                  login=True
                  break
              else:
                login=False
        userID= (Email.split('@') [0])
        if login==True:
             print("logged in successfully as",userID)
             HODWindow()
            
        elif login==False:
            messagebox.showerror("Error","username and passowrd is wrong")


userID='urEmailDomain'
home='urhomewindow'
def HODWindow():         
    global userID,home,bg1
    home=Toplevel()
    home.title("Student Leave Project")
    home.geometry("1350x700+0+0")
    frm=Frame(home)
    frm.pack(padx=0,pady=0,anchor="nw")
   
    win.withdraw()
    connection=pymysql.connect(host='localhost',user='root',password="",db='registration')
    cur=connection.cursor() 
 
    sql2="SELECT email,leavestatus,Remark FROM action"
     

    cur.execute(sql2)
    rows=cur.fetchall()
    tv=Treeview(frm,columns=(1,2,3),show="headings")


    tv.pack(side=TOP,pady=10)
    tv.heading(1,text="Email")
    tv.column(1,minwidth=0,width=150, stretch=YES)
    
    tv.heading(2,text="Leavestatus")
    tv.column(2,minwidth=0,width=200, stretch=NO)
    tv.heading(3,text="Remark")
    tv.column(3,minwidth=0,width=150, stretch=NO)
    for i in rows:
            tv.insert('','end',values=i)
  
    
    

 

    something=Label(home,text="You are logged in Successfully\n{}".format(userID))
    something.place(x=1000,y=20)
   
class teacherlogin1():
     def __init__(self):

          global image
          root1=Toplevel()
          root1.title('Teacher Login window')
          
        #  root1.resizable(0,0)
          image=ImageTk.PhotoImage(file='image/lapi4.jpg')
          bgLabel=Label(root1,image=image).pack()
#login system
          site=Label(root1,text="Teacher Login",font=('arial',15,'bold','underline'))
          site.place(x=550,y=160)
#USERNAME
          Username=Label(root1,text="Username:",font=('arial',10,'bold')).place(x=500,y=220)
          self.User=Entry(root1,width=30,font=('calibri',12))
          self.User.place(x=620,y=220)
#PASSWORD
          password=Label(root1,text="Password:",font=('arial',10,'bold')).place(x=500,y=270)
          self.Pass=Entry(root1,show="*",width=30,font=('calibri',12))
          self.Pass.place(x=620,y=270)
#SUBMIT
          submit=Button(root1,text='Login',command=self.teacherlogin,compound=LEFT)
          submit.place(x=570,y=360)
     userID='urEmailDomain'
     home='urhomewindow'
     def teacherlogin(self):
        global userID,win
        win.withdraw()
        try:
            connection=pymysql.connect(host='localhost',user='root',password="",db='registration')
        except:  
         print("you are not connected to the server(localhost)")
        else:       
          print("connected successfully")
       # print("enter ur Email and password")
          Email=self.User.get()
          Password=self.Pass.get()
          cur=connection.cursor()
          query="SELECT username,password FROM teacher"
          cur.execute(query)
          for (email,pas) in cur:
             if Email==email and Password==pas:
                  login=True
                  break
             else:
                login=False
          userID=(Email.split('@') [0])
          if login==True:
             print("logged in successfully as ",userID)
             Student()
          elif login==False:
                  messagebox.showerror("Error","username and passowrd is wrong")


 # def Leave(self):
class Student():
        
                   
        def __init__(self):
              style = Style() 
              style.configure('TButton', font =
			       ('calibri', 10, 'bold'), 
            				borderwidth = '4') 

              top2=Toplevel()
              top2.title("Teacher Action")
              top2.geometry("1350x700+0+0")
              title=Label(top2,text="Student Leave Management System",font=("times new roman",40,"bold"))
              title.pack(side=TOP,fill=X)
        #========all variaables
              self.rollno_var=StringVar()
              self.email_var=StringVar()
              self.fromdate_var=StringVar()
              self.todate_var=StringVar()
              self.status_var=StringVar()
              self.search_by=StringVar()
              self.searchall=StringVar()
              self.adminstatus_var=StringVar()
              manage_frame=Frame(top2)
              manage_frame.place(x=20,y=100,width=450,height=560)
              detail_frame=Frame(top2)
              detail_frame.place(x=500,y=100,width=750,height=560)
              m_title=Label(manage_frame,text="Manage Students",font=("times new roman",30,"bold"))
              m_title.grid(row=0,columnspan=2,pady=20)
       
              m_roll=Label(manage_frame,text="Email",font=("times new roman",20,"bold"))
              m_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

              txt_roll=Entry(manage_frame,textvariable=self.rollno_var,font=("times new roman",15,"bold"))
              txt_roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")

              m_name=Label(manage_frame,text="Leavetype",font=("times new roman",20,"bold"))
              m_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")

              txt_email=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"))
              txt_email.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        
              m_fdate=Label(manage_frame,text="From Date",font=("times new roman",20,"bold"))
              m_fdate.grid(row=3,column=0,pady=10,padx=10,sticky="w")

              txt_fdate=Entry(manage_frame,textvariable=self.fromdate_var,font=("times new roman",15,"bold"))
              txt_fdate.grid(row=3,column=1,pady=10,padx=10,sticky="w")

              m_tdate=Label(manage_frame,text="ToDate",font=("times new roman",20,"bold"))
              m_tdate.grid(row=4,column=0,pady=10,padx=10,sticky="w")

              txt_tdate=Entry(manage_frame,textvariable=self.todate_var,font=("times new roman",15,"bold"))
              txt_tdate.grid(row=4,column=1,pady=10,padx=10,sticky="w")

              m_status=Label(manage_frame,text="ApplyLeaveDate",font=("times new roman",20,"bold"))
              m_status.grid(row=5,column=0,pady=10,padx=10,sticky="w")

              txt_status=Entry(manage_frame,textvariable=self.status_var,font=("times new roman",15,"bold"))
              txt_status.grid(row=5,column=1,pady=10,padx=10,sticky="w")

              admin_status=Label(manage_frame,text="Status",font=("times new roman",20,"bold"))
              admin_status.grid(row=6,column=0,pady=10,padx=10,sticky="w")

              admin_status=Entry(manage_frame,textvariable=self.adminstatus_var,font=("times new roman",15,"bold"))
              admin_status.grid(row=6,column=1,pady=10,padx=10,sticky="w")
              x=datetime.datetime.now()
              self.time1=x.strftime("%m-%d-%y %H:%M:%S")
              time2=Label(top2,text="current time:\n{}".format(self.time1))
              time2.place(x=800,y=10)
#============>button frame===========================================
              btn_frame=Frame(manage_frame)
              btn_frame.place(x=10,y=450,width=430)
       
              Addbtn=Button(btn_frame,text="Submit",width=10,command=self.add_student).grid(row=0,column=0,padx=5,pady=10)
              updatebtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=5,pady=10)
              delbtn=Button(btn_frame,text="Deny Leave",width=10,command=self.delete_data).grid(row=0,column=2,padx=5,pady=10)
              clearbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=5,pady=10)
              
             
#============detail frame============================================
        
              detail_frame=Frame(top2)
              detail_frame.place(x=500,y=100,width=800,height=580)
       
              lbl_search=Label(detail_frame,text="Search By",font=("times new roman",20,"bold"))
              lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
              combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
              combo_search['value']=("email")
              combo_search.grid(row=0,column=1,padx=20,pady=10)
              txt_search=Entry(detail_frame,textvariable=self.searchall,font=("times new roman",10,"bold"))
              txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

              searchbtn=Button(detail_frame,text="Search",width=10,command=self.searchdata).grid(row=0,column=3,padx=10,pady=10)
              showallbtn=Button(detail_frame,text="ShowAll",width=10,command=self.fetchdata).grid(row=0,column=4,padx=10,pady=10)
        
              table_frame=Frame(detail_frame)
              table_frame.place(x=10,y=70,width=760,height=500)
          
              scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
              scroll_y=Scrollbar(table_frame,orient=VERTICAL)
         
              self.student_table=ttk.Treeview(table_frame,columns=("Email","Leavetype","FromDate","ToDate","status","ApplyLeaveDate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
              scroll_x.pack(side=BOTTOM,fill=X)
              scroll_y.pack(side=RIGHT,fill=Y)
              scroll_x.config(command=self.student_table.xview)
              scroll_y.config(command=self.student_table.yview)
              self.student_table.heading("Email",text="Email")
              self.student_table.heading("Leavetype",text="Leavetype")
              self.student_table.heading("FromDate",text="FromDate")
              self.student_table.heading("ToDate",text="ToDate")
              self.student_table.heading("status",text="status")
              self.student_table.heading("ApplyLeaveDate",text="ApplyLeaveDate")
              self.student_table["show"]="headings"
              self.student_table.column("Email",width=150)
              self.student_table.column("Leavetype",width=150)
              self.student_table.column("FromDate",width=150)
              self.student_table.column("ToDate",width=150)
              self.student_table.column("status",width=150)
              self.student_table.column("ApplyLeaveDate",width=150)
            
       
              
        
              self.student_table.pack(fill=BOTH,expand=1)
              self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
              self.fetchdata()

        def add_student(self):
            if self.rollno_var.get()=="" or self.email_var.get()=="":
                    messagebox.showerror("Error","All Fields are Required")
            else:        
                 conn=pymysql.connect(host="localhost",user="root",password="",database="registration")#self.adminstatus_var.get()
                 cur=conn.cursor()
                 cur.execute("INSERT INTO leaveaction(Email,Leavetype,FromDate,ToDate,status,ApproveLeaveDate) VALUES ('%s','%s','%s','%s','%s','%s')" % (self.rollno_var.get(),self.email_var.get(),self.fromdate_var.get(),self.todate_var.get(),self.adminstatus_var.get(),self.time1)) 
                 conn.commit()
                 self.fetchdata()
                 self.clear()
                 conn.close()
                 messagebox.showinfo("Success","Record has been inserted")
                 
        def fetchdata(self):
            conn=pymysql.connect(host="localhost",user="root",password="",database="registration")
            cur=conn.cursor()
            cur.execute("SELECT Email,Leavetype,FromDate,ToDate,status,ApplyLeaveDate FROM leaveform") 
            rows=cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert("",END,values=row)
                conn.commit()
                conn.close()
        def clear(self):
            self.rollno_var.set("")
            self.email_var.set("")
            self.fromdate_var.set("")
            self.todate_var.set("")
            self.adminstatus_var.set("")
        def get_cursor(self,ev):
            cursor_row=self.student_table.focus()
            contents=self.student_table.item(cursor_row)
            row=contents["values"]
            self.rollno_var.set(row[0])
            self.email_var.set(row[1])
            self.fromdate_var.set(row[2])
            self.todate_var.set(row[3])
            self.adminstatus_var.set(row[4])
            self.time1
            
        def update_data(self):
            conn=pymysql.connect(host="localhost",user="root",password="",database="registration")
            cur=conn.cursor()
            cur.execute("""UPDATE leaveform SET  status=%s where Email=%s""",(self.adminstatus_var.get(),self.rollno_var.get()))   
            conn.commit()

           # cur.execute("""UPDATE leaveaction SET  status=%s where Email=%s""",(self.email_var.get(),self.fromdate_var.get(),self.todate_var.get(),self.status_var.get(),self.rollno_var.get()))   
          
            self.fetchdata()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record has been Updated")
        def delete_data(self):
            conn=pymysql.connect(host="localhost",user="root",password="",database="registration")
            cur=conn.cursor()
            cur.execute("DELETE  FROM leaveform where Email=%s",self.rollno_var.get()) 
        
            conn.commit()
            conn.close()
            self.fetchdata()
            self.clear()
        def searchdata(self):
            conn=pymysql.connect(host="localhost",user="root",password="",database="registration")
            cur=conn.cursor()
            cur.execute("SELECT * FROM leaveform WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.searchall.get())+"%'") 
            rows=cur.fetchall()
            if len(rows)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                        self.student_table.insert("",END,values=row)
                conn.commit()
            conn.close()
   
        
        
       

            
                
 



class studentlogin(): 
    def __init__(self):
        global win
     #   win.withdraw()
         
        global my1
        top1=Toplevel()
        top1.title("Student Login")
        my1=ImageTk.PhotoImage(file="image/lapi4.jpg")   
        myl=Label(top1,image=my1).pack()
       
        frame_login=Frame(top1)
        frame_login.place(x=150,y=150,height=340,width=500)
        title=Label(frame_login,text="Login Here",font=("Impact",35,"bold")).place(x=90,y=30)
        desc=Label(frame_login,text="Student Login",font=("goudy old style",15,"bold")).place(x=90,y=100)
       #-----------username
  
        lbl_user=Label(frame_login,text="Username",font=("goudy old style",15,"bold")).place(x=90,y=140)
        self.txt_user=Entry(frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
      #---------------------password  
      
        lbl_pass=Label(frame_login,text="Password",font=("goudy old style",15,"bold")).place(x=90,y=210)
        self.txt_pass=Entry(frame_login,font=("times new roman",15),show="*")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
    #forget=Button(frame_login,text="Forget password?",font=("times new roman",12)).place(x=90,y=280) 
        login_btn=Button(top1,text="Sign In",command=self.login,compound=LEFT).place(x=300,y=470,width=180,height=40)
    def login(self):
        global userID
        try:
            connection=pymysql.connect(host='localhost',user='root',password="",db='registration')
        except:  
             print("you are not connected to the server(localhost)")
        else:       
            print("connected successfully")
       # print("enter ur email and password")
        Email=self.txt_user.get()
        Password=self.txt_pass.get()
        #cur=connection.cursor()
        query="SELECT Email,Password FROM reg_info"
        cur=connection.cursor()
        cur.execute(query)
        for (email,pas) in cur:
              if Email==email and Password==pas:
                  login=True
                  break
              else:
                login=False
        userID= (Email.split('@') [0])
        if login==True:
             print("logged in successfully as ",userID)
             newWindow()
            
        elif login==False:
            messagebox.showerror("Error","username and passowrd is wrong")


userID='urEmailDomain'
home='urhomewindow'

def newWindow():         
    global userID,home,bg1
    win.withdraw()
    home=Toplevel()
    home.title("Student Leave Project")
    home.geometry("1350x700+0+0")
    home.config(bg="white")
    bg1=ImageTk.PhotoImage(file="image/lapi4.jpg")
    bg1label=Label(home,image=bg1).pack()


    frame1=Frame(home)
    frame1.place(x=480,y=100,width=700,height=500)
        #------------------------------------------row1
    
    curpass=Label(frame1,text="Current Password",font=("times new roman",15,"bold")).place(x=50,y=100)
    txt_curpass=Entry(frame1,font=("times new roman",15))
    txt_curpass.place(x=50,y=130,width=250)
        
        
    newpass=Label(frame1,text="New Password",font=("times new roman",15,"bold")).place(x=370,y=100)
    txt_newpass=Entry(frame1,font=("times new roman",15))
    txt_newpass.place(x=370,y=130,width=250)

    conpass=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold")).place(x=50,y=230)
    txt_conpass=Entry(frame1,font=("times new roman",15))
    txt_conpass.place(x=250,y=230,width=250)
        #--------------button 
    btn_chg=Button(frame1,text="Change",cursor="hand2").place(x=250,y=400)

  

        #-----------------side buttons
    btn_reg1=Button(home,text="My Profile",cursor="hand2").place(x=40,y=200,width=200)
    btn_reg2=Button(home,text=" ApplyLeave",cursor="hand2",command=ApplyLeave,compound=LEFT).place(x=40,y=300,width=200)
    

    btn_reg3=Button(home,text="Leave Status",cursor="hand2",command=LeaveStatus).place(x=40,y=400,width=200)
         
    something=Label(home,text="You are logged in Successfully\n{}".format(userID))
    something.place(x=80,y=20)
    logout=Button(home,text='logOut',command=logOut,compound=LEFT)
    logout.place(x=1100,y=20)
class ApplyLeave():
    def __init__(self):
         #home1='urwindow'
         date='datevariable'
         global userID,home1,bg2
         #global time1
         
         home.withdraw()
         
    
         home1=Toplevel()
         home1.title("Student Leave Project")
         home1.geometry("1350x700+0+0")

         
         bg2=ImageTk.PhotoImage(file="image/lapi4.jpg")
         bg2label=Label(home1,image=bg2).pack()
         frame1=Frame(home1)
         frame1.place(x=480,y=100,width=700,height=500)
         title=Label(frame1,text="APPLY FOR LEAVE ",font=("times new roman",20,"bold")).place(x=50,y=30)
        #------------------------------------------row1
         type=Label(frame1,text="Leave Type:",font=("times new roman",15,"bold")).place(x=50,y=170)
         self.type=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
         self.type['values']=("select Leave type","Casual Leave","Medical Leave","Restrict Holiday")
         self.type.place(x=230,y=170,width=250)
         self.type.current(0)
         
         email=Label(frame1,text="Student Email:",font=("times new roman",15,"bold")).place(x=50,y=110)
         self.txt_email=Entry(frame1,font=("times new roman",15))
         self.txt_email.place(x=230,y=110)
      
         fromdate=Label(frame1,text="From Date:",font=("times new roman",15,"bold")).place(x=50,y=220)
         self.cal=Entry(frame1,font=("times new roman",15))
         self.cal.place(x=160,y=220)
       
         todate=Label(frame1,text="To Date:",font=("times new roman",15,"bold")).place(x=380,y=220)
         self.cal2=Entry(frame1,font=("times new roman",15))
         self.cal2.place(x=470,y=220)
         
         desc=Label(frame1,text="Description:",font=("times new roman",15,"bold")).place(x=50,y=280)
         self.txt_desc=Entry(frame1,font=("times new roman",15))
         self.txt_desc.place(x=230,y=280,width=250,height=100)
       
         login_btn=Button(frame1,text="Apply",command=self.register_data,compound=LEFT).place(x=260,y=420,width=180,height=40)
         logout=Button(home1,text='logOut',command=self.logOut1,compound=LEFT)
         logout.place(x=1100,y=20)
         
         x=datetime.datetime.now()
         self.time2=x.strftime("%m-%d-%y %H:%M:%S")
         time3=Label(home1,text="current leave apply time:\n{}".format(self.time2))
         time3.place(x=30,y=10)
         
         something1=Label(home1,text="You are logged in Successfully\n{}".format(userID))
         something1.place(x=80,y=60)
        
    def clear(self):
         self.txt_email.delete(0,END),
         self.type.current(0),  
         self.cal.delete(0,END),
         self.cal2.delete(0,END),
         self.txt_desc.delete(0,END)
  
    def register_data(self):
         con=pymysql.connect(host="localhost",user="root",password="",database="registration")
         cur=con.cursor()
         if self.type.get()=="" or self.cal.get()=="" or self.cal2.get()=="" or self.txt_desc.get()=="":
                           messagebox.showerror("error","all fields are required")
    

         else: 

             try:
                  con=pymysql.connect(host="localhost",user="root",password="",database="registration")
                  cur=con.cursor()
                 
                
                  cur.execute("INSERT INTO leaveform(Email,Leavetype,FromDate,ToDate,Description,status,ApplyLeaveDate) VALUES ('%s','%s','%s','%s','%s','%s','%s')" % (self.txt_email.get(),self.type.get(),self.cal.get(),self.cal2.get(),self.txt_desc.get(),"Pending",self.time2))                      

                  con.commit()
                  con.close()
                  messagebox.showinfo("Success","Leave Applied Sucessfully...")
                  self.clear()
                
             except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}")
    def logOut1(self):
        global home1
        home1.withdraw()
        print("logged out successfulyy")
def LeaveStatus():
   
       connection=pymysql.connect(host='localhost',user='root',password="",db='registration')
       cur=connection.cursor()   
       

            


       sql2="SELECT * FROM leaveform"
       cur.execute(sql2)
       rows=cur.fetchall()
       
       win=Tk()



       frm=Frame(win)
       frm.pack(padx=0,pady=0,anchor="nw")
       tv=Treeview(frm,columns=(1,2,3,4,5,6,7),show="headings")
       
       tv.pack(side=TOP,pady=5)

     
       tv.heading(1,text="Email")
       tv.column(1,minwidth=0,width=180, stretch=NO)
       tv.heading(2,text="LeaveType")
       tv.column(2,minwidth=0,width=181, stretch=NO)
       tv.heading(3,text="FromDate")
       tv.column(3,minwidth=0,width=182, stretch=NO)
       tv.heading(4,text="ToDate")
       tv.column(4,minwidth=0,width=183, stretch=NO)
       tv.heading(5,text="Description")
       tv.column(5,minwidth=0,width=195, stretch=YES)
       tv.heading(6,text="Status")
       tv.column(6,minwidth=0,width=201, stretch=NO)
       tv.heading(7,text="ActionTakenTime")
       tv.column(7,minwidth=0,width=205, stretch=NO)
       tv.pack(side=LEFT,padx=10,pady=5)
       for i in rows:
           tv.insert('','end',values=i)
    










   
         
def logOut():
    global home
  #  home.withdraw()
    print("logged out successfulyy")


    

mainloop()
