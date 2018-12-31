import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df=pd.read_excel('automobile.xlsx')

a=sns.regplot(x='engine-size',y='price',data=df)
plt.ylim(0,)
plt.show()

a=sns.regplot(x='highway-mpg',y='price',data=df)
plt.ylim(0,)
plt.show()

a=sns.regplot(x='peak-rpm',y='price',data=df)
plt.ylim(0,)
plt.show()