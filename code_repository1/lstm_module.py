import matplotlib,pickle,os
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

df = pd.read_csv('main5.csv')
print(df.head())
sns.countplot(df.target)
plt.xlabel('Label')
plt.title('Number of positive and negative reviews')
X = df.text
Y = df.target
le = LabelEncoder()
Y = le.fit_transform(Y)
Y = Y.reshape(-1, 1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.15)
max_words = 1000
max_len = 150
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(X_train)
sequences = tok.texts_to_sequences(X_train)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)
if "LSTM_Model.pickle" not in os.listdir():
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

    model.fit(sequences_matrix,Y_train,batch_size=128,epochs=10,validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',min_delta=0.0001)])



    lstmM = open('LSTM_Model.pickle', 'wb')
    pickle.dump(model, lstmM)  # here we are referencing the pickle module that we imported
            # the 2 parameters needed for dump() is - what to dump and where to dump
    lstmM.close()
else:
    print("LSTM Model loaded")
    lstmM = open('LSTM_Model.pickle', 'rb')
    model = pickle.load(lstmM)
    test_sequences = tok.texts_to_sequences(X_test)
    test_sequences_matrix = sequence.pad_sequences(test_sequences,maxlen=max_len)
    accr = model.evaluate(test_sequences_matrix,Y_test)

    def check(Testing_context):

        txts = tok.texts_to_sequences(Testing_context)
        txts = sequence.pad_sequences(txts, maxlen=max_len)

        preds = model.predict(txts)
        print(Testing_context)
        print(preds)
        if preds>=0.50 :
            print('Positive')
        elif preds<0.5:
            print('Negative')

    Testing_context1 = ["i hate you"]
    Testing_context2 = ["i am going to sucide."]
    Testing_context3 = ["I am happy."]
    Testing_context4 = ["i wil not do sucide"]
    Testing_context5 = ["i hate the dentist....who invented them anyways"]
    Testing_context6 = ["congratulations to you."]
    Testing_context7 = ["i am not happy"]
    check(Testing_context1)
    check(Testing_context2)
    check(Testing_context3)
    check(Testing_context4)
    check(Testing_context5)
    check(Testing_context6)
    check(Testing_context7)