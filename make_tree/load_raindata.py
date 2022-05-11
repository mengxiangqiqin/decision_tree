import numpy as np
import pandas as pd
import random


#加载数据集并进行格式整理
def createDataSet():
    dataSet = pd.read_csv('E:\ML\\first_work\decision_tree\datasets/equilibrium_data.csv')
    dataSet = dataSet.values.tolist()
    for index, data in enumerate(dataSet):
        dataSet[index].pop(0)
        if data[5] == 0.0:
            dataSet[index][5] = 'no'
        else:
            dataSet[index][5] = 'yes'
    #打乱数据集
    random.shuffle(dataSet)
    # #随机取50条数据进行测试
    # dataSet = dataSet[0:500]

    #test数据
    # dataSet = [[0, 0, 0, 0, 1, 'no'],
    #            [0, 0, 0, 1, 1, 'no'],
    #            [0, 1, 0, 1, 1, 'yes'],
    #            [0, 1, 1, 0, 1, 'yes'],
    #            [0, 0, 0, 0, 1, 'no'],
    #            [1, 0, 0, 0, 1, 'no'],
    #            [1, 0, 0, 1, 1, 'no'],
    #            [1, 1, 1, 1, 1, 'yes'],
    #            [1, 0, 1, 2, 1, 'yes'],
    #            [1, 0, 1, 2, 1, 'yes'],
    #            [2, 0, 1, 2, 1, 'yes'],
    #            [2, 0, 1, 1, 1, 'yes'],
    #            [2, 1, 0, 1, 1, 'yes'],
    #            [2, 1, 0, 2, 1, 'yes'],
    #            [2, 0, 0, 0, 1, 'no']]

    labels = ['风速', '风向', '气压', '气温' ,'湿度']  # 特征标签
    return dataSet, labels  # 返回数据集和分类属性