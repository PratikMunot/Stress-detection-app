from tkinter import *

def gather_tweets():
    # with open("name.txt", "r") as fp:
    #     name = fp.read()
    #     print(name)
    import os
    os.system('Scripts\python getter.py')


def display():
    import pandas as pd
    root = Tk()
    text = Text(root,width=100,height=50,wrap=WORD,padx=10,pady=10,
                bd=1,selectbackground="light blue",font="Calibri")

    df1 = pd.read_csv("results.csv")
    # print(df1)
    # print(df1.shape)
    tweets=df1.tweet
    print(type(tweets[1]))
    # print(tweets)


    with open("user_tweets.txt","w") as fp:
        for tw in tweets:
            try:
                text.insert(INSERT, tw + "\n")
                fp.write(str(tw) + "\n")
            except:
                pass



    # text.insert(INSERT, "Hello Pratik\n")
    # text.insert(INSERT, "Hello Pratik\n")
    # myfont = Font(size=12, family="Times New Roman", weight="normal", slant="roman", underline=0)
    root.geometry("500x500")

    text.pack()

    def print_val():
        # in 1.0 , 1 indicates first line 0 indicates first character & END indicates last line
        print(text.get(1.0,END))
        #print(text.selection_get())
        #print(text.search(text.selection_get(),1.0,stopindex=END))
        # to clear text box on button click
        #text.delete(1.0,END)
    but = Button(root, text="print", command=print_val)
    but.pack()
    root.mainloop()

# display_Text()

def mainframe():
    root=Tk()
    root.geometry("300x300")
    btn=Button(root,text="Gather Tweets",command=gather_tweets)
    btn.place(x=20,y=20)
    btn = Button(root, text="Display Tweets", command=display)
    btn.place(x=20, y=50)
    root.mainloop()


# mainframe()
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

Twitter()