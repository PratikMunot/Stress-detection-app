from tkinter import *
from functools import partial
import sqlite3

def raise_frame(frame):
    frame.tkraise()

main_win = Tk()
main_win.geometry('700x400')
main_win.title("Twitter Sentiment Analysis")

# Frames ==================================================
third_frame = Frame(main_win)  # login frame
third_frame.place(x=0, y=0, width=700, height=400)

second_frame = Frame(main_win)  # Registration frame
second_frame.place(x=0, y=0, width=700, height=400)

first_frame = Frame(main_win)
first_frame.place(x=0, y=0, width=700, height=400)

# raise_frame(first_frame)

#================================================================
def mainframe():
    root=Tk()
    root.geometry("300x300")
    btn=Button(root,text="Gather Tweets",command=gather_tweets)
    btn.place(x=20,y=20)
    btn = Button(root, text="Display Tweets", command=display)
    btn.place(x=20, y=50)
    root.mainloop()
from tkinter import *
def Twitter():
    from tkinter.font import Font
    import  tkinter.messagebox
    import os
    # main_win.destroy()
    root = Tk()
    root.geometry("700x390")
    first = Frame(root)
    first.place(x=0, y=0, width=700, height=390)
    myfont = Font(size=13, family="Calibri", weight="bold", slant="italic")
    background = PhotoImage(file="background.png")

    # label = Label(root, image=photo)
    label_01 = Label(first, image=background,text="Welcome to Twint\n Please Enter your Twitter username")
    label_01.place(x=0, y=0)
    var1 = StringVar()
    var1.set("UserID")
    var2 = StringVar()
    var2.set("Email_ID")
    var3 = StringVar()
    var3.set("Email_ID")
    var4 = StringVar()
    var4.set("Email_ID")

    frame = LabelFrame(root, bg='white',text="Enter your Twitter Username", padx=10, pady=10,font=myfont)
    # entry = Entry(frame)
    # entry.pack()
    # frame.pack()
    entry1 = Entry(frame, bd=1, width=40,textvariable=var1)
    entry1.pack()
    frame.place(x=240,y=40)

    frame2 = LabelFrame(root, bg='white', text="Enter your Friends Email-id", padx=10, pady=10, font=myfont)
    entry2 = Entry(frame2, bd=1, width=40,textvariable=var2)
    # entry2.place(x=240, y=130)
    entry3 = Entry(frame2, bd=1, width=40,textvariable=var3)
    # entry3.place(x=240,y=180)
    entry4 = Entry(frame2, bd=1, width=40,textvariable=var4)
    # entry4.place(x=240, y=230)
    entry2.pack()
    l1=Label(frame2,text="").pack()
    entry3.pack()
    l1 = Label(frame2, text="").pack()
    entry4.pack()
    # l1 = Label(frame2, text=" ").pack()
    frame2.place(x=240,y=150)



    def submit():
        if(var1.get()=="UserID" or var1.get()==""):
            tkinter.messagebox.showerror("Error", "UserID cannot be empty\nPlease Enter valid UserID")
        else:
            with open("name.txt","w") as fp:
                fp.write(var1.get())
            with open("email.txt", "w") as fp:
                fp.write(var2.get()+"\n")
                fp.write(var3.get()+"\n")
                fp.write(var4.get()+"\n")

            if("name.txt" in os.listdir()):
                answer = tkinter.messagebox.askquestion('Done', "Do you want to Analyze the tweets")
                if answer == 'yes':
                    mainframe()
                    # print("Nice to meet a new specie\n Well i am a computer")
                else:
                    root.quit()
    Button(root, text="Submit", font=('Calibri', 12), bd=1, width=21, bg='blue',
           fg='white',command=submit).place(x=275, y=320)
    root.mainloop()






# Home frame ===================================================
# scanBtn_img = PhotoImage(file="btn.png")
home = PhotoImage(file="twitsenti2.png")

#label = Label(root, image=photo)
label_0 = Label(first_frame, image=home)
label_0.place(x=0, y=0)

Button(first_frame, text='Registration',borderwidth=0,font=('Calibri', 12), width=20, bg='blue',
       fg='white', command=lambda: raise_frame(second_frame)).place(x=350, y=365)
Button(first_frame, text='Login',borderwidth=0,font=('Calibri', 12), width=18, bg='blue',
       fg='white', command=lambda: raise_frame(third_frame)).place(x=540, y=365)





# Registration frame ==================================================================
def register():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("create table if not exists Admin(id integer primary key, name text, password text)")

    data = list(cur.execute("select * from Admin"))
    print(data)
    if(len(data)>0):
        usernames = [i[1] for i in data]
        if uname_entry.get() in usernames:
            print("User already exists")
        else:
            if len(data) == 0:
                id = 100
            else:
                id = data[-1][0]
                # print(data)
            id += 1

            print(uname_entry.get(), pass_entry.get())
            # print(id)
            # cur.execute("insert into Admin values("+id,'" + txtuname.get() + "','" + txtPass.get() + "')")
            cur.execute("insert into Admin values(?,?,?)", (id, uname_entry.get(), pass_entry.get()))
            con.commit()

    else:
        id = 100
        id += 1
        print(uname_entry.get(), pass_entry.get())
        # print(id)
        # cur.execute("insert into Admin values("+id,'" + txtuname.get() + "','" + txtPass.get() + "')")
        cur.execute("insert into Admin values(?,?,?)", (id, uname_entry.get(), pass_entry.get()))
        con.commit()





log = PhotoImage(file="login.png")
label_2 = Label(second_frame, image=log)
label_2.place(x=0, y=0)

mycolor = '#%02x%02x%02x' % (9,186,244)
reg_frame= LabelFrame(second_frame, text="Registration",width=40,bd=1, font=('Calibri', 14),padx=2,pady=5,bg=mycolor)

user_label = Label(reg_frame,text="Enter your Username",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
#food_label.place(x=100,y=265)
user_label.pack()
uname_entry = Entry(reg_frame,bd=1,width=20)
uname_entry.pack()

pass_label = Label(reg_frame,text="Enter your Password",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
#food_label.place(x=100,y=265)
pass_label.pack()
pass_entry = Entry(reg_frame,width=20,bd=1, show="*")
pass_entry.pack()

reg_frame.place(x=30,y=210)
Button(second_frame, text="Register",font=('Calibri', 12),bd=1, width=21, bg='brown', fg='white',
       command=register).place(x=32, y=360)
# label_8 = Label(second_frame, text="Welcome to page 2", width=20, font=("bold", 10))
# label_8.place(x=50, y=230)

Button(second_frame, text="Switch back to Home Page", width=20, bg='brown', fg='white',
       command=lambda: raise_frame(first_frame)).place(x=540, y=365)



# Login Frame===============================================================================

def login():
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    def check_user():
        name = user_entry.get()
        pwd = password.get()
        #cur.execute("insert into Admin values(101,'" + txtuname.get() + "','" + txtPass.get() + "')")
        #con.commit()
        row = cur.execute("select * from Admin")
        data = list(row)[:]
        #print(data)

        for items in data:
            if name == items[1] and pwd == items[2]:
                print("Access Granted")
                Twitter()


    check_user()

# log = PhotoImage(file="login.png")
label_3 = Label(third_frame, image=log)
label_3.place(x=0, y=0)
# label_8 = Label(second_frame, text="Welcome to page 2", width=20, font=("bold", 10))
# label_8.place(x=50, y=230)


log_frame= LabelFrame(third_frame, text="Login",width=40,bd=1, font=('Calibri', 14),padx=2,pady=5,bg=mycolor)

user= Label(log_frame,text="Username",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
#food_label.place(x=100,y=265)
user.pack()
user_entry = Entry(log_frame,bd=1,width=20)
user_entry.pack()

pass_label = Label(log_frame,text="Password",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
#food_label.place(x=100,y=265)
pass_label.pack()
password = Entry(log_frame,width=20,bd=1, show="*")
password.pack()

log_frame.place(x=30,y=210)
Button(third_frame, text="Login",font=('Calibri', 12),bd=1, width=21, bg='brown', fg='white',
       command=login).place(x=32, y=360)




Button(third_frame, text="Switch back to Home Page", width=20, bg='brown', fg='white',
       command=lambda: raise_frame(first_frame)).place(x=540, y=365)


main_win.mainloop()