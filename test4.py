# def method11(sentence):
# pass

# ----------- LSTM --------------
import os,pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import Activation, LSTM, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix

# --------------------------------------------------------

#---------------------  Naive Bayes ---------------------
# from sklearn.model_selection import train_test_split
# import pickle
import nltk
# import os
# import pandas as pd

#---------------------------------------------------------


# ------------------------ SVM Model ------------------

from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from typing import List, Any, Union
from numpy.core._multiarray_umath import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray


#----------------------- Text Blob --------------------------------------

from textblob import TextBlob



# ---------------------- tkinter -----------------------------------------
from tkinter import *
from functools import partial
import sqlite3
from tkinter.font import Font
import  tkinter.messagebox
import os



from keras.utils import to_categorical
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pasta.augment import inline






















#===========================  LSTM MODEL =========================================
df = pd.read_csv('newtrainingdata.csv')
#print(df.head())
'''sns.countplot(df.target)
plt.xlabel('Label')
plt.title('Number of positive and negative reviews')'''
X = df.SentimentText
Y = df.Sentiment
le = LabelEncoder()
Y = le.fit_transform(Y)
Y = Y.reshape(-1, 1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.15)
max_words = 1000
max_len = 150
# print("stage1")
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(X_train)
sequences = tok.texts_to_sequences(X_train)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)

def RNN():
    inputs = Input(name='inputs' ,shape=[max_len])
    layer = Embedding(max_words,50,input_length=max_len)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.5)(layer)
    layer = Dense(1,name='out_layer')(layer)
    layer = Activation('sigmoid')(layer)
    model = Model(inputs=inputs, outputs=layer)
    return model

# print("stage2")
model = RNN()
# model.summary()
model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
# print("stage3")
allfiles=os.listdir()

if "LSTM_Classifier.pickle" not in allfiles:
    print("LSTM classifier Model Training started")
    model.fit(sequences_matrix, Y_train, batch_size=128, epochs=10, validation_split=0.2,
              callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
    # print("stage4")
    print("\nLSTM classifier model training compleated")

    LSTMCM = open('LSTM_Classifier.pickle', 'wb')

    pickle.dump(model, LSTMCM)  # here we are referencing the pickle module that we imported
    # the 2 parameters needed for dump() is - what to dump and where to dump
    LSTMCM.close()
    if "LSTM_Classifier.pickle" in os.listdir():
        print("\nLSTM classifier Model saved successfully")
    else:
        print("\nLSTM classifier was not saved ")
else:
    LSTMCM = open('LSTM_Classifier.pickle', 'rb')
    model = pickle.load(LSTMCM)


test_sequences = tok.texts_to_sequences(X_test)
test_sequences_matrix = sequence.pad_sequences(test_sequences, maxlen=max_len)
accr = model.evaluate(test_sequences_matrix, Y_test)
print("\n\n\n\n========== LSTM_Classifier Model loaded====================")
# print(accr)
def check(Testing_context):
    txts = tok.texts_to_sequences(Testing_context)
    txts = sequence.pad_sequences(txts, maxlen=max_len)
    preds = model.predict(txts)
    # print(Testing_context)
    # print(preds)
    if preds >= 0.50:
        return 'Positive'
    elif preds < 0.5:
        return 'Negative'


#
# for tweet in sentence:
#     check([tweet])
def accur_lstm():
    y_pred = []
    for i in X_test:
        y_pred.append(check([i]))
    print(accr)
    print(confusion_matrix(Y_test, y_pred))
    print(classification_report(Y_test, y_pred))
# accur_lstm()
'''
[0.785330722316741, 0.6308420300483704]

[[3210 3307]
 [2544 5938]]

              precision    recall  f1-score   support

           0       0.56      0.49      0.52      6517
           1       0.64      0.70      0.67      8482

    accuracy                           0.61     14999
   macro avg       0.60      0.60      0.60     14999
weighted avg       0.61      0.61      0.61     14999
'''

def lstm_(sentence):
    lstm_output = []
    for i in sentence:
        res=check([i])
        lstm_output.append(res)

    pickle_out = open('LSTM_results.pickle', 'wb')
    pickle.dump(lstm_output, pickle_out)
    pickle_out.close()


    # pickle_in = open('LSTM_results.pickle', 'rb')
    # output = pickle.load(pickle_in)
    # pickle_in.close()
    # # print(sentence)
    # print(output)
sentence=["I am happy","I am very sad"]


# uncomment from up above
# lstm_(sentence)
# accur_lstm()

# ======================================================================================


# from NB import *
# sentence=["I am happy","I am very sad"]
# Naive_Bayse(sentence)

#================================= Naive Bayes MODEL ===================================


def Naive_Bayse(sentence):

    from nltk.corpus import stopwords
    # from tkinter import *
    # from tkinter import messagebox
    # import smtplib, ssl
    # nltk.download('stopwords')

    # Function to extract words from tweets
    def get_words_in_tweets(tweets):
        wordList = []
        for (words, sentiment) in tweets:
            wordList.extend(words)
        return wordList

    # Function to extract words based on their frequency
    def get_word_features(wordList):
        wordList = nltk.FreqDist(wordList)
        features = wordList.keys()
        return features

    # Function to extract words based on document features
    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features


    POSITIVE = 4
    NEGATIVE = 0
    NEUTRAL = 2

    # Read the data
    data = pd.read_csv('main5.csv')

    # Split into train and test
    train, test = train_test_split(data, test_size=0.2)
    # train = data[:10000]
    # test = data[10000:]
    # Remove neutral tweets
    train = train[train.target != NEUTRAL]
    test_pos = test[test['target'] == POSITIVE]['text']
    test_neg = test[test['target'] == NEGATIVE]['text']

    tweets = []

    # Create set of stopwords using nltk
    stopwords = set(stopwords.words("english"))

    # Filter the tweets
    for index, row in train.iterrows():
        words_filtered = []
        for word in row.text.split():
            if not ((len(word) < 3) or
                    (word.startswith('@')) or
                    (word.startswith('#')) or
                    (word in stopwords) or
                    ('http' in word)):
                words_filtered.append(word)

        tweets.append((words_filtered, row.target))

    wordList = get_words_in_tweets(tweets)
    word_features = get_word_features(wordList)
    allfiles = os.listdir()
    if "NaiveBayesClassifier.pickle" not in allfiles:
        print("\nNaive Bayes Model Training started")
        training_set = nltk.classify.apply_features(extract_features, tweets, labeled=True)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        #print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, test)) * 100)

        print("\nNaive Bayes model training compleated")


        NBC = open('NaiveBayesClassifier.pickle', 'wb')

        pickle.dump(classifier, NBC)  # here we are referencing the pickle module that we imported
        # the 2 parameters needed for dump() is - what to dump and where to dump
        NBC.close()
        if "NaiveBayesClassifier.pickle" in os.listdir():
            print("\nNaive Bayes Model saved successfully")
        else:
            print("\nNaive Bayes Classifier was not saved ")
    else:
        print("\n========== Naive Bayes Classifier Model loaded ============")
        NBC = open('NaiveBayesClassifier.pickle', 'rb')
        classifier = pickle.load(NBC)
        output=[]
        for i in sentence:
            res = classifier.classify(extract_features(i.split()))
            if res == 4:
                #print(i + " : " + "positive")
                output.append("Positive")
                # string += item + " : " + "positive\n"
            if res == 0:
                #print(i + " : " + "negative")
                output.append("Negative")
                # string += item + " : " + "negative\n"
        pickle_out = open('NBC_results.pickle', 'wb')
        pickle.dump(output, pickle_out)
        pickle_out.close()

        #print(test)
        def accuracy():
            #  incorrect - dont call this function
            print("\nClassifier accuracy percent:", (nltk.classify.accuracy(classifier, test)) * 100)

            # X_train, X_test, y_train, y_test = train_test_split(data, data.target, test_size=0.2)
            # y_pred = classifier.predict(X_test)
            # print('accuracy by using Naive Bayes:', nltk.classify.util.accuracy(classifier, X_test))
            # print(confusion_matrix(y_test, y_pred))
            # print('Naive Bayes Classification Report', classification_report(y_test, y_pred))
            #
            # print(classification_report(y_test, y_pred))
            #
            # print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
        # accuracy()
    # def create():
    #     ans.append(tweet.get())

    def NB_accur():
    #     list2 = []
    #     # tweet2 = tweet.get()
    #     # res = classifier.classify(extract_features(tweet2.split()))
    #     # with open("list.txt",'r') as fp2:
    #     #     text = fp2.readlines()
    #     string = ""
    #     for item in ans:
    #         res = classifier.classify(extract_features(item.split()))
    #         if res == 4:
    #             print(item + " : " + "positive")
    #             string += item + " : " + "positive\n"
    #         if res == 0:
    #             print(item + " : " + "negative")
    #             string += item + " : " + "negative\n"
    #         list2.append(res)
    #     happy = list2.count(4)
    #     sad = list2.count(0)
    #     percentage = sad * 100 / (happy + sad)
        print("Testing Naive Bayes Classifier......")
        tp, tn, fp, fn = 0, 0, 0, 0
        for tweet in test_neg:
            res = classifier.classify(extract_features(tweet.split()))
            if res == NEGATIVE:
                tn += 1
            else:
                fp += 1

        for tweet in test_pos:
            res = classifier.classify(extract_features(tweet.split()))
            if res == POSITIVE:
                tp += 1
            else:
                fn += 1
        acc = (tp + tn) / (tp + tn + fp + fn)
        print("\nNaive Bayes Classifier model accuracy = ",acc)

        # [[1289   1]
        # [49   1317]]
        # Naive Bayes Classifier model accuracy =  97.32680722891565
        print('[[',tp,' ',fp,']\n',' [',fn,' ',tn,']]')

    # NB_accur()

# Naive_Bayse(sentence)

# ================================================================================


# ========================= SVM Model ==========================================


def SVM_classifier(sentence):
    ##Step1: Load Dataset
    dataframe = pd.read_csv("main5.csv")
    #print(dataframe.describe())

    ##Step2: Split in to Training and Test Data
    x = dataframe["text"]
    y = dataframe["target"]

    x_train,y_train = x[0:10000],y[0:10000]
    y_test: Union[Union[ExtensionArray, None, Series, ndarray, object, DataFrame], Any]
    x_test,y_test = x[10000:],y[10000:]

    ##Step3: Extract Features
    cv = CountVectorizer()
    features = cv.fit_transform(x_train)
    ##Step4: Build a model
    tuned_parameters = {'kernel': ['rbf','linear'], 'gamma': [1e-3, 1e-4],
                         'C': [1, 10, 100, 1000]}

    model = GridSearchCV(svm.SVC(), tuned_parameters)

    clf = svm.SVC(kernel='linear') # Linear Kernel
    allfiles = os.listdir()
    if "SVM_Classifier.pickle" not in allfiles:
        print("SVM classifier Model Training started")
        model.fit(features,y_train)
        print("SVM classifier model training compleated")

        SVMCM = open('SVM_Classifier.pickle', 'wb')

        pickle.dump(model, SVMCM)  # here we are referencing the pickle module that we imported
        # the 2 parameters needed for dump() is - what to dump and where to dump
        SVMCM.close()
        if "SVM_Classifier.pickle" in os.listdir():
            print("SVM classifier Model saved successfully")
        else:
            print("SVM classifier was not saved ")

    else:
        def SVM_accur():
            print("Classification report")
            #print(model.best_params_)
            #Step5: Test Accuracy
            print("Accuracy",model.score(cv.transform(x_test),y_test))
            #text = "Is that seriously how you spell his name?"
            #testin for accuracy
            y_pred =model.predict(cv.transform(x_test))
            #print(x_test)
            #print(x_test,  y_test  ,  y_pred  )
            print("predicting...")
            print(confusion_matrix(y_test, y_pred))
            print(classification_report(y_test, y_pred))
            '''Classification report
            Accuracy 0.9978645515558268
            predicting...
            [[1638    1]
             [   6 1633]]
                          precision    recall  f1-score   support
            
                       0       1.00      1.00      1.00      1639
                       4       1.00      1.00      1.00      1639
            
                accuracy                           1.00      3278
               macro avg       1.00      1.00      1.00      3278
            weighted avg       1.00      1.00      1.00      3278'''


        SVMCM = open('SVM_Classifier.pickle', 'rb')
        model = pickle.load(SVMCM)
        print("\n========== SVM Classifier Model loaded ====================")
        #SVM_accur()
        output = []
        #print(sentence)
        lab = model.predict(cv.transform(sentence))  # testing sentence given as list elements
        #print(lab)
        length = len(lab)
        # print(x_testp)

        #print("Running loop")
        for i in range(length):
            # print("inside loop")
            if lab[i] == 0:
                #print("negative")
                output.append("Negative")
            elif lab[i] == 4:
                #print("positive")
                output.append("Positive")
        pickle_out = open('SVM_results.pickle', 'wb')
        pickle.dump(output, pickle_out)
        pickle_out.close()
# SVM_classifier(sentence)

#===========================================================================



#============== Text Blob Model ==============================================


def Text_Blob_Model(sentence):
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

    output = []
    for line in sentence:
        # performs the sentiment analysis and classifies it
        # print(line.get('text').encode('unicode_escape'))
        analysis = TextBlob(line)
        #print(line,analysis.sentiment, get_label(analysis))  # print the results
        result = get_label(analysis)
        output.append(result)
    #print(output)
    pickle_out = open('TB_results.pickle', 'wb')
    pickle.dump(output, pickle_out)
    pickle_out.close()



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
    # accur()


# Text_Blob_Model(sentence)
# import pickle

def save_tweets():
    with open("user_tweets.txt",'r') as fp:
        data = fp.readlines()
        # print(data)
        data = [i.replace('\n','') for i in data ]
        # print(data)
        pickle_out = open('tweets.pickle', 'wb')
        pickle.dump(data, pickle_out)
        pickle_out.close()

def analyze_tweets():
    pickle_in = open('tweets.pickle', 'rb')
    tweets = pickle.load(pickle_in)
    pickle_in.close()
    lstm_(tweets)
    Naive_Bayse(tweets)
    SVM_classifier(tweets)
    Text_Blob_Model(tweets)

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
    fp=open('user_final_reports.txt','w')

    for twt,res in zip(tweets,result):
        try:
            # print(twt,res)
            data = twt+'\t\t\t\t\t\t'+str(res)+"\n"
            print(data,end='')
            fp.write(data)

            # text2.insert(INSERT, twt+'\t'+res+"\n")
            text2.insert(INSERT, data)

        except:
            pass
    fp.close()
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


def display_results():
    print("\n\n================= Analysis ================================")
    pickle_in = open('tweets.pickle', 'rb')
    tweets = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open('NBC_results.pickle', 'rb')
    outputnb = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open('SVM_results.pickle', 'rb')
    outputsvm = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open('TB_results.pickle', 'rb')
    outputtb = pickle.load(pickle_in)
    pickle_in.close()
    # print(os.listdir())
    pickle_in = open('LSTM_results.pickle', 'rb')
    outputlstm = pickle.load(pickle_in)
    pickle_in.close()
    final_results=[]
    for i in range(len(tweets)):
        print("Tweet - ", tweets[i])
        print("Results - ")
        print("Naive Bayes Classifier - ", outputnb[i])
        print("SVM Classifier - ", outputsvm[i])
        print("Text Blob Classifier - ", outputtb[i])
        print("LSTM Classifier - ", outputlstm[i])
        current=[outputnb[i],outputsvm[i],outputtb[i],outputlstm[i]]
        c = current.count('Negative')
        c=c / 4 * 100
        final_results.append(c)
        print("Stress Level Percentage -",c)
        print("---------------------------------------")
    pickle_out = open('Final_results.pickle', 'wb')
    pickle.dump(final_results, pickle_out)
    pickle_out.close()
    final_report()

# save_tweets()
# analyze_tweets()
# display_results()











# ------------------------------ User Interface -----------------------------------


def raise_frame(frame):
    frame.tkraise()

main_win = Tk()
main_win.geometry('700x392')
main_win.title("Twitter Sentiment Analysis")

# Frames ==================================================
tweeter_frame = Frame(main_win)  # Tweeter frame
tweeter_frame.place(x=0, y=0, width=700, height=400)

third_frame = Frame(main_win)  # login frame
third_frame.place(x=0, y=0, width=700, height=400)

second_frame = Frame(main_win)  # Registration frame
second_frame.place(x=0, y=0, width=700, height=400)

first_frame = Frame(main_win)
first_frame.place(x=0, y=0, width=700, height=400)

# raise_frame(first_frame)

#================================================================


# def pratik_email():
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


# pratik_email()

def gather_tweets():
    # with open("name.txt", "r") as fp:
    #     name = fp.read()
    #     print(name)

    import os
    if 'results.csv' in os.listdir():
        os.remove('results.csv')

    os.system('Scripts\python getter.py')
    save_tweets()

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
        # fp.seek(0)
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



# def mainframe():
#     root=Tk()
#     mycolor = '#%02x%02x%02x' % (9, 186, 244)
#     hme_pg_frame = LabelFrame(root, text="Welcome to Twint", width=300,height=300, bd=1, font=('Calibri', 14), padx=2, pady=5,
#                            bg=mycolor)
#
#     root.geometry("300x300")
#     btn=Button(hme_pg_frame,text="Gather Tweets",command=gather_tweets,bg='light blue', fg='black',)
#     btn.place(x=20,y=20)
#     btn = Button(hme_pg_frame, text="Display Tweets", command=display)
#     btn.place(x=20, y=60)
#     btn = Button(hme_pg_frame, text="Analyze Tweets", command=analyze_tweets)
#     btn.place(x=20, y=100)
#     btn = Button(hme_pg_frame, text="View Results", command=display_results)
#     btn.place(x=20, y=140)
#     btn = Button(hme_pg_frame, text="Send Report", command=send_email)
#     btn.place(x=20, y=180)
#     hme_pg_frame.place(x=0,y=0)
#     root.mainloop()


# Home frame   (1)  ===================================================
# scanBtn_img = PhotoImage(file="btn.png")
home = PhotoImage(file="twitsenti2.png")

#label = Label(root, image=photo)
label_0 = Label(first_frame, image=home)
label_0.place(x=0, y=0)

Button(first_frame, text='Registration',borderwidth=0,font=('Calibri', 12), width=20, bg='blue',
       fg='white', command=lambda: raise_frame(second_frame)).place(x=350, y=365)
Button(first_frame, text='Login',borderwidth=0,font=('Calibri', 12), width=18, bg='blue',
       fg='white', command=lambda: raise_frame(third_frame)).place(x=540, y=365)





# Registration frame   (2)  ==================================================================
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



# Login Frame   (3)  ===============================================================================

background = PhotoImage(file="background.png")
label_01 = Label(tweeter_frame, image=background,text="Welcome to Twint Please Enter your Twitter username")
label_01.place(x=0, y=0)
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
                #Twitter()
                raise_frame(tweeter_frame)

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





myfont = Font(size=13, family="Calibri", weight="bold", slant="italic")
background = PhotoImage(file="background.png")

# label = Label(root, image=photo)
label_01 = Label(tweeter_frame, image=background,text="Welcome to Twint\n Please Enter your Twitter username")
label_01.place(x=0, y=0)
var1 = StringVar()
var1.set("UserID")
var2 = StringVar()
var2.set("Email_ID")
var3 = StringVar()
var3.set("Email_ID")
var4 = StringVar()
var4.set("Email_ID")

frame = LabelFrame(tweeter_frame, bg='white',text="Enter your Twitter Username", padx=10, pady=10,font=myfont)
# entry = Entry(frame)
# entry.pack()
# frame.pack()
entry1 = Entry(frame, bd=1, width=40,textvariable=var1)
entry1.pack()
frame.place(x=240,y=40)

frame2 = LabelFrame(tweeter_frame, bg='white', text="Enter your Friends Email-id", padx=10, pady=10, font=myfont)
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
                main_win.quit()
Button(tweeter_frame, text="Submit", font=('Calibri', 12), bd=1, width=21, bg='blue',
       fg='white',command=submit).place(x=275, y=320)
# root.mainloop()






main_win.mainloop()


























#
# class Twitter:
#     def gather_tweets(self):
#         # with open("name.txt", "r") as fp:
#         #     name = fp.read()
#         #     print(name)
#         # import os
#         os.system('Scripts\python getter.py')
#
#     def display(self):
#         import pandas as pd
#         root = Tk()
#         text = Text(root, width=100, height=50, wrap=WORD, padx=10, pady=10,
#                     bd=1, selectbackground="light blue", font="Calibri")
#
#         df1 = pd.read_csv("results.csv")
#         # print(df1)
#         # print(df1.shape)
#         tweets = df1.tweet
#         print(type(tweets[1]))
#         # print(tweets)
#
#         with open("user_tweets.txt", "w") as fp:
#             for tw in tweets:
#                 try:
#                     text.insert(INSERT, tw + "\n")
#                     fp.write(str(tw) + "\n")
#                 except:
#                     pass
#
#         # text.insert(INSERT, "Hello Pratik\n")
#         # text.insert(INSERT, "Hello Pratik\n")
#         # myfont = Font(size=12, family="Times New Roman", weight="normal", slant="roman", underline=0)
#         root.geometry("500x500")
#
#         text.pack()
#
#         def print_val():
#             # in 1.0 , 1 indicates first line 0 indicates first character & END indicates last line
#             print(text.get(1.0, END))
#             # print(text.selection_get())
#             # print(text.search(text.selection_get(),1.0,stopindex=END))
#             # to clear text box on button click
#             # text.delete(1.0,END)
#
#         but = Button(root, text="print", command=print_val)
#         but.pack()
#         root.mainloop()
#
#     # display_Text()
#
#     def mainframe(self):
#         root = Tk()
#         root.geometry("300x300")
#         btn = Button(root, text="Gather Tweets", command=gather_tweets)
#         btn.place(x=20, y=20)
#         btn = Button(root, text="Display Tweets", command=display)
#         btn.place(x=20, y=50)
#         root.mainloop()
#
#     # mainframe()
#     def tweet(self):
#         from tkinter.font import Font
#         import tkinter.messagebox
#         import os
#         # main_win.destroy()
#         root = Tk()
#         root.geometry("700x390")
#         first = Frame(root)
#         first.place(x=0, y=0, width=700, height=390)
#         myfont = Font(size=13, family="Calibri", weight="bold", slant="italic")
#         background = PhotoImage(file="background.png")
#
#         # label = Label(root, image=photo)
#         label_01 = Label(first, image=background, text="Welcome to Twint\n Please Enter your Twitter username")
#         label_01.place(x=0, y=0)
#         var1 = StringVar()
#         var1.set("UserID")
#         var2 = StringVar()
#         var2.set("Email_ID")
#         var3 = StringVar()
#         var3.set("Email_ID")
#         var4 = StringVar()
#         var4.set("Email_ID")
#
#         frame = LabelFrame(root, bg='white', text="Enter your Twitter Username", padx=10, pady=10, font=myfont)
#         # entry = Entry(frame)
#         # entry.pack()
#         # frame.pack()
#         entry1 = Entry(frame, bd=1, width=40, textvariable=var1)
#         entry1.pack()
#         frame.place(x=240, y=40)
#
#         frame2 = LabelFrame(root, bg='white', text="Enter your Friends Email-id", padx=10, pady=10, font=myfont)
#         entry2 = Entry(frame2, bd=1, width=40, textvariable=var2)
#         # entry2.place(x=240, y=130)
#         entry3 = Entry(frame2, bd=1, width=40, textvariable=var3)
#         # entry3.place(x=240,y=180)
#         entry4 = Entry(frame2, bd=1, width=40, textvariable=var4)
#         # entry4.place(x=240, y=230)
#         entry2.pack()
#         l1 = Label(frame2, text="").pack()
#         entry3.pack()
#         l1 = Label(frame2, text="").pack()
#         entry4.pack()
#         # l1 = Label(frame2, text=" ").pack()
#         frame2.place(x=240, y=150)
#
#         def submit():
#             if (var1.get() == "UserID" or var1.get() == ""):
#                 tkinter.messagebox.showerror("Error", "UserID cannot be empty\nPlease Enter valid UserID")
#             else:
#                 with open("name.txt", "w") as fp:
#                     fp.write(var1.get())
#                 with open("email.txt", "w") as fp:
#                     fp.write(var2.get() + "\n")
#                     fp.write(var3.get() + "\n")
#                     fp.write(var4.get() + "\n")
#
#                 if ("name.txt" in os.listdir()):
#                     answer = tkinter.messagebox.askquestion('Done', "Do you want to Analyze the tweets")
#                     if answer == 'yes':
#                         mainframe()
#                         # print("Nice to meet a new specie\n Well i am a computer")
#                     else:
#                         root.quit()
#
#         Button(root, text="Submit", font=('Calibri', 12), bd=1, width=21, bg='blue',
#                fg='white', command=submit).place(x=275, y=320)
#         root.mainloop()
#
#     # Twitter()
#
#
#
#
#
#
# def raise_frame(frame):
#     frame.tkraise()
#
# def Twitter2():
#     from tkinter.font import Font
#     import  tkinter.messagebox
#     import os
#     # main_win.destroy()
#     root = Tk()
#     root.geometry("700x390")
#     first = Frame(root)
#     first.place(x=0, y=0, width=700, height=390)
#     myfont = Font(size=13, family="Calibri", weight="bold", slant="italic")
#     background_Twitter = PhotoImage(file="bg.png")
#
#     # home = PhotoImage(file="twitsenti2.png")
#     #
#     # # label = Label(root, image=photo)
#     # label_0 = Label(first_frame, image=home)
#
#     # label = Label(root, image=photo)
#
#     background = PhotoImage(file="background.png")
#
#     # label = Label(root, image=photo)
#     label_01 = Label(first, image=log, text="Welcome to Twint\n Please Enter your Twitter username")
#     label_01.place(x=0, y=0)
#     # var1 = StringVar()
#     # var1.set("UserID")
#     # var2 = StringVar()
#     # var2.set("Email_ID")
#     # var3 = StringVar()
#     # var3.set("Email_ID")
#     # var4 = StringVar()
#     # var4.set("Email_ID")
#     #
#     # frame = LabelFrame(root, bg='white',text="Enter your Twitter Username", padx=10, pady=10,font=myfont)
#     # # entry = Entry(frame)
#     # # entry.pack()
#     # # frame.pack()
#     # entry1 = Entry(frame, bd=1, width=40,textvariable=var1)
#     # entry1.pack()
#     # frame.place(x=240,y=40)
#     #
#     # frame2 = LabelFrame(root, bg='white', text="Enter your Friends Email-id", padx=10, pady=10, font=myfont)
#     # entry2 = Entry(frame2, bd=1, width=40,textvariable=var2)
#     # # entry2.place(x=240, y=130)
#     # entry3 = Entry(frame2, bd=1, width=40,textvariable=var3)
#     # # entry3.place(x=240,y=180)
#     # entry4 = Entry(frame2, bd=1, width=40,textvariable=var4)
#     # # entry4.place(x=240, y=230)
#     # entry2.pack()
#     # l1=Label(frame2,text="").pack()
#     # entry3.pack()
#     # l1 = Label(frame2, text="").pack()
#     # entry4.pack()
#     # # l1 = Label(frame2, text=" ").pack()
#     # frame2.place(x=240,y=150)
#     #
#     #
#     #
#     # def submit():
#     #     if(var1.get()=="UserID" or var1.get()==""):
#     #         tkinter.messagebox.showerror("Error", "UserID cannot be empty\nPlease Enter valid UserID")
#     #     else:
#     #         with open("name.txt","w") as fp:
#     #             fp.write(var1.get())
#     #         with open("email.txt", "w") as fp:
#     #             fp.write(var2.get()+"\n")
#     #             fp.write(var3.get()+"\n")
#     #             fp.write(var4.get()+"\n")
#     #
#     #         if("name.txt" in os.listdir()):
#     #             answer = tkinter.messagebox.askquestion('Done', "Do you want to Analyze the tweets")
#     #             if answer == 'yes':
#     #                 mainframe()
#     #                 # print("Nice to meet a new specie\n Well i am a computer")
#     #             else:
#     #                 root.quit()
#     # Button(root, text="Submit", font=('Calibri', 12), bd=1, width=21, bg='blue',
#     #        fg='white',command=submit).place(x=275, y=320)
#     root.mainloop()
#
# main_win = Tk()
# main_win.geometry('700x400')
# main_win.title("Twitter Sentiment Analysis")
#
# # Frames ==================================================
# third_frame = Frame(main_win)  # login frame
# third_frame.place(x=0, y=0, width=700, height=400)
#
# second_frame = Frame(main_win)  # Registration frame
# second_frame.place(x=0, y=0, width=700, height=400)
#
# first_frame = Frame(main_win)
# first_frame.place(x=0, y=0, width=700, height=400)
#
#
#
#
#
# # Home frame ===================================================
# # scanBtn_img = PhotoImage(file="btn.png")
# home = PhotoImage(file="twitsenti2.png")
#
# #label = Label(root, image=photo)
# label_0 = Label(first_frame, image=home)
# label_0.place(x=0, y=0)
#
# Button(first_frame, text='Registration',borderwidth=0,font=('Calibri', 12), width=20, bg='blue',
#        fg='white', command=lambda: raise_frame(second_frame)).place(x=350, y=365)
# Button(first_frame, text='Login',borderwidth=0,font=('Calibri', 12), width=18, bg='blue',
#        fg='white', command=lambda: raise_frame(third_frame)).place(x=540, y=365)
#
#
#
#
#
# # Registration frame ==================================================================
# def register():
#     con = sqlite3.connect('users.db')
#     cur = con.cursor()
#     cur.execute("create table if not exists Admin(id integer primary key, name text, password text)")
#
#     data = list(cur.execute("select * from Admin"))
#     print(data)
#     if(len(data)>0):
#         usernames = [i[1] for i in data]
#         if uname_entry.get() in usernames:
#             print("User already exists")
#         else:
#             if len(data) == 0:
#                 id = 100
#             else:
#                 id = data[-1][0]
#                 # print(data)
#             id += 1
#
#             print(uname_entry.get(), pass_entry.get())
#             # print(id)
#             # cur.execute("insert into Admin values("+id,'" + txtuname.get() + "','" + txtPass.get() + "')")
#             cur.execute("insert into Admin values(?,?,?)", (id, uname_entry.get(), pass_entry.get()))
#             con.commit()
#
#     else:
#         id = 100
#         id += 1
#         print(uname_entry.get(), pass_entry.get())
#         # print(id)
#         # cur.execute("insert into Admin values("+id,'" + txtuname.get() + "','" + txtPass.get() + "')")
#         cur.execute("insert into Admin values(?,?,?)", (id, uname_entry.get(), pass_entry.get()))
#         con.commit()
#
#
#
#
#
# log = PhotoImage(file="login.png")
# label_2 = Label(second_frame, image=log)
# label_2.place(x=0, y=0)
#
# mycolor = '#%02x%02x%02x' % (9,186,244)
# reg_frame= LabelFrame(second_frame, text="Registration",width=40,bd=1, font=('Calibri', 14),padx=2,pady=5,bg=mycolor)
#
# user_label = Label(reg_frame,text="Enter your Username",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
# #food_label.place(x=100,y=265)
# user_label.pack()
# uname_entry = Entry(reg_frame,bd=1,width=20)
# uname_entry.pack()
#
# pass_label = Label(reg_frame,text="Enter your Password",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
# #food_label.place(x=100,y=265)
# pass_label.pack()
# pass_entry = Entry(reg_frame,width=20,bd=1, show="*")
# pass_entry.pack()
#
# reg_frame.place(x=30,y=210)
# Button(second_frame, text="Register",font=('Calibri', 12),bd=1, width=21, bg='brown', fg='white',
#        command=register).place(x=32, y=360)
# # label_8 = Label(second_frame, text="Welcome to page 2", width=20, font=("bold", 10))
# # label_8.place(x=50, y=230)
#
# Button(second_frame, text="Switch back to Home Page", width=20, bg='brown', fg='white',
#        command=lambda: raise_frame(first_frame)).place(x=540, y=365)
#
#
#
# # Login Frame===============================================================================
#
# def login():
#     con = sqlite3.connect('users.db')
#     cur = con.cursor()
#
#     def check_user():
#         name = user_entry.get()
#         pwd = password.get()
#         #cur.execute("insert into Admin values(101,'" + txtuname.get() + "','" + txtPass.get() + "')")
#         #con.commit()
#         row = cur.execute("select * from Admin")
#         data = list(row)[:]
#         #print(data)
#
#         for items in data:
#             if name == items[1] and pwd == items[2]:
#                 print("Access Granted")
#                 Twitter2()
#                 # t=Twitter()
#                 # t.tweet()
#
#
#
#     check_user()
#
# # log = PhotoImage(file="login.png")
# label_3 = Label(third_frame, image=log)
# label_3.place(x=0, y=0)
# # label_8 = Label(second_frame, text="Welcome to page 2", width=20, font=("bold", 10))
# # label_8.place(x=50, y=230)
#
#
# log_frame= LabelFrame(third_frame, text="Login",width=40,bd=1, font=('Calibri', 14),padx=2,pady=5,bg=mycolor)
#
# user= Label(log_frame,text="Username",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
# #food_label.place(x=100,y=265)
# user.pack()
# user_entry = Entry(log_frame,bd=1,width=20)
# user_entry.pack()
#
# pass_label = Label(log_frame,text="Password",width=20,font=('Calibri', 12),padx=2,pady=5,bg=mycolor )
# #food_label.place(x=100,y=265)
# pass_label.pack()
# password = Entry(log_frame,width=20,bd=1, show="*")
# password.pack()
#
# log_frame.place(x=30,y=210)
# Button(third_frame, text="Login",font=('Calibri', 12),bd=1, width=21, bg='brown', fg='white',
#        command=login).place(x=32, y=360)
#
#
#
#
# Button(third_frame, text="Switch back to Home Page", width=20, bg='brown', fg='white',
#        command=lambda: raise_frame(first_frame)).place(x=540, y=365)
#
#
# main_win.mainloop()