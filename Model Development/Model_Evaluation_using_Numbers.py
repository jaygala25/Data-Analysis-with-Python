import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np 

df=pd.read_excel('automobile.xlsx')

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

lm=LinearRegression()

x=df[['highway-mpg']]
y=df['price']

lm.fit(x,y)

y=lm.predict(df[['highway-mpg']])

mse=mean_squared_error(df['price'],y)
print(mse)
print()

rsquared=lm.score(df[['highway-mpg']],df['price'])
print(rsquared)