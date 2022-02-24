import pandas as pd

data = pd.read_csv('./data/houseSmallData.csv')
print(f'The dimensionality of the Database is: {data.shape}')
train = data.iloc[0:20, :]
print(train.head())
