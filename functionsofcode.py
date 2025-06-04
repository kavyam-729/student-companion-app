import json

with open("userdata.json", "r") as k:
    users = json.load(k)

def savefile():
    with open("userdata.json", "w") as f:
        json.dump(users, f, indent=4)
    print("File Saved!")

def newuser(userid, password, subjects):
    # users.append(users[0])
    new_user =      {
        "Username": "",
        "Password": "",
        "Subject": [
            "English",
            "Hindi",
            "Physics"
        ],
        "Notes": [] ,
        "Tasks": {
            "Daily": [],
            "Monthly": [],
            "Weekly": []
        }
    }
    new_user["Username"] = userid
    new_user["Password"] = password
    new_user["Subject"] = subjects
    print("Sucessfully Registered!")
    users.append(new_user)
    savefile()

def loginuser(userid, password):
    Userpresent = False
    for user in users:
        if user["Username"] == userid and user["Password"] == password:
            print(f"Welcome {user['Username']}")
            Userpresent = True
        else:
            continue
    if not Userpresent:
        print("User Is Not Present Please Register With Us!")
    return Userpresent

def getsubject(userid):
    for user in users:
        if user["Username"] == userid:
            print("YOO")
            SUBJECTs = user["Subject"]
            return SUBJECTs
                
def addsubject(subejctname, userid):
    for user in users:
        if user["Username"] == userid:
            if subejctname not in user["Subject"]:
                user["Subject"].append(subejctname)
                savefile()
            else:
                print("Subject already present")

def addnotes(subjectname,userid,filelocation,title):
    for user in users:
        if user["Username"] == userid:
            if subjectname in user["Subject"]:
                user["Notes"].append({
                    "Subject":subjectname,
                    "Title":title,
                    "File Location":filelocation
                 })
                savefile()
            else:
                print("Subject not present")
                return

def deletenotes(subjectname,userid,title):
    for user in users:
        if user["Username"]== userid:
            for notes in user["Notes"]:
                if notes["Subject"] == subjectname and notes["Title"] == title:
                    user["Notes"].remove(notes)
                    savefile()
                    print("Sucessfully removed")

                    return
            print("Note not found")
            return
    print("User not found")

def addtask(category,userid,subject,title,duedate):
    for user in users:
        if user["Username"] == userid:
            if subject in user["Subject"]:
                Task = user["Tasks"]
                Task[category].append({"Title":title,
                                    "subject":subject,
                                    "Due Date":duedate,
                                    "Status":"Incomplete"})
                user["Tasks"] = Task
                savefile()
                print("Sucessfully Added The Task")
                return
            print("Subject Not Found!")
            return
    print("User Not Found")
    return

def Task_updation(userid, subject, title, duedate, category):
    for user in users:
        if user["Username"] == userid:
            Task = user["Tasks"]
            for tasks in Task[category]:
                if tasks["subject"] == subject and tasks["Title"] == title and tasks["Due Date"] == duedate:
                    if tasks["Status"] == "Incomplete":
                        tasks["Status"] = "Complete"
                    elif tasks["Status"] == "Complete":
                        tasks["Status"] = "Incomplete" 
                    user["Tasks"] = Task
                    savefile()
                    return
            print("Task Not Found")
            return
    print("User Not Found")
    return

def deletetask(userid, subject, title, duedate, category):
    for user in users:
        if user["Username"] == userid:
            Task = user["Tasks"]
            for tasks in Task[category]:
                if tasks["Subject"] == subject and tasks["Title"] == title and tasks["Due Date"] == duedate:
                    Task[category].remove(tasks)
                    user["Tasks"] = Task
                    
                    savefile()
                    print("Task updated")
                    return
            print("Task Not found")
            return
    print("User not found return")
    return