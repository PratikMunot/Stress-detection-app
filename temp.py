import pandas as pd

df=pd.read_csv('final.csv',index_col=0)
print(df.head())

print(df.shape)
print(type(df.SentimentText.iloc[2]))

df=df.sample(frac=1).reset_index(drop=True)

print(df.head(10))

