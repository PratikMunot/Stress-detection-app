















#===================================================================================================
from sklearn.model_selection import train_test_split
import pickle
import nltk
import os
from textblob import TextBlob
from sklearn import metrics
from typing import List, Any, Union

import pandas as pd
from numpy.core._multiarray_umath import ndarray
from pandas import Series, DataFrame
from pandas.core.arrays import ExtensionArray
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix

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
        print("Naive Bayse Model Training started")
        training_set = nltk.classify.apply_features(extract_features, tweets, labeled=True)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        #print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, test)) * 100)

        print("NB model training compleated")


        NBC = open('NaiveBayesClassifier.pickle', 'wb')

        pickle.dump(classifier, NBC)  # here we are referencing the pickle module that we imported
        # the 2 parameters needed for dump() is - what to dump and where to dump
        NBC.close()
        if "NaiveBayesClassifier.pickle" in os.listdir():
            print("Naive Bayes Model saved successfully")
        else:
            print("Naive Bayes Classifier was not saved ")
    else:
        print("Naive Bayes Model loaded")
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

            print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, test)) * 100)

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

    def check():
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
        print("Naive Bayes Classifier model accuracy = ",acc*100)
    #check()
#============================================================
tweets_list = ["I am feeling happy","I am feeling very sad ","She is so cheerful","we all are frustrated"]
#Naive_Bayse(tweets_list)
def display_NBC(tweetlist):
    pickle_in = open('NBC_results.pickle', 'rb')
    output = pickle.load(pickle_in)
    pickle_in.close()
    print(tweetlist)
    print(output)

# display_NBC()
#============================================================




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
        def accur():
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



        SVMCM = open('SVM_Classifier.pickle', 'rb')
        model = pickle.load(SVMCM)
        print("SVM_Classifier Model loaded")
        accur()
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


        # for i in sentence:
        #     res = classifier.classify(extract_features(i.split()))
        #     if res == 4:
        #         print(i + " : " + "positive")
        #         output.append("Positive")
        #         # string += item + " : " + "positive\n"
        #     if res == 0:
        #         print(i + " : " + "negative")
        #         output.append("Negative")
        #         # string += item + " : " + "negative\n"
        # pickle_out = open('SVM_results.pickle', 'wb')
        # pickle.dump(output, pickle_out)
        # pickle_out.close()
     # Code to Predict the output label
    #dataframe = pd.read_csv("test.csv")#loading testing dataframe
    #print(dataframe.describe())
    # x1 = dataframe["text"]
    # y1 = dataframe["target"]
    # x_testp,y_testp = x1[0:],y1[0:]


    # print('This is predicted value')
    # #lab = model.predict(cv.transform(x_testp))#testing sentence given as csv file
    # lab= model.predict(cv.transform(["She is so cheerful" , " I am  feeling frustrated"]))#testing sentence given as list elements
    # # print(x_testp , lab)
    # length = len(lab)
    # #print(x_testp)
    # print("Running loop")
    # for i  in range (length):
    #    # print("inside loop")
    #     if lab[i] == 0 :
    #         print( "negative")
    #     elif lab[i] == 4 :
    #         print("positive")
       #code to save the model
# import pickle
# with open('model_pickle','wb') as f:
#      pickle.dump(model,f)
# with open('model_pickle','rb') as f:
#     mp = pickle.load(f)
#======================================================================

# tweets_list = ["I am feeling happy","I am feeling very sad ","She is so cheerful","we all are frustrated"]
#SVM_classifier(tweets_list)
def display_SVM(tweetlist):
    pickle_in = open('SVM_results.pickle', 'rb')
    output = pickle.load(pickle_in)
    pickle_in.close()
    print(tweetlist)
    print(output)

# display_SVM()

#=======================================================================


def Text_Blob_Model(sentence):
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

    #------------------------
    # def classify(analysis, threshold=0):
    #     if analysis.sentiment[0] > threshold:
    #         return "Positive"
    #     elif analysis.sentiment[0] < threshold:
    #         return "Negative"
    #     else:
    #         return "Neutral"

    # def accur():
    #     # data = pd.read_csv('main5.csv')
    #     print("Testing Naive Bayes Classifier......")
    #     dataframe = pd.read_csv("main5.csv")
    #     # print(dataframe.describe())
    #
    #     ##Step2: Split in to Training and Test Data
    #     x = dataframe["text"]
    #     y = dataframe["target"]
    #
    #     # x_train, y_train = x[0:10000], y[0:10000]
    #     # y_test: Union[Union[ExtensionArray, None, Series, ndarray, object, DataFrame], Any]
    #     # x_test, y_test = x[10000:], y[10000:]
    #
    #     #print(y)
    #     POSITIVE = 4
    #     NEGATIVE = 0
    #     #NEUTRAL = 2
    #     train, test = train_test_split(dataframe, test_size=0.2)
    #     test_pos = test[test['target'] == POSITIVE]['text']
    #     test_neg = test[test['target'] == NEGATIVE]['text']
    #     #print(test_neg)
    #
    #     def get_label(analysis, threshold=0):
    #         if analysis.sentiment[0] > threshold:
    #             return 'Positive'
    #         elif analysis.sentiment[0] < threshold:
    #             return 'Negative'
    #         else:
    #             return 'Neutral'
    #
    #     for line in test_neg:
    #         # performs the sentiment analysis and classifies it
    #         # print(line.get('text').encode('unicode_escape'))
    #         analysis = TextBlob(line)
    #         print(line,analysis.sentiment, get_label(analysis))  # print the results
    #     #     #print("  ")
    #     tp, tn, fp, fn = 0, 0, 0, 0
    #     # for tweet in test_neg:
    #     #     analysis = TextBlob(tweet)
    #     #     res = classify(analysis)
    #     #     if res == NEGATIVE:
    #     #         tn += 1
    #     #     else:
    #     #         fp += 1
    #     #
    #     # for tweet in test_pos:
    #     #     analysis = TextBlob(tweet)
    #     #     res = classify(analysis)
    #     #     if res == POSITIVE:
    #     #         tp += 1
    #     #     else:
    #     #         fn += 1
    #     # acc = (tp + tn) / (tp + tn + fp + fn)
    #     # print("Text Blob model accuracy = ", acc * 100)
    # accur()


#==================================================================


#Text_Blob_Model(tweets_list)

def display_TB(tweetlist):
    pickle_in = open('TB_results.pickle', 'rb')
    output = pickle.load(pickle_in)
    pickle_in.close()
    print(tweetlist)
    print(output)

#display_TB()

#=================================================================


def display_LSTM(tweetlist):
    pickle_in = open('lstm_results.pickle', 'rb')
    output = pickle.load(pickle_in)
    pickle_in.close()
    print(tweetlist)
    print(output)


tweets_list2=[
" was he close to suicide? poor boy ",
"i am happy",
"Yup it was fun! watching 21 ",
"it's not sad. kinda like finding 100 pesos in the pavement. which never happens to me ",
"is so sad for my APL friend",
"ok thats it you win.",
"Very sad about Iran.",
"congratulations to all",
"RIP, David Eddings.",
"really wanted Safina to pull out a win &amp; to lose like that...",
"pleased",
"oh thank you!",
"not a cool night.",
"My new car was stolen....by my mother who wanted to go pose at church.",
"im sick  'cough cough",
"CRY CRY ",
"Goodnight",
"i like you more",
"i m bored anyone wanna talk",
"i am sad",
"i m happy",
"i am not happy",
"i am unhappy",
"I am very frustrated",
"I am feeling very stressed",
"She is cheerful",
"I will not do suicide",
"I will do suicide",
"She wants to die"]







tweets_list4=["I am not happy","I am not frustrated","I am feeling very stressed","She is not cheerful",
              "I will not do suicide","I will do suicide","She wants to die"]
newlist=[]
def convert(tweets_list2):
    for item in tweets_list2:
        newlist.append([item])
    # print(newlist)
    pickle_out = open('tweets_list.pickle', 'wb')
    pickle.dump(newlist, pickle_out)
    pickle_out.close()

print("--------------------------------------")
convert(tweets_list2)
Naive_Bayse(tweets_list2)
SVM_classifier(tweets_list2)
Text_Blob_Model(tweets_list2)
# LSTM_algo(tweets_list2)
print("-------------------")
# display_NBC(tweets_list2)
# display_SVM(tweets_list2)
# display_TB(tweets_list2)
#display_LSTM(tweets_list2)

def master_display(tweets_list):
    pickle_in = open('NBC_results.pickle', 'rb')
    outputnb = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open('SVM_results.pickle', 'rb')
    outputsvm = pickle.load(pickle_in)
    pickle_in.close()
    pickle_in = open('TB_results.pickle', 'rb')
    outputtb = pickle.load(pickle_in)
    pickle_in.close()
    #print(os.listdir())
    # pickle_in = open('LSTM_resuts.pickle', 'rb')
    # outputlstm = pickle.load(pickle_in)
    # pickle_in.close()
    for i in range(len(tweets_list)):
        print("Tweet - ",tweets_list[i])
        print("Results - ")
        print("Naive Bayes Classifier - ",outputnb[i])
        print("SVM Classifier - ", outputsvm[i])
        print("Text Blob Classifier - ", outputtb[i])
        #print("LSTM Classifier - ", outputlstm[i])
        print("---------------------------------------")
master_display(tweets_list2)

