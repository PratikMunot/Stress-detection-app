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

import os,pickle
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
        print(sentence)
        lab = model.predict(cv.transform(sentence))  # testing sentence given as list elements
        print(lab)
        length = len(lab)
        # print(x_testp)
        print("Running loop")
        for i in range(length):
            # print("inside loop")
            if lab[i] == 0:
                print("negative")
                output.append("Negative")
            elif lab[i] == 4:
                print("positive")
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
tweets_list = ["I am feeling happy","I am feeling very sad ","She is so cheerful","we all are frustrated"]
SVM_classifier(tweets_list)
def display():
    pickle_in = open('NBC_results.pickle', 'rb')
    output = pickle.load(pickle_in)
    pickle_in.close()
    print(tweets_list)
    print(output)

display()