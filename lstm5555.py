# # def method11():
# import matplotlib,os,pickle
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from pasta.augment import inline
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from keras.database import Model
# from keras.layers import Activation, LSTM, Dense, Dropout, Input, Embedding
# from keras.optimizers import RMSprop
# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing import sequence
# from keras.utils import to_categorical
# from keras.callbacks import EarlyStopping
#
# # %matplotlib inline
#
# df = pd.read_csv('newtrainingdata.csv')
# print(df.head())
# '''sns.countplot(df.target)
# plt.xlabel('Label')
# plt.title('Number of positive and negative reviews')'''
# X = df.SentimentText
# Y = df.Sentiment
# le = LabelEncoder()
# Y = le.fit_transform(Y)
# Y = Y.reshape(-1, 1)
# X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.15)
# max_words = 1000
# max_len = 150
# print("stage1")
# tok = Tokenizer(num_words=max_words)
# tok.fit_on_texts(X_train)
# sequences = tok.texts_to_sequences(X_train)
# sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)
# print("stage2")
# def RNN():
#     inputs = Input(name='inputs' ,shape=[max_len])
#     layer = Embedding(max_words,50,input_length=max_len)(inputs)
#     layer = LSTM(64)(layer)
#     layer = Dense(256,name='FC1')(layer)
#     layer = Activation('relu')(layer)
#     layer = Dropout(0.5)(layer)
#     layer = Dense(1,name='out_layer')(layer)
#     layer = Activation('sigmoid')(layer)
#     model = Model(inputs=inputs, outputs=layer)
#     return model
# model = RNN()
# model.summary()
# model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
# print("stage3")
# allfiles=os.listdir()
# if "LSTM_Classifier.pickle" not in allfiles:
#     print("LSTM classifier Model Training started")
#     model.fit(sequences_matrix, Y_train, batch_size=128, epochs=10, validation_split=0.2,
#               callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
#     print("stage4")
#     print("LSTM classifier model training compleated")
#
#     LSTMCM = open('LSTM_Classifier.pickle', 'wb')
#
#     pickle.dump(model, LSTMCM)  # here we are referencing the pickle module that we imported
#     # the 2 parameters needed for dump() is - what to dump and where to dump
#     LSTMCM.close()
#     if "LSTM_Classifier.pickle" in os.listdir():
#         print("LSTM classifier Model saved successfully")
#     else:
#         print("LSTM classifier was not saved ")
# else:
#     LSTMCM = open('LSTM_Classifier.pickle', 'rb')
#     model = pickle.load(LSTMCM)
#     print("LSTM_Classifier Model loaded")
#
#
#
# test_sequences = tok.texts_to_sequences(X_test)
# test_sequences_matrix = sequence.pad_sequences(test_sequences,maxlen=max_len)
# accr = model.evaluate(test_sequences_matrix,Y_test)
# print("stage5")
# def check(Testing_context):
#     txts = tok.texts_to_sequences(Testing_context)
#     txts = sequence.pad_sequences(txts, maxlen=max_len)
#     preds = model.predict(txts)
#     print(Testing_context)
#     print(preds)
#     if preds>=0.50 :
#         print('Positive')
#     elif preds<0.5:
#         print('Negative')
#
# # Testing_context1 = [" was he close to suicide? poor boy "]
# # Testing_context2 = ["i am happy"]
# # Testing_context3 = ["Yup it was fun! watching 21 "]
# # Testing_context4 = ["it's not sad. kinda like finding 100 pesos in the pavement. which never happens to me "]
# # Testing_context5 = ["is so sad for my APL friend"]
# # Testing_context6 = ["I missed the New Moon trailer"]
# # Testing_context7 = ["ok thats it you win."]
# # Testing_context8 = ["Very sad about Iran."]
# # Testing_context9 = ["congrats to helio though"]
# # Testing_context10 = ["RIP, David Eddings."]
# # Testing_context11= ["really wanted Safina to pull out a win &amp; to lose like that..."]
# # Testing_context12= ["pleased"]
# # Testing_context13= ["oh thank you!"]
# # Testing_context14= ["not a cool night."]
# # Testing_context15= ["My new car was stolen....by my mother who wanted to go pose at church."]
# # Testing_context16= ["im sick  'cough cough"]
# # Testing_context17= ["RY CRY CRY   "]
# # Testing_context18= ["Goodnight"]
# # Testing_context19= ["i like you more"]
# # Testing_context20= ["i lost two followers"]
# # Testing_context21= ["I wanted to go cinema"]
# # Testing_context22= ["im bored anyone wanna talk"]
# # Testing_context23= [" was he close to suicide? poor boy "]
# # Testing_context24= ["i m not happy"]
# # Testing_context25= ["i am sad"]
# # Testing_context26= ["i am not happy"]
# # Testing_context27= ["i am unhappy"]
# #
# #
# # check(Testing_context1)
# # check(Testing_context2)
# # check(Testing_context3)
# # check(Testing_context4)
# # check(Testing_context5)
# # check(Testing_context6)
# # check(Testing_context7)
# # check(Testing_context8)
# # check(Testing_context9)
# # check(Testing_context10)
# # check(Testing_context11)
# # check(Testing_context12)
# # check(Testing_context13)
# # check(Testing_context14)
# # check(Testing_context15)
# # check(Testing_context16)
# # check(Testing_context17)
# # check(Testing_context18)
# # check(Testing_context19)
# # check(Testing_context20)
# # check(Testing_context21)
# # check(Testing_context22)
# # check(Testing_context23)
# # check(Testing_context24)
# # check(Testing_context25)
# # check(Testing_context26)
# # check(Testing_context27)
# tweetlist = ["I am not happy", "I am not frustrated", "I am feeling very stressed", "She is not cheerful",
#                 "I will not do suicide", "I will do suicide", "She wants to die"]
# for item in tweetlist:
#     data=[]
#     data.append(item)
#     check(list(data))
# # method11()
#
#
# '''
#     [' was he close to suicide? poor boy ']
#     [[0.02250681]]
#     Negative
#     ['i am happy']
#     [[0.91927874]]
#     Positive
#     ['Yup it was fun! watching 21 ']
#     [[0.97589207]]
#     Positive
#     ["it's not sad. kinda like finding 100 pesos in the pavement. which never happens to me "]
#     [[0.07890859]]
#     Negative
#     ['is so sad for my APL friend']
#     [[0.01246906]]
#     Negative
#     ['I missed the New Moon trailer']
#     [[0.04426914]]
#     Negative
#     ['ok thats it you win.']
#     [[0.8838523]]
#     Positive
#     ['Very sad about Iran.']
#     [[0.00962782]]
#     Negative
#     ['congrats to helio though']
#     [[0.8569402]]
#     Positive
#     ['RIP, David Eddings.']
#     [[0.64322674]]
#     Positive
#     ['really wanted Safina to pull out a win &amp; to lose like that...']
#     [[0.3083812]]
#     Negative
#     ['pleased']
#     [[0.64322674]]
#     Positive
#     ['oh thank you!']
#     [[0.96808285]]
#     Positive
#     ['not a cool night.']
#     [[0.6791744]]
#     Positive
#     ['My new car was stolen....by my mother who wanted to go pose at church.']
#     [[0.18341649]]
#     Negative
#     ["im sick  'cough cough"]
#     [[0.03220288]]
#     Negative
#     ['RY CRY CRY   ']
#     [[0.00325864]]
#     Negative
#     ['Goodnight']
#     [[0.9481939]]
#     Positive
#     ['i like you more']
#     [[0.7991786]]
#     Positive
#     ['i lost two followers']
#     [[0.07225962]]
#     Negative
#     ['I wanted to go cinema']
#     [[0.11571187]]
#     Negative
#     ['im bored anyone wanna talk']
#     [[0.16733056]]
#     Negative
#     [' was he close to suicide? poor boy ']
#     [[0.02250681]]
#     Negative
#     ['i m not happy']
#     [[0.3415248]]
#     Negative
#     ['i am sad']
#     [[0.00944276]]
#     Negative
#     ['i am not happy']
#     [[0.40121517]]
#     Negative
#     ['i am unhappy']
#     [[0.5356729]]
#     Positive
# '''

# def method11():
import matplotlib,os,pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pasta.augment import inline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import Activation, LSTM, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping

# %matplotlib inline

df = pd.read_csv('newtrainingdata.csv')
print(df.head())
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
print("stage1")
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(X_train)
sequences = tok.texts_to_sequences(X_train)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)
print("stage2")
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
model = RNN()
model.summary()
model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
print("stage3")
allfiles=os.listdir()
if "LSTM_Classifier.pickle" not in allfiles:
    print("LSTM classifier Model Training started")
    model.fit(sequences_matrix, Y_train, batch_size=128, epochs=10, validation_split=0.2,
              callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
    print("stage4")
    print("LSTM classifier model training compleated")

    LSTMCM = open('LSTM_Classifier.pickle', 'wb')

    pickle.dump(model, LSTMCM)  # here we are referencing the pickle module that we imported
    # the 2 parameters needed for dump() is - what to dump and where to dump
    LSTMCM.close()
    if "LSTM_Classifier.pickle" in os.listdir():
        print("LSTM classifier Model saved successfully")
    else:
        print("LSTM classifier was not saved ")
else:
    LSTMCM = open('LSTM_Classifier.pickle', 'rb')
    model = pickle.load(LSTMCM)
    print("LSTM_Classifier Model loaded")

import code

test_sequences = tok.texts_to_sequences(X_test)
test_sequences_matrix = sequence.pad_sequences(test_sequences,maxlen=max_len)
accr = model.evaluate(test_sequences_matrix,Y_test)
print("stage5")
def check(Testing_context):
    txts = tok.texts_to_sequences(Testing_context)
    txts = sequence.pad_sequences(txts, maxlen=max_len)
    preds = model.predict(txts)
    # print(Testing_context)
    # print(preds)
    if preds>=0.50 :
        return 'Positive'
    elif preds<0.5:
        return 'Negative'

# Testing_context1 = [" was he close to suicide? poor boy "]
# Testing_context2 = ["i am happy"]
# Testing_context3 = ["Yup it was fun! watching 21 "]
# Testing_context4 = ["it's not sad. kinda like finding 100 pesos in the pavement. which never happens to me "]
# Testing_context5 = ["is so sad for my APL friend"]
# Testing_context6 = ["I missed the New Moon trailer"]
# Testing_context7 = ["ok thats it you win."]
# Testing_context8 = ["Very sad about Iran."]
# Testing_context9 = ["congrats to helio though"]
# Testing_context10 = ["RIP, David Eddings."]
# Testing_context11= ["really wanted Safina to pull out a win &amp; to lose like that..."]
# Testing_context12= ["pleased"]
# Testing_context13= ["oh thank you!"]
# Testing_context14= ["not a cool night."]
# Testing_context15= ["My new car was stolen....by my mother who wanted to go pose at church."]
# Testing_context16= ["im sick  'cough cough"]
# Testing_context17= ["RY CRY CRY   "]
# Testing_context18= ["Goodnight"]
# Testing_context19= ["i like you more"]
# Testing_context20= ["i lost two followers"]
# Testing_context21= ["I wanted to go cinema"]
# Testing_context22= ["im bored anyone wanna talk"]
# Testing_context23= [" was he close to suicide? poor boy "]
# Testing_context24= ["i m not happy"]
# Testing_context25= ["i am sad"]
# Testing_context26= ["i am not happy"]
# Testing_context27= ["i am unhappy"]
#
#
# check(Testing_context1)
# check(Testing_context2)
# check(Testing_context3)
# check(Testing_context4)
# check(Testing_context5)
# check(Testing_context6)
# check(Testing_context7)
# check(Testing_context8)
# check(Testing_context9)
# check(Testing_context10)
# check(Testing_context11)
# check(Testing_context12)
# check(Testing_context13)
# check(Testing_context14)
# check(Testing_context15)
# check(Testing_context16)
# check(Testing_context17)
# check(Testing_context18)
# check(Testing_context19)
# check(Testing_context20)
# check(Testing_context21)
# check(Testing_context22)
# check(Testing_context23)
# check(Testing_context24)
# check(Testing_context25)
# check(Testing_context26)
# check(Testing_context27)
# tweetlist = ["I am not happy", "I am not frustrated", "I am feeling very stressed", "She is not cheerful",
#                 "I will not do suicide", "I will do suicide", "She wants to die"]
# for item in tweetlist:
#     data=[]
#     data.append(item)
#     check(list(data))
# method11()

def master():
    print("master")
    if 'tweets_list.pickle' in os.listdir():
        print('inside if')
        pickle_in = open('tweets_list.pickle', 'rb')
        tweetlist = pickle.load(pickle_in)
        pickle_in.close()
        output = []
        for item in tweetlist:
            result = check(item)
            output.append(result)
        pickle_out = open('LSTM_resuts.pickle', 'wb')
        pickle.dump(output, pickle_out)
        pickle_out.close()
        print("done")
master()
'''
    [' was he close to suicide? poor boy ']
    [[0.02250681]]
    Negative
    ['i am happy']
    [[0.91927874]]
    Positive
    ['Yup it was fun! watching 21 ']
    [[0.97589207]]
    Positive
    ["it's not sad. kinda like finding 100 pesos in the pavement. which never happens to me "]
    [[0.07890859]]
    Negative
    ['is so sad for my APL friend']
    [[0.01246906]]
    Negative
    ['I missed the New Moon trailer']
    [[0.04426914]]
    Negative
    ['ok thats it you win.']
    [[0.8838523]]
    Positive
    ['Very sad about Iran.']
    [[0.00962782]]
    Negative
    ['congrats to helio though']
    [[0.8569402]]
    Positive
    ['RIP, David Eddings.']
    [[0.64322674]]
    Positive
    ['really wanted Safina to pull out a win &amp; to lose like that...']
    [[0.3083812]]
    Negative
    ['pleased']
    [[0.64322674]]
    Positive
    ['oh thank you!']
    [[0.96808285]]
    Positive
    ['not a cool night.']
    [[0.6791744]]
    Positive
    ['My new car was stolen....by my mother who wanted to go pose at church.']
    [[0.18341649]]
    Negative
    ["im sick  'cough cough"]
    [[0.03220288]]
    Negative
    ['RY CRY CRY   ']
    [[0.00325864]]
    Negative
    ['Goodnight']
    [[0.9481939]]
    Positive
    ['i like you more']
    [[0.7991786]]
    Positive
    ['i lost two followers']
    [[0.07225962]]
    Negative
    ['I wanted to go cinema']
    [[0.11571187]]
    Negative
    ['im bored anyone wanna talk']
    [[0.16733056]]
    Negative
    [' was he close to suicide? poor boy ']
    [[0.02250681]]
    Negative
    ['i m not happy']
    [[0.3415248]]
    Negative
    ['i am sad']
    [[0.00944276]]
    Negative
    ['i am not happy']
    [[0.40121517]]
    Negative
    ['i am unhappy']
    [[0.5356729]]
    Positive
'''

