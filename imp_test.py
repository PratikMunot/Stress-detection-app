import pickle
from tkinter import *
def final_report():
    pickle_in = open('tweets.pickle', 'rb')
    tweets = pickle.load(pickle_in)
    pickle_in.close()

    pickle_in = open('Final_results.pickle', 'rb')
    result = pickle.load(pickle_in)
    pickle_in.close()



    root = Tk()
    text2 = Text(root, width=100, height=50, wrap=WORD, padx=10, pady=10,
                bd=1, selectbackground="light blue", font="Calibri")

    # df1 = pd.read_csv("results.csv")
    # # print(df1)
    # # print(df1.shape)
    # tweets = df1.tweet
    # print(type(tweets[1]))
    # # print(tweets)

    # with open("user_tweets.txt", "w") as fp:
        # fp.seek(0)
    for twt,res in zip(tweets,result):
        try:
            # print(twt,res)
            data = twt+'\t\t\t\t\t\t'+str(res)+"\n"
            print(data)
            # text2.insert(INSERT, twt+'\t'+res+"\n")
            text2.insert(INSERT, data)


        except:
            pass

    # text.insert(INSERT, "Hello Pratik\n")
    # text.insert(INSERT, "Hello Pratik\n")
    # myfont = Font(size=12, family="Times New Roman", weight="normal", slant="roman", underline=0)
    root.geometry("500x500")

    text2.pack()

    # def print_val():
    #     # in 1.0 , 1 indicates first line 0 indicates first character & END indicates last line
    #     print(text2.get(1.0, END))
    #     # print(text.selection_get())
    #     # print(text.search(text.selection_get(),1.0,stopindex=END))
    #     # to clear text box on button click
    #     # text.delete(1.0,END)
    #
    # but = Button(root, text="print", command=print_val)
    # but.pack()
    root.mainloop()
# final_report()
def gather_tweets():
    pass
def display():
    pass
def analyze_tweets():
    pass
def display_results():
    pass
# def send_email():
#     pass





def mainframe():
    root=Tk()

    mycolor = '#%02x%02x%02x' % (9, 255, 154)
    root.configure(bg=mycolor)
    mycolor = '#%02x%02x%02x' % (189, 255, 174)
    hme_pg_frame = LabelFrame(root, text="Welcome to Twint", width=800,height=300, bd=3, font=('Calibri', 16), padx=2, pady=5,
                           bg=mycolor)

    root.geometry("480x480")
    btnf = LabelFrame(hme_pg_frame, text="Collect all the tweets from the user's official twitter account",
                      bd=2, font=('Calibri', 12), padx=2,width=450, height=70,pady=5, bg=mycolor)
    btn=Button(btnf,text=" Gather Tweets ",command=gather_tweets, fg='black',)
    btn.place(x=180,y=6)
    btnf.pack()
    btnf = LabelFrame(hme_pg_frame, text="Display all the user's tweets ",
                      bd=2, font=('Calibri', 12), padx=2, width=450, height=70, pady=5, bg=mycolor)
    btn = Button(btnf, text="Display Tweets ", command=display)
    btn.place(x=180, y=6)
    btnf.pack()
    btnf = LabelFrame(hme_pg_frame, text="Analyze the tweets to find their stress level",
                      bd=2, font=('Calibri', 12), padx=2, width=450, height=70, pady=5, bg=mycolor)
    btn = Button(btnf, text="Analyze Tweets", command=analyze_tweets)
    btn.place(x=180, y=6)
    btnf.pack()
    btnf = LabelFrame(hme_pg_frame, text="View the analysis report of the tweets ",
                      bd=2, font=('Calibri', 12), padx=2, width=450, height=70, pady=5, bg=mycolor)
    btn = Button(btnf, text="  View Results   ", command=display_results)
    btn.place(x=180, y=6)
    btnf.pack()
    btnf = LabelFrame(hme_pg_frame, text="Send Analysis report to your contact ids ",
                      bd=2, font=('Calibri', 12), padx=2, width=450, height=70, pady=5, bg=mycolor)
    btn = Button(btnf, text="  Send Report   ", command=send_email)
    btn.place(x=180, y=6)
    btnf.pack()
    btnf = LabelFrame(hme_pg_frame, text="Exit the Application ",
                      bd=2, font=('Calibri', 12), padx=2, width=450, height=70, pady=5, bg=mycolor)
    btn = Button(btnf, text="  Quit  ", width=11,command=lambda :root.destroy())
    btn.place(x=180, y=6)
    btnf.pack()
    #Label(text="Collect all the tweets from the user's official twitter account").place(x=100,y=55)
    # btn = Button(hme_pg_frame, text="Display Tweets", command=display)
    # btn.place(x=20, y=60)
    # btn = Button(hme_pg_frame, text="Analyze Tweets", command=analyze_tweets)
    # btn.place(x=20, y=100)
    # btn = Button(hme_pg_frame, text="View Results", command=display_results)
    # btn.place(x=20, y=140)
    # btn = Button(hme_pg_frame, text="Send Report", command=send_email)
    # btn.place(x=20, y=180)
    hme_pg_frame.place(x=10,y=10)
    root.mainloop()


# mainframe()

def send_email():
    import yagmail
    id = "python.9798@gmail.com"
    pas = "PYTHON@123python"

    with open('email.txt','r') as em:
        email_list=em.readlines()
    with open('name.txt','r') as em:
        userid=em.read()
    contents = "Your friend's @" + userid + " Stress Level Report"
    print(email_list)
    print(userid)
    print(contents)
    # email_list=['pmunot11@gmail.com\n','pratik.n.co9798@gmail.com\n']
    def run(client):
        try:
            # initializing the server connection
            yag = yagmail.SMTP(user=id, password=pas)
            # sending the email
            yag.send(to=client, subject='Stress Level Report',
                     contents="Your friend's @"+userid+" Stress Level Report", attachments=['user_final_reports.txt'])
            print("Email sent successfully")
        except:
            print("Error, email was not sent")
    for em in email_list:
        run(em.strip())


    # window = Tk()
    # window.geometry('200x100')
    # email = Entry(window, bd=1, width=25)
    # email.place(x=20,y=10)
    #
    # Button(window, text="Submit",  bd=1, width=15, bg='white',
    #        fg='black',command=send_email).place(x=30,y=50)
    # window.mainloop()


# send_email()


def Text_Blob_Model():
    from textblob import TextBlob
    from sklearn.model_selection import train_test_split
    import pandas as pd
    print("\n========== Text Blob Classifier Model loaded===============")
    fields = ['text', 'timestamp', 'polarity', 'subjectivity', 'sentiment']  # field names
    # writer.writerow(fields)  # writes field
    # data_python = ["I am feeling very happy today", "I am sad", "Good Night", "I am feeling very stress",
    #                "I am very frustrated", "Fuck off"]


    #-------------
    def get_label(analysis, threshold=0):
        if analysis.sentiment[0] > threshold:
            return 'Positive'
        elif analysis.sentiment[0] < threshold:
            return 'Negative'
        else:
            return 'Neutral'

    # output = []
    # for line in sentence:
    #     # performs the sentiment analysis and classifies it
    #     # print(line.get('text').encode('unicode_escape'))
    #     analysis = TextBlob(line)
    #     #print(line,analysis.sentiment, get_label(analysis))  # print the results
    #     result = get_label(analysis)
    #     output.append(result)
    # #print(output)
    # pickle_out = open('TB_results.pickle', 'wb')
    # pickle.dump(output, pickle_out)
    # pickle_out.close()



    def accur():
        # data = pd.read_csv('main5.csv')
        print("Testing Naive Bayes Classifier......")
        dataframe = pd.read_csv("main5.csv")
        # print(dataframe.describe())

        ##Step2: Split in to Training and Test Data
        x = dataframe["text"]
        y = dataframe["target"]

        # x_train, y_train = x[0:10000], y[0:10000]
        # y_test: Union[Union[ExtensionArray, None, Series, ndarray, object, DataFrame], Any]
        # x_test, y_test = x[10000:], y[10000:]

        #print(y)
        POSITIVE = 4
        NEGATIVE = 0
        #NEUTRAL = 2
        train, test = train_test_split(dataframe, test_size=0.99)
        test_pos = test[test['target'] == POSITIVE]['text']
        test_neg = test[test['target'] == NEGATIVE]['text']
        #print(test_neg)

        # def get_label(analysis, threshold=0):
        #     if analysis.sentiment[0] > threshold:
        #         return 'Positive'
        #     elif analysis.sentiment[0] < threshold:
        #         return 'Negative'
        #     else:
        #         return 'Neutral'

        # for line in test_neg:
        #     # performs the sentiment analysis and classifies it
        #     # print(line.get('text').encode('unicode_escape'))
        #     analysis = TextBlob(line)
        #     print(line,analysis.sentiment, get_label(analysis))  # print the results
        #     #print("  ")
        tp, tn, fp, fn = 0, 0, 0, 0
        for tweet in test_neg:
            analysis = TextBlob(tweet)
            res = get_label(analysis)
            if res == 'Negative':
                tn += 1
            else:
                fp += 1

        for tweet in test_pos:
            analysis = TextBlob(tweet)
            res = get_label(analysis)
            if res == 'Positive' or res=='Neutral':
                tp += 1
            else:
                fn += 1
        acc = (tp + tn) / (tp + tn + fp + fn)
        print('[[', tp, ' ', fp, ']\n', ' [', fn, ' ', tn, ']]')
        print("Text Blob model accuracy = ", acc)
    accur()


Text_Blob_Model()