import pandas as pd
import os
import re
from csv import DictReader
from csv import writer

input_file="unclean.csv"
output_file="clean_neg.csv"




data = pd.read_csv(input_file,encoding='utf8')
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
    return target,text

def append_row(file_name, list_of_elem):
    # Open file in append model
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

with open(input_file, 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    for row in csv_dict_reader:
       # print(row['text'])
        new=cleanTxt(row['target'],row['text'])
        print(new)
        append_row(output_file ,new)

