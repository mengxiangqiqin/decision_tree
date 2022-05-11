from make_tree import *
from load_raindata import *



if __name__ == '__main__':
    dataSet, labels = createDataSet()
    print('----------------------------------加载成功，开始决策树分类---------------------------------------------')
    print('\n')
    print('----------------------------------查看数据集-----------------------------------------------------------')
    print(dataSet)
    featLabels = []

    print('-----------------------------------查看当前树节点--------------------------------------------------------')
    myTree = createTree(dataSet, labels, featLabels)

    # pyplot绘制决策树，（数据量过大时不建议绘制，一是不直观， 二是防止程序崩溃）
    createPlot(myTree)

    #测试数据， 根据标签和实际数据进行测试
    testVec = [4, 102, 1005, 22, 77]

    result = classify(myTree, featLabels, testVec)
    print('\n')
    print('=========================================================================================================')
    print('最后的预测结果为：')
    if result == 'yes':
        print('下雨')
    if result == 'no':
        print('不下雨')