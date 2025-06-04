from customtkinter import * 
from functionsofcode import *
from tkinter import filedialog
import os

app = CTk()
app.title("Student Companion App")
app.geometry("700x800")
app.rowconfigure(0,weight=1)
app.columnconfigure(0,weight=1)
list = [CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53"),CTkFrame(app,fg_color="#225E53")]
usert = ""

def show_popup(message):
    popup = CTkToplevel()
    popup.geometry("300x150")
    popup.title("")
    popup.configure(fg_color="#E8F5E9")
    
    label = CTkLabel(popup, text=message, text_color="green", font=("Arial", 16, "bold"))
    label.pack(pady=30)
    
    btn = CTkButton(popup, text="OK", command=popup.destroy)
    btn.pack()

def unpacking():
    for i in list:
        i.grid_forget()

def homepage():
    loginpage = list[0]
    loginpage.grid(row=0,column=0, sticky="nsew")
    WelText = CTkLabel(loginpage,text="STUDENT COMPANION APP", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    WelText.place(relx=0.5,rely=0.2,anchor="center", relwidth=0.5,relheight=0.4)
    Button1 = CTkButton(loginpage,text="New User",corner_radius=20, command=newuserpage, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    Button1.place(relx=0.2,rely=0.5, anchor="center", relwidth=0.2,relheight=0.1)
    Button2 = CTkButton(loginpage,text="Exsisting User",corner_radius=20, command=olduserpage, fg_color="#2C786C", hover_color="#22665B", text_color="white" )
    Button2.place(relx=0.8,rely=0.5, anchor="center", relwidth=0.2,relheight=0.1)

def newuserpage():
    unpacking()
    newuserpaget = list[1]
    newuserpaget.grid(row=0,column=0, sticky="nsew")
    Newuserlabel = CTkLabel(newuserpaget, text="Please Enter The Following Details To Proced", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    Newuserlabel.place(relx=0.5,rely=0.2,anchor="center", relwidth=0.5,relheight=0.4)
    useridlgo = CTkLabel(newuserpaget, text="USER ID: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    useridlgo.place(relx=0.3,rely=0.4,anchor="center", relwidth=0.2,relheight=0.1 )
    userpasslgo = CTkLabel(newuserpaget, text="PASSWORD: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    userpasslgo.place(relx=0.3,rely=0.5,anchor="center", relwidth=0.2,relheight=0.1 )
    usersublgo = CTkLabel(newuserpaget, text="SUBJECTS: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    usersublgo.place(relx=0.3,rely=0.6,anchor="center", relwidth=0.2,relheight=0.1 )
    newuserid = CTkEntry(newuserpaget)
    newuserid.place(relx=0.6,rely=0.4, anchor="center", relwidth=0.3,relheight=0.05)
    newuserpass = CTkEntry(newuserpaget)
    newuserpass.place(relx=0.6,rely=0.5, anchor="center", relwidth=0.3,relheight=0.05)
    newusersub = CTkEntry(newuserpaget, placeholder_text="ENTER SUBJECT NAME SEPERATE BY ','")
    newusersub.place(relx=0.6,rely=0.6, anchor="center", relwidth=0.3,relheight=0.05)
    def newuserlogin():
        userid = newuserid.get().strip()
        password = newuserpass.get().strip()
        subjects = (newusersub.get()).split(",")
        subejct = [i.strip() for i in subjects]
        for user in users:
            if user["Username"] == userid:
                show_popup("PLEASE SELECT ANOTHER USER ID")
                newuserpage()
            else:
                newuser(userid=userid,password=password,subjects=subejct)
                show_popup("SUCESSFULLY REGISTERED")
                olduserpage()
    sub = CTkButton(newuserpaget, text="SUBMIT", command=newuserlogin, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    sub.place(relx=0.5,rely=0.8, anchor="center", relwidth=0.2,relheight=0.1)
    # v = newuserid.get()
    # print(v)

def olduserpage():
    unpacking()
    newuserpaget = list[2]
    newuserpaget.grid(row=0,column=0, sticky="nsew")
    Newuserlabel = CTkLabel(newuserpaget, text="Please Enter The Following Details To Proced", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    Newuserlabel.place(relx=0.5,rely=0.2,anchor="center", relwidth=0.5,relheight=0.4)
    useridlgo = CTkLabel(newuserpaget, text="USER ID: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    useridlgo.place(relx=0.3,rely=0.4,anchor="center", relwidth=0.2,relheight=0.1 )
    userpasslgo = CTkLabel(newuserpaget, text="PASSWORD: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    userpasslgo.place(relx=0.3,rely=0.5,anchor="center", relwidth=0.2,relheight=0.1 )
    newuserid = CTkEntry(newuserpaget)
    newuserid.place(relx=0.6,rely=0.4, anchor="center", relwidth=0.3,relheight=0.05)
    newuserpass = CTkEntry(newuserpaget)
    newuserpass.place(relx=0.6,rely=0.5, anchor="center", relwidth=0.3,relheight=0.05)
    def homego():
        userid = newuserid.get().strip()
        password = newuserpass.get().strip()
        if loginuser(userid,password):
            global usert 
            usert = userid
            print(usert)
            home()
        else:
            olduserpage()
                    
    sub = CTkButton(newuserpaget, text="SUBMIT", command=homego, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    sub.place(relx=0.5,rely=0.8, anchor="center", relwidth=0.2,relheight=0.1)    

def home():
    unpacking()
    homepage = list[3]
    homepage.grid(row=0,column=0, sticky="nsew")
    Welcoming_Label = CTkLabel(homepage,text=f"Welcome {usert}", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    Tasktodo_Label = CTkLabel(homepage, text="What Will You Like To Do Today? ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    Welcoming_Label.place(relx=0.1,rely=0.2, anchor="center")
    Tasktodo_Label.place(relx=0.1,rely=0.3, anchor="center")
    Note = CTkButton(homepage,text="NOTES" , command=Notes, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    Plan = CTkButton(homepage, text="Plannar", command=Taskt, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    Task = CTkButton(homepage, text="TASKS", fg_color="#2C786C", hover_color="#22665B", text_color="white")
    Note.place(relx=0.25,rely=0.5, anchor="center", relwidth=0.2,relheight=0.1)
    Plan.place(relx=0.5,rely=0.5, anchor="center", relwidth=0.2,relheight=0.1)
    Task.place(relx=0.75,rely=0.5, anchor="center", relwidth=0.2,relheight=0.1)

def Notes():
    unpacking()
    Note = list[4]
    Note.grid(row=0,column=0, sticky="nsew")
    Notelabel = CTkLabel(Note, text="NOTES", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    Notelabel.place(relx=0.1,rely=0.1, anchor="center")
    HomeButton(Note)
    AddNote_Button = CTkButton(Note, text="ADD NOTES", command=AddNotesSys, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    AddNote_Button.place(relx=0.35,rely = 0.2, anchor="center", relwidth=0.1,relheight=0.1)
    Notesdiplay = CTkScrollableFrame(Note,fg_color = "#3D8B7C")
    Notesdiplay.place(relx=0.5, rely=0.6,anchor="center", relwidth=0.5, relheight=0.5)

    for user in users:
        if usert == user["Username"]:
            for note in user["Notes"]:
                path = note["File Location"]
                title = note["Title"]
                subjectname = note["Subject"]
                def open_file(a,path=path):
                     os.startfile(path)
                def deltrue(subjectname=subjectname,title=title):
                    deletenotes(userid=usert,subjectname=subjectname,title=title)
                    Notes()
                note_row = CTkFrame(Notesdiplay, fg_color="transparent")
                noteshow = CTkLabel(note_row, text=f"Title {note["Title"]} Subject {note["Subject"]}", cursor="hand2",  text_color="#2E2E2E", font=("Arial", 18, "bold"))
                noteshow.bind("<Button-1>", open_file )
                HomeButtom = CTkButton(note_row, text="🗑️", command=deltrue, fg_color="#2C786C", hover_color="#22665B", text_color="white")
                HomeButtom.pack(side="right")
                noteshow.pack(side="left")
                note_row.pack(fill="x", padx=10, pady=5)        

def AddNotesSys():
    unpacking()
    AddNotes = list[5]
    AddNotes.grid(row=0,column=0, sticky="nsew")
    title_Label = CTkLabel(AddNotes, text="PLEASE WRITE THE TITLE: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    title_Label.place(relx=0.3,rely=0.4)
    titlegetentry = CTkEntry(AddNotes, placeholder_text="TITLE")
    titlegetentry.place(relx=0.7,rely=0.4, anchor="center", relwidth=0.3,relheight=0.05)
    sub_label = CTkLabel(AddNotes, text="CHOOSE THE SUBJECT:",text_color="#2E2E2E", font=("Arial", 18, "bold"))
    sub_label.place(relx=0.3, rely=0.5)
    def choseone(choice):
        global subjectchosen
        subjectchosen = choice
        print("Subjectchosen")
    def filelocation(a):
        global location_of_notes
        location_of_notes = filedialog.askopenfilename(parent=AddNotes,title="Please Select Location Of Your Notes")
    def savenote():
        if location_of_notes:
            show_popup("SAVED SUCESSFULLY")
            addnotes(subjectname=subjectchosen, userid=usert, filelocation=location_of_notes, title=(titlegetentry.get().strip()))
            Notes()
        else:
            show_popup("PLEASE SET PROPER LOCATION")
            AddNotesSys()
    subjectslist = getsubject(usert)
    print(type(subjectslist))
    menu = CTkOptionMenu(AddNotes, values=subjectslist ,command=choseone, fg_color="#2C786C", 
    button_color="#22665B", 
    button_hover_color="#1B5449", 
    text_color="white",
    dropdown_fg_color="#3D8B7C", 
    dropdown_hover_color="#22665B")
    menu.set(subjectslist[0])
    subjectchosen = subjectslist[0]
    menu.place(relx=0.5,rely=0.5)
    fileloc = CTkLabel(AddNotes, text="Select Notes Location", cursor="hand2", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    fileloc.bind("<Button-1>", filelocation )
    fileloc.place(relx=0.4, rely=0.6)
    sub = CTkButton(AddNotes, text="SUBMIT", command=savenote, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    sub.place(relx=0.5,rely=0.8, anchor="center", relwidth=0.2,relheight=0.1)
    HomeButton(AddNotes)

def HomeButton(frame):
    HomeButtom = CTkButton(frame, text="🏡", command=home, fg_color="#2C786C", hover_color="#22665B", text_color="white")
    HomeButtom.place(relx=0.9,rely=0.1, anchor="center", relwidth=0.05, relheight=0.05)

def Taskt():
    unpacking()
    Taskshow = list[6]
    Taskshow.grid(row=0,column=0, sticky="nsew")
    Taskshow.rowconfigure(0,weight=1)
    Taskshow.columnconfigure(0,weight=1)
    Taskshow.columnconfigure(1,weight=1)
    Monthlytask = CTkScrollableFrame(Taskshow, fg_color = "#3D8B7C",width=300)
    Weeklytask = CTkScrollableFrame(Taskshow, fg_color = "#3D8B7C")
    Dailytask = CTkScrollableFrame(Taskshow, fg_color = "#3D8B7C")
    Monthlytask.place(relx=0,rely=0.1, relwidth=0.5 , relheight=0.9)
    Weeklytask.place(relx=0.5,rely=0.1, relwidth=0.5 , relheight=0.48)
    Dailytask.place(relx=0.5,rely=0.6, relwidth=0.5, relheight=0.4)
    AddTskbutton = CTkButton(Taskshow, text="ADD TASK", command=Tskadd, fg_color="#2C786C", hover_color="#22665B", text_color="white" )
    AddTskbutton.place(relx=0.3 , rely=0 , relwidth=0.2,relheight=0.1)
    for user in users:
        print("HEYYYY")
        if user["Username"] == usert:
            task = user["Tasks"]
            setdicton = {"Daily": Dailytask, "Monthly": Monthlytask, "Weekly": Weeklytask}
            for i in ["Daily", "Monthly", "Weekly"]:
                if task[i]:
                    mainlabel = CTkLabel(setdicton[i], text=f"Title         Subject        Due Date          STATUS")
                    mainlabel.pack()
                    for DailyTask in task[i]:
                        Lcable = CTkFrame(setdicton[i], fg_color="transparent")
                        Lcable.pack()
                
                    
                        def tskexecution(userid=usert, subject=DailyTask["subject"], title = DailyTask["Title"], duedate = DailyTask["Due Date"], category = i):
                            Task_updation(userid,subject,title,duedate,category)
                        
                        dailylabel = CTkLabel(Lcable, text=f"{DailyTask["Title"]}    {DailyTask["subject"]}      {DailyTask["Due Date"]}         ") 
                        check_var = StringVar(value=DailyTask["Status"])
                        configurechange = CTkCheckBox(Lcable, text="", command=tskexecution,variable=check_var ,onvalue="Complete",offvalue="Incomplete")
                        configurechange.pack(side="right")
                        dailylabel.pack(side="left")
                elif not task[i]:
                    mainlab = CTkLabel(setdicton[i],text="NO TASK FOUND")
                    mainlab.pack()

                    
    HomeButton(Taskshow)

def Tskadd():
    unpacking()
    Taskaddwork = list[7]
    Taskaddwork.grid(row=0,column=0 , sticky="nsew")
    HomeButton(Taskaddwork)
    title_Label = CTkLabel(Taskaddwork, text="PLEASE WRITE THE TITLE: ", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    title_Label.place(relx=0.3,rely=0.4)
    titlegetentry = CTkEntry(Taskaddwork, placeholder_text="TITLE")
    titlegetentry.place(relx=0.7,rely=0.4, anchor="center", relwidth=0.3,relheight=0.05)
    sub_label = CTkLabel(Taskaddwork, text="CHOOSE THE SUBJECT:", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    sub_label.place(relx=0.3, rely=0.5)
    tasktypelabel = CTkLabel(Taskaddwork, text="CHOOSE THE TYPE OF TASK:", text_color="#2E2E2E", font=("Arial", 18, "bold"))
    tasktypelabel.place(relx=0.3, rely=0.6)
    duedatelavel = CTkLabel(Taskaddwork, text="WRITE DUE DATE:",text_color="#2E2E2E", font=("Arial", 18, "bold"))
    duedatelavel.place(relx=0.3, rely=0.7)
    duedatentry = CTkEntry(Taskaddwork, placeholder_text="DD/MM/YYYY")
    duedatentry.place(relx=0.7,rely=0.7, anchor="center", relwidth=0.3,relheight=0.05)

    def choseone(choice):
        global subjectchosen 
        subjectchosen = choice
        print(subjectchosen) 
    def tsktype(choice):
        global tsk_typesk
        tsk_typesk = choice
        print(tsk_typesk)
    def tskset():
        titles = titlegetentry.get().strip()
        duedate = duedatentry.get().strip()
        addtask(category=tsk_typesk,userid=usert,subject=subjectchosen,title=titles,duedate=duedate)
        show_popup("TASK ADDED")
        Taskt()
    subjectslist = getsubject(usert)
    print(type(subjectslist))

    menu = CTkOptionMenu(Taskaddwork, values=subjectslist ,command=choseone, fg_color="#2C786C", 
    button_color="#22665B", 
    button_hover_color="#1B5449", 
    text_color="white",
    dropdown_fg_color="#3D8B7C", 
    dropdown_hover_color="#22665B")
    menu.set(subjectslist[0])
    subjectchosen = subjectslist[0]
    menu.place(relx=0.5,rely=0.5)
    menu2 = CTkOptionMenu(Taskaddwork, values=["Daily", "Monthly", "Weekly"], command=tsktype,  fg_color="#2C786C", 
    button_color="#22665B", 
    button_hover_color="#1B5449", 
    text_color="white",
    dropdown_fg_color="#3D8B7C", 
    dropdown_hover_color="#22665B")
    menu2.set("Daily")
    tsk_typesk = "Daily"
    menu2.place(relx=0.5,rely=0.6)
    subbu = CTkButton(Taskaddwork , text="SUBMIT",command=tskset,fg_color="#2C786C", hover_color="#22665B", text_color="white" )
    subbu.place(relx=0.5,rely=0.8, relwidth=0.2,relheight=0.1)

homepage()
app.mainloop()