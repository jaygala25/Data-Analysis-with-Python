import pandas as pd
# read the online file by the URL provides above, and assign it to variable "df"
path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(path,header=None)

headers=['symboling','normalised-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels',
'engine-location','wheel-base','length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke',
'compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

df.columns=headers
print(df);
print()

df.to_csv('automobile.csv')
print('File saved successfully')
print()

print(df.dtypes)
print()

print(df.describe())
print()

print(df.describe(include='all'))
print()

print(df.info)
print()