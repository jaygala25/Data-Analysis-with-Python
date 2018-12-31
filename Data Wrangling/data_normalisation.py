import pandas as pd

df=pd.read_excel('automobile.xlsx')

print(df['length'])

max=df['length'].max()

df['length']=df['length']/max

print(df['length'])