import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_excel('automobile.xlsx')

print(df.describe())
print()

drive_wheel_counts=pd.DataFrame(df['drive-wheels'].value_counts())

print(drive_wheel_counts)
print()

drive_wheel_counts.rename(columns={'drive-wheels':'value_counts'},inplace=True)
print(drive_wheel_counts)
print()

drive_wheel_counts.index.name='drive_wheels'
print(drive_wheel_counts)
print()

a=sns.boxplot(x='drive-wheels',y='price',data=df)
plt.show()

x=df['engine-size']
y=df['price']
plt.scatter(x,y)
plt.title("Scatter plot of engine-size vs price")
plt.xlabel("Engine-size")
plt.ylabel('Price')
plt.show()