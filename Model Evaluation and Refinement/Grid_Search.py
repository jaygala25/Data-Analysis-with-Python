import pandas as pd 
import numpy as np 
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

parameter1=[{'alpha':[0.001,0.1,1,10,100,1000,10000,100000,1000000]}]

df=pd.read_excel('automobile.xlsx')

mean=df['horsepower'].mean()
df['horsepower'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['curb-weight'].mean()
df['curb-weight'].replace(np.nan,mean,inplace=True)

mean=df['engine-size'].mean()
df['engine-size'].replace(np.nan,mean,inplace=True)

RR=Ridge()

grid1=GridSearchCV(RR,parameter1,cv=4)

grid1.fit(df[['horsepower','curb-weight','engine-size','highway-mpg']],df['price'])

print(grid1.best_estimator_)
print()

scores=grid1.cv_results_
print(scores['mean_test_score'])
print()

parameter2=[{'alpha':[0.001,0.1,1,10,100],'normalize':[True,False]}]

RR=Ridge()

grid1=GridSearchCV(RR,parameter2,cv=4)

grid1.fit(df[['horsepower','curb-weight','engine-size','highway-mpg']],df['price'])

print(grid1.best_estimator_)
print()

scores=grid1.cv_results_
print(scores['mean_test_score'])
print()

for param,mean_val,mean_test in zip(scores['params'],scores['mean_test_score'],scores['mean_train_score']):
	print(param,"R^2 on test data:",mean_val,"R^2 on train data:",mean_test)