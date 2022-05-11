import pandas as pd
import numpy as np
import random

#一、(将是否下雨置为0 / 1)
dataset = pd.read_csv('E:\ML\\first_work\decision_tree\datasets\original_data.csv')
# print(dataset)
dataset.loc[dataset['rainfall']!=0,'rainfall'] = 1

# #验证是否下雨为1， 不下雨为0
# for i in dataset['rainfall']:
#     print(i)


#相同时间段的一些数据进行修正，使得相近时间段的下雨标签相同
rain_index = dataset[dataset['rainfall'] == 1].index
#获取下雨索引列表
rain_index = rain_index.tolist()

#将下雨前后时间段也修正为下雨状态
list_index = 0
for i in list(dataset.index):

    if i == rain_index[list_index]:
        # print('a')
        dataset.loc[i-20:i+20, 'rainfall'] = 1
        list_index = list_index + 1

    if list_index > len(rain_index) - 1:
        break


#存入handle_csv
dataset.to_csv('E:\ML\\first_work\decision_tree\datasets/handle_data.csv')

#====================================================================================================#


# 正样本 ~~ 负样本

dataset = pd.read_csv('E:\ML\\first_work\decision_tree\datasets/handle_data.csv')
# print(dataset)

#正样本
true_samples = dataset[dataset['rainfall']==1]
# true_samples.sample(frac=1)
true_samples = true_samples[0:250]
print(len(true_samples))    #正样本大约250条

#取大约250条负样本
false_samples = dataset[dataset['rainfall']==0]
# false_samples.sample(frac=1)
false_samples = false_samples[0:250]
print(len(false_samples))

#总样本 = 正样本 + 负样本
samples = pd.concat([true_samples, false_samples], axis=0)

samples.to_csv('E:\ML\\first_work\decision_tree\datasets/equilibrium_data.csv')


#============================================================================================#
#三、数据验证

dataset = pd.read_csv('equilibrium_data.csv')
dataset = dataset.values.tolist()
for index, data in enumerate(dataset):
    dataset[index].pop(0)
    if data[5] == 0.0:
        dataset[index][5] = 'No'
    else:
        dataset[index][5] = 'Yes'

random.shuffle(dataset)
print(dataset)
