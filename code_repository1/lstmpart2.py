# def method11(sentence):
# pass


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
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('main5.csv')
#print(df.head())
'''sns.countplot(df.target)
plt.xlabel('Label')
plt.title('Number of positive and negative reviews')'''
X = df.text
Y = df.target
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

if "LSTM_Classifier2.pickle" not in allfiles:
    print("LSTM classifier Model Training started")
    model.fit(sequences_matrix, Y_train, batch_size=128, epochs=10, validation_split=0.2,
              callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
    # print("stage4")
    print("LSTM classifier model training compleated")

    LSTMCM = open('LSTM_Classifier2.pickle', 'wb')

    pickle.dump(model, LSTMCM)  # here we are referencing the pickle module that we imported
    # the 2 parameters needed for dump() is - what to dump and where to dump
    LSTMCM.close()
    if "LSTM_Classifier2.pickle" in os.listdir():
        print("LSTM classifier Model saved successfully")
    else:
        print("LSTM classifier was not saved ")
else:
    LSTMCM = open('LSTM_Classifier2.pickle', 'rb')
    model = pickle.load(LSTMCM)


test_sequences = tok.texts_to_sequences(X_test)
test_sequences_matrix = sequence.pad_sequences(test_sequences, maxlen=max_len)
accr = model.evaluate(test_sequences_matrix, Y_test)
print("LSTM_Classifier Model loaded")
print(accr)
def check(Testing_context):
    txts = tok.texts_to_sequences(Testing_context)
    txts = sequence.pad_sequences(txts, maxlen=max_len)
    preds = model.predict(txts)
    print(Testing_context)
    print(preds)
    if preds >= 0.50:
        return 4
        # print('Positive')
    elif preds < 0.5:
        return 0
        # print('Negative')

sentence=["I am happy","I am very sad"]

# for tweet in sentence:
#     check([tweet])
df2 = pd.read_csv('newtrainingdata.csv')
#print(df.head())

X2 = df2.SentimentText
Y2 = df2.Sentiment
le = LabelEncoder()
Y2 = le.fit_transform(Y2)
Y2 = Y2.reshape(-1, 1)
X2_train,X2_test,Y2_train,Y2_test = train_test_split(X2,Y2,test_size=0.15)
y_pred=[]
for i in X2_test:
    y_pred.append(check([i]))

yy=[]
for i in Y2_test:
    if i==1:
        yy.append(4)
    if i==0:
        yy.append(0)
print(yy)
print(len(yy))
print(y_pred)
print(len(y_pred))
print(Y2_test)
print(len(Y2_test))

print(confusion_matrix(yy, y_pred))
print(classification_report(yy, y_pred))

'''

[[3210 3307]
 [2544 5938]]
              precision    recall  f1-score   support

           0       0.56      0.49      0.52      6517
           1       0.64      0.70      0.67      8482

    accuracy                           0.61     14999
   macro avg       0.60      0.60      0.60     14999
weighted avg       0.61      0.61      0.61     14999
'''