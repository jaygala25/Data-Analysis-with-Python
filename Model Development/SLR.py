import pandas as pd 
from sklearn.linear_model import LinearRegression
import numpy as np 

lm=LinearRegression()

df=pd.read_excel('automobile.xlsx')

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

x=df[['highway-mpg']]
y=df['price']

lm.fit(x,y)

print(lm.intercept_)
print(lm.coef_)

X=[[20]]
Y=lm.predict(X)

print(Y)