from initialInformations import dimensionalityDatabase, investigateSalePrice, plotHistSalePrice, dimensionalityNumbersData, correlationShapeNumberDatas, correlationFactor, howGoodIsModel, scatterPrediction
import time


while True:
    print("Selection one option about House Database:")
    print("1 - Dimensionality of the dataframe")
    print("2 - Investigate Sale Price of 20 datas")
    print("3 - Plot Histogram Sale Prices of 20 datas")
    print("4 - Dimensionality of Numbers Datas")
    print("5 - Correlation Shape of Number Datas")
    print("6 - Calculate Correlation Factor")
    print("7 - How good is Model")
    print("8 - Print Scatter Predictions")
    print("9 - Exit")
    print("----------------------------------------------------------------------")
    print("Digit the number of the option:")
    option = int(input())

    if option == 1:
        dimensionalityDatabase()
        time.sleep(2)
    if option == 2:
        investigateSalePrice()
        time.sleep(2)
    if option == 3:
        plotHistSalePrice()
    if option == 4:
        dimensionalityNumbersData()
        time.sleep(2)
    if option == 5:
        correlationShapeNumberDatas()
        time.sleep(2)
    if option == 6:
        correlationFactor()
        time.sleep(2)
    if option == 7:
        howGoodIsModel()
        time.sleep(2)
    if option == 8:
        scatterPrediction()
    if option == 9:
        exit()
