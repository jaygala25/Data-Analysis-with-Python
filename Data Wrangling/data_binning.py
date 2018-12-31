import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('automobile.xlsx')

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

df['price']=df['price'].astype('int64')

binwidth=int((max(df['price'])-min(df['price']))/3)
bin = list(range(min(df['price'])+binwidth,max(df['price'])-binwidth,binwidth))
bin = [df['price'].min()] + bin + [df['price'].max()]

print(bin)
print()

group_names=['Low','Medium','High']

df['price-binned']=pd.cut(df['price'],bins=bin,labels=group_names,include_lowest=True)
print(df['price-binned'])

print()
print(df['price-binned'].value_counts())

print()
print(df)

df['price'].plot(kind='hist',xticks=bin,bins=bin)
plt.xlabel('price')
plt.ylabel('count')
plt.title('price bins')
plt.show()