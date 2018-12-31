import pandas as pd 
from sklearn.linear_model import LinearRegression
import numpy as np 

lm=LinearRegression()

df=pd.read_excel('automobile.xlsx')

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['horsepower'].mean()
df['horsepower'].replace(np.nan,mean,inplace=True)

mean=df['curb-weight'].mean()
df['curb-weight'].replace(np.nan,mean,inplace=True)

mean=df['engine-size'].mean()
df['engine-size'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

x=df[['horsepower','curb-weight','engine-size','highway-mpg']]
y=df['price']

lm.fit(x,y)

print(lm.intercept_)
print(lm.coef_)

X=[[60,2000,150,30]]
Y=lm.predict(X)

print(Y)