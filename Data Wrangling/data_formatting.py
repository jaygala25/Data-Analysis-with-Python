import pandas as pd
import numpy as np

df = pd.read_excel('automobile.xlsx')

print(df['city-mpg'])
print()
#print(df.dtypes)

df['city-mpg']=235/df['city-mpg'];
df.rename(columns={'city-mpg':'city-L/100km'},inplace=True)
print(df['city-L/100km'])