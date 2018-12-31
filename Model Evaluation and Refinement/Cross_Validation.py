import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict

df=pd.read_excel('automobile.xlsx')

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

x_data=df['highway-mpg']
y_data=df['price']
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=0)
'''print(x_train)
print(x_test)
print(y_train)
print(y_test)'''

print()
lm=LinearRegression()

yhat=cross_val_predict(lm,df[['highway-mpg']],df[['price']],cv=3)
print(yhat)
print(len(yhat))

scores=cross_val_score(lm,df[['highway-mpg']],df[['price']],cv=3)
print(scores)
print(np.mean(scores))