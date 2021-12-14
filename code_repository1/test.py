# import tkinter as tk
#
# LARGE_FONT = ("Verdana", 12)
#
#
# class SeaofBTCapp(tk.Tk):
#
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         container = tk.Frame(self)
#
#         container.pack(side="top", fill="both", expand=True)
#
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#
#         self.frames = {}
#
#         for F in (StartPage, PageOne, PageTwo):
#             frame = F(container, self)
#
#             self.frames[F] = frame
#
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame(StartPage)
#
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
#
#
# class StartPage(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button = tk.Button(self, text="Visit Page 1",
#                            command=lambda: controller.show_frame(PageOne))
#         button.pack()
#
#         button2 = tk.Button(self, text="Visit Page 2",
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#
# class PageOne(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Page Two",
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()
#
#
# class PageTwo(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
#
#         button1 = tk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = tk.Button(self, text="Page One",
#                             command=lambda: controller.show_frame(PageOne))
#         button2.pack()
#
#
# app = SeaofBTCapp()
# app.mainloop()


from tkinter import *
from functools import partial

def raise_frame(frame):
    frame.tkraise()

main_win = Tk()
main_win.geometry('500x500')
main_win.title("Registration Form")

second_frame = Frame(main_win)
second_frame.place(x=0, y=0, width=500, height=500)

first_frame = Frame(main_win)
first_frame.place(x=0, y=0, width=500, height=500)

# label_0 = Label(first_frame, text="Registration form", width=20, font=("bold", 20))
photo = PhotoImage(file="abc.png")
#label = Label(root, image=photo)
label_0 = Label(first_frame, image=photo, width=20, font=("bold", 20))

label_0.place(x=90, y=53)

label_1 = Label(first_frame, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(first_frame)
entry_1.place(x=240, y=130)

label_2 = Label(first_frame, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(first_frame)
entry_2.place(x=240, y=180)

label_3 = Label(first_frame, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(first_frame, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(first_frame, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(first_frame, text="country", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];
c = StringVar()
droplist = OptionMenu(first_frame, c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240, y=280)

label_4 = Label(first_frame, text="Programming", width=20, font=("bold", 10))
label_4.place(x=85, y=330)
var1 = IntVar()
Checkbutton(first_frame, text="java", variable=var1).place(x=235, y=330)
var2 = IntVar()
Checkbutton(first_frame, text="python", variable=var2).place(x=290, y=330)

Button(first_frame, text='Submit', width=20, bg='brown', fg='white', command=lambda: raise_frame(second_frame)).place(
    x=180, y=380)

label_8 = Label(second_frame, text="Welcome to page 2", width=20, font=("bold", 10))
label_8.place(x=70, y=230)

Button(second_frame, text="Switch back to page 1", width=20, bg='brown', fg='white',
       command=lambda: raise_frame(first_frame)).place(x=180, y=380)

main_win.mainloop()

'''
[4:12 pm, 10/04/2020] Sachin Sir: Can we have project meet with you all using zoom if you have sufficient work done to show.
[4:15 pm, 10/04/2020] Sachin Sir: Personal Meeting ID 548-751-1493
[4:15 pm, 10/04/2020] Sachin Sir: 9QYM5W
[4:16 pm, 10/04/2020] Sachin Sir: Date:11-04-2020 time 1.00pm
[4:16 pm, 10/04/2020] Sachin Sir: on Zoom
[4:17 pm, 10/04/2020] Sachin Sir: Sachin Jadhav is inviting you to a scheduled Zoom meeting.

Topic: Project Review 
Time: Apr 11, 2020 01:00 AM India

Join Zoom Meeting
https://us04web.zoom.us/j/5487511493?pwd=WXVQK241SFh2MWZJaVd6aGFZWk9Odz09

Meeting ID: 548 751 1493
Password: 9QYM5W
'''