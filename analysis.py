import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('./data/houseSmallData.csv')
train = data.iloc[0:100, :]
salePrice = train['SalePrice']


def describeSalePrice():
    print(salePrice.describe())


def plotHistogramSalePrice():
    plt.hist(salePrice)
    plt.show(block=False)
    plt.pause(5)
    plt.close()


def plotLogNormalDistribution():
    plt.hist(np.log(salePrice))
    plt.show(block=False)
    plt.pause(5)
    plt.close()


def skewSalePrice():
    print(salePrice.skew())
    print(np.log(salePrice).skew())


skewSalePrice()
