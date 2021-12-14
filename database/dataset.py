# import pandas as pd
# import os
# import re
# from csv import DictReader
# from csv import writer
#
# input_file="abcd.csv"
# output_file="clean_neg.csv"
#
#
#
#
#
# #data1=pd.reader.
# #print(data)
# #df=pd.DataFrame([tweet.full_text for tweet in data],columns=['Tweet'])
# #df.head()
# def cleanTxt(target,text):
#     text = re.sub(r'@[A-Za-z0-9]+','',text)
#     text =re.sub(r'#','',text)
#     text=re.sub(r'RT[\s]+','',text)
#     text=re.sub(r'https?:\/S+','',text)
#     text=re.sub(r'http','',text)
#     text = re.sub(r'www.[A-Za-z0-9]+.[A-Za-z0-9]','', text)
#     text =re.sub(r'@','',text)
#     text =re.sub(r'[*,!@#$%^&*()-_+]','',text)
#     list1=list(text)
#     new=[]
#     a = "�"
#     for i in text:
#         if i=='ï' or i==a:
#             continue
#         if i.isalpha() or i==' ':
#             new.append(i)
#             print(i,end='')
#     text=''.join(new)
#     text=text.strip()
#     return target,text
#
# def append_row(file_name, list_of_elem):
#     # Open file in append model
#     with open(file_name, 'a+', newline='') as write_obj:
#         # Create a writer object from csv module
#         csv_writer = writer(write_obj)
#         # Add contents of list as last row in the csv file
#         csv_writer.writerow(list_of_elem)
# def start():
#     data = pd.read_csv(input_file, encoding='utf8')
#     with open(input_file, 'r') as read_obj:
#         csv_dict_reader = DictReader(read_obj)
#         for row in csv_dict_reader:
#            # print(row['text'])
#             new=cleanTxt(row['target'],row['text'])
#             print(new)
#             append_row(output_file ,new)
# start()
# # import pandas as pd
# #
# # df=pd.read_csv('clean_neg.csv')
# #
# # # print(df.head(5))    # print first five records
# # # print(df.tail(5))    # print last five records
# #
# # print(df.shape)
# # print(df)
# # print(type(df.b[0]))
#
#
import pandas as pd
import os
import re
from csv import DictReader
from csv import writer

input_file="tryial"
output_file="clean_pos.csv"





#data1=pd.reader.
#print(data)
#df=pd.DataFrame([tweet.full_text for tweet in data],columns=['Tweet'])
#df.head()
def cleanTxt(target,text):
    text = re.sub(r'@[A-Za-z0-9]+','',text)
    text =re.sub(r'#','',text)
    text=re.sub(r'RT[\s]+','',text)
    text=re.sub(r'https?:\/S+','',text)
    text=re.sub(r'http','',text)
    text = re.sub(r'www.[A-Za-z0-9]+.[A-Za-z0-9]','', text)
    text =re.sub(r'@','',text)
    text =re.sub(r'[*,!@#$%^&*()-_+]','',text)
    list1=list(text)
    new=[]
    a = "�"
    for i in text:
        if i=='ï' or i==a:
            continue
        if i.isalpha() or i==' ':
            new.append(i)
            print(i,end='')
    text=''.join(new)
    text=text.strip()
    if target=='4':
        target='1'
    return target,text

# def append_row(file_name, list_of_elem):
#     # Open file in append model
#
#         # Create a writer object from csv module
#
#         # Add contents of list as last row in the csv file

def start():
    cnt=1
    data = pd.read_csv(input_file, encoding='utf8')
    with open(input_file, 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)
        with open(output_file, 'a+', newline='') as write_obj:
            for row in csv_dict_reader:
                # print(row['text'])
                new=cleanTxt(row['target'],row['text'])
                # new = (cnt,new[0],new[1])
                # cnt+=1
                print(new)
                if new[1]=='':
                    continue
                csv_writer = writer(write_obj)
                csv_writer.writerow(new)

                # append_row(output_file ,new)
start()
# import pandas as pd
#
# df=pd.read_csv('clean_neg.csv')
#
# print(df.head(5))    # print first five records
# print(df.tail(5))    # print last five records
#
# print(df.shape)
# print(df)
# d=df.copy()
# df2=df.append(df,sort=False)
# frames=[df,df,df,df,df,df,df,df,df,df]
# df2=pd.concat(frames)
# # df2['target']+=df['target']
# print(df2.shape)
# print(len(df2))
# # with open('testing.csv','w') as fp:
# import time
# for i in range(len(df2)):
#     # time.sleep(1)
#     if i%1000==0:
#         print(df2.iloc[i])
#     # fp.write(df2.iloc[i])
#
# import sys
# print(len(df2['target']))
# print(sys.getsizeof(df2))