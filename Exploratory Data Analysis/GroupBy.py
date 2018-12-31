import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel('automobile.xlsx')

df_test=df[['drive-wheels','body-style','price']]
df_grp=df_test.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(df_grp)
print()

df_pivot=df_grp.pivot(index='drive-wheels',columns='body-style')
print(df_pivot)
print(df['price'].min())
print(df['price'].max())

ax=sns.heatmap(df_pivot,vmin=df['price'].min(),vmax=df['price'].max())
plt.show()