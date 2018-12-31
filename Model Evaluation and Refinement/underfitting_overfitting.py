import pandas as pd 
import numpy as np 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_excel('automobile.xlsx')

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

x_data=df['highway-mpg']
y_data=df['price']
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=0)
x_train=pd.DataFrame(x_train)
x_test=pd.DataFrame(x_test)
y_train=pd.DataFrame(y_train)
y_test=pd.DataFrame(y_test)

Rsqu_test=[]
order=[1,2,3,4,5,6]
lm=LinearRegression()

for n in order:
	pr=PolynomialFeatures(degree=n)
	x_train_pr=pr.fit_transform(x_train[['highway-mpg']])
	x_test_pr=pr.fit_transform(x_test[['highway-mpg']])
	lm.fit(x_train_pr,y_train)
	Rsqu_test.append(lm.score(x_test_pr,y_test))

print(Rsqu_test)