import pandas as pd 
import numpy as np 
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures 

df=pd.read_excel('automobile.xlsx')

mean=df['horsepower'].mean()
df['horsepower'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

mean=df['curb-weight'].mean()
df['curb-weight'].replace(np.nan,mean,inplace=True)

mean=df['engine-size'].mean()
df['engine-size'].replace(np.nan,mean,inplace=True)

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['normalised-losses'].mean()
df['normalised-losses'].replace(np.nan,mean,inplace=True)

mean=df['symboling'].mean()
df['symboling'].replace(np.nan,mean,inplace=True)

x_data=df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalised-losses','symboling']]
y_data=df['price']
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=0)
x_train=pd.DataFrame(x_train)
x_test=pd.DataFrame(x_test)
y_train=pd.DataFrame(y_train)
y_test=pd.DataFrame(y_test)

pr=PolynomialFeatures(degree=2)
x_train_pr=pr.fit_transform(x_train)
x_test_pr=pr.fit_transform(x_test)

RidgeModel=Ridge(alpha=0.1)
RidgeModel.fit(x_train_pr,y_train)
yhat=RidgeModel.predict(x_test_pr)
print('predicted:', yhat[0:4])
print('test set :', y_test[0:4].values)

Rsqu_test=[]
Rsqu_train=[]
alp=5000*np.array(range(0,10000))

for alfa in alp:
    RidgeModel=Ridge(alpha=alfa) 
    RidgeModel.fit(x_train_pr,y_train)
    Rsqu_test.append(RidgeModel.score(x_test_pr,y_test))
    Rsqu_train.append(RidgeModel.score(x_train_pr,y_train))

plt.plot(alp,Rsqu_test,label='validation data  ')
plt.plot(alp,Rsqu_train,'r',label='training Data ')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()