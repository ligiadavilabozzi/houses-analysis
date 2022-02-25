import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

data = pd.read_csv('./data/houseSmallData.csv')

train = data.iloc[0:20]
numeric = train.select_dtypes(include=[np.number])

corr = numeric.corr()
cols_sale = corr['SalePrice'].sort_values(ascending=False)[0:5]
cols_index = corr['SalePrice'].sort_values(ascending=False)[0:3].index

X = train[cols_index]
Y = train['SalePrice']
X = X.drop(['SalePrice'], axis=1)

lr = linear_model.LinearRegression()
model = lr.fit(X, Y)
predictions = model.predict(X)


def dimensionalityDatabase():
    print(f'The dimensionality of the Dataframe is: {data.shape}')
    print('-------------------------------------------------')


def investigateSalePrice():
    print(f"Investigate Sale Price of 5 datas:\n{train['SalePrice']}")
    print('-------------------------------------------------')


def plotHistSalePrice():
    plt.hist(train['SalePrice'])
    plt.show(block=False)
    plt.pause(5)
    plt.close('all')


def dimensionalityNumbersData():
    print('-------------------------------------------------')
    print(
        f'The dimensionality of numbers data is: {numeric.shape}\nFrom: {data.shape} datas')
    print('-------------------------------------------------')


def correlationShapeNumberDatas():
    print('-------------------------------------------------')
    print(f'Correlation shape of number datas: {corr.shape}')
    print('-------------------------------------------------')


def correlationFactor():
    print('-------------------------------------------------')
    print(f'Calculate Correlation Factor:\n{cols_sale}')
    print('-------------------------------------------------')


def howGoodIsModel():
    print('-------------------------------------------------')
    print(f'How good is the model: {model.score(X, Y)}')
    print('-------------------------------------------------')


def scatterPrediction():
    plt.scatter(predictions, Y)
    plt.show(block=False)
    plt.pause(5)
    plt.close('all')
