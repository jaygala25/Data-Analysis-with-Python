import pandas as pd

df=pd.read_excel('automobile.xlsx')

df_fuel=pd.get_dummies(df['fuel-type'])

print(df_fuel)

df['gas']=df_fuel['gas']
df['diesel']=df_fuel['diesel']

print(df)