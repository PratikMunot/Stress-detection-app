# ----------- LSTM --------------
import os,pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model,save_model,load_model,model_from_json,model_from_yaml
from keras.layers import Activation, LSTM, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

from keras.callbacks import EarlyStopping
from sklearn.metrics import classification_report, confusion_matrix






#===========================  LSTM MODEL =========================================
df = pd.read_csv('newtrainingdata.csv')
df=df.sample(frac=1).reset_index(drop=True)
#print(df.head())
'''sns.countplot(df.target)
plt.xlabel('Label')
plt.title('Number of positive and negative reviews')'''
X = df.SentimentText
Y = df.Sentiment
le = LabelEncoder()
Y = le.fit_transform(Y)
Y = Y.reshape(-1, 1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=1000)
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

if "LSTM.h5" not in allfiles:
    print("LSTM classifier Model Training started")
    model.fit(sequences_matrix, Y_train, batch_size=128, epochs=20, validation_split=0.1,
              callbacks=[EarlyStopping(monitor='val_loss', min_delta=0.0001)])
    # print("stage4")
    # print("\nLSTM classifier model training compleated")
    #
    # LSTMCM = open('LSTM_Classifier.pickle', 'wb')
    #
    # pickle.dump(model, LSTMCM)  # here we are referencing the pickle module that we imported
    # # the 2 parameters needed for dump() is - what to dump and where to dump
    # LSTMCM.close()
    # if "LSTM_Classifier.pickle" in os.listdir():
    #     print("\nLSTM classifier Model saved successfully")
    # else:
    #     print("\nLSTM classifier was not saved ")

    model_json = model.to_json()
    with open('LSTM_Classifier.json','w') as js:
        js.write(model_json)
    model.save_weights('LSTM_Classifier.h5')

    model_yaml = model.to_yaml()
    with open('LSTM_Classifier.yaml', 'w') as js:
        js.write(model_yaml)
    # model.save_weights('LSTM_Classifier.h5')
    model.save('LSTM.h5')



else:

    model = load_model('LSTM.h5')



#     js=open('LSTM_Classifier.json','r')
#     loaded=js.read()
#     js.close()
#     model = model_from_json(loaded)
#     model.load_weights('LSTM_Classifier.h5')
#     print('json model loaded')
#
#
# model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
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
    print(model.metrics_names[1],accr[1])
    # print(type(Y_test))
    # print(type(y_pred))
    y_pred = list(y_pred)
    Y_test2 = list(Y_test)
    # print(y_pred)
    # print(Y_test)
    a = []
    for i in y_pred:
        if i=='Negative':
            a.append(0)
        else:
            a.append(1)
    b = []
    for i in Y_test:
        if i[0] == 0:
            b.append(0)
        else:
            b.append(1)
    print(a,b)
    # y_pred = [int(i) for i in y_pred]
    # Y_test2 = [int(i) for i in Y_test2]
    # print(type(y_pred[1]))
    # print(type(Y_test2[1]))
    print(confusion_matrix(b, a))
    print(classification_report(b, a))
# accur_lstm()
'''
accuracy 0.7549999952316284

[[371  73]
 [172 384]]
              precision    recall  f1-score   support

           0       0.68      0.84      0.75       444
           1       0.84      0.69      0.76       556

    accuracy                           0.76      1000
   macro avg       0.76      0.76      0.75      1000
weighted avg       0.77      0.76      0.76      1000

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
lstm_(sentence)
accur_lstm()

# ======================================================================================


