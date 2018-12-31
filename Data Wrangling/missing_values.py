import pandas as pd
import numpy as np

df = pd.read_excel('automobile.xlsx')

print(df);
print()

#replacing missing values
mean=df['normalised-losses'].mean()
df['normalised-losses'].replace(np.nan,mean,inplace=True)
print(df)

#droping missing values
df.dropna(subset=['price'],axis=0,inplace=True)
print(df)