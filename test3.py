# from tkinter import *
#
# root = Tk()
#
# def quitApp():
#     root.destroy()
#
# background_img = PhotoImage(file="twitsenti2.png")
# scanBtn_img = PhotoImage(file="btn.png")
#
# background = Label(root,bg='black', image = background_img).pack(side = RIGHT)
# quitButton = Button(bg='black', image=scanBtn_img, command = quitApp).pack(side = LEFT)
# backgroundimage = background_img # keep a reference!
#
# root.mainloop()

#
# import tkinter as tk
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.HelloButton = tk.Button(self.frame, text = 'Hello', width = 25, command = self.new_window,)
#         self.HelloButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()
#         self.new_window
#     def new_window(self):
#         self.new_window = tk.Toplevel(self.master)
#         self.app = Demo2(self.new_window)
#
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
from tkinter import *
import tkinter as tk
# def kill():
#     root.destroy()
#     window = tk.Tk()
#
#     window.mainloop()
#
#
#
#
# root = tk.Tk()
# # app = Demo1(root)
# btn = Button(root,text="Register",command=kill)
# btn.pack()
# root.mainloop()


def Twitter():
    # main_win.destroy()
    root = Tk()
    root.geometry("700x390")
    first = Frame(root)
    first.place(x=0, y=0, width=700, height=390)

    background = PhotoImage(file="background.png")

    # label = Label(root, image=photo)
    label_01 = Label(first, image=background)
    label_01.place(x=0, y=0)
    var1 = StringVar()
    var1.set("Enter data")
    var2 = StringVar()
    var2.set("Enter data")
    var3 = StringVar()
    var3.set("Enter data")
    var4 = StringVar()
    var4.set("Enter data")

    entry1 = Entry(root, bd=1, width=40,textvariable=var1)
    entry1.place(x=240,y=80)
    entry2 = Entry(root, bd=1, width=40,textvariable=var2)
    entry2.place(x=240, y=130)
    entry3 = Entry(root, bd=1, width=40,textvariable=var3)
    entry3.place(x=240,y=180)
    entry4 = Entry(root, bd=1, width=40,textvariable=var4)
    entry4.place(x=240, y=230)

    Button(root, text="Submit", font=('Calibri', 12), bd=1, width=21, bg='blue',
           fg='white').place(x=275, y=290)
    root.mainloop()

# Twitter()



def pratik_email():
    def send_email():
        import yagmail
        id = "python.9798@gmail.com"
        pas = "PYTHON@123python"

        client = email.get()
        try:
            # initializing the server connection
            yag = yagmail.SMTP(user=id, password=pas)
            # sending the email
            yag.send(to=client, subject='Testing.......',
                     contents='Hurray, it worked!', attachments=['login.png'])
            print("Email sent successfully")
        except:
            print("Error, email was not sent")

    window = tk.Tk()
    window.geometry('200x100')
    email = Entry(window, bd=1, width=25)
    email.place(x=20,y=10)

    Button(window, text="Submit",  bd=1, width=15, bg='white',
           fg='black',command=send_email).place(x=30,y=50)
    window.mainloop()


pratik_email()



def email4():
    import smtplib
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #server.login("python.9798@gmail.com", "PYTHON@123python")
    server.login("pmunot11@gmail.com",'Pratik@Gmail')
    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """
    server.sendmail(
        "pmunot11@gmail.com",
        "pmunot11@gmail.com",
        message)
    server.quit()

# email4()