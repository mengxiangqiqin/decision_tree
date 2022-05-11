from utils import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pickle



# 开始创建决策树
def createTree(dataSet, labels, featLabels):
    classList = [example[-1] for example in dataSet]  # 取分类标签(是否下雨:yes or no)

    if classList.count(classList[0]) == len(classList):  # 如果类别完全相同则停止继续划分
       return classList[0]

    if len(dataSet[0]) == 1 or len(labels) == 0:  # 遍历完所有特征时返回出现次数最多的类标签

        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)  # 选择最优特征
    bestFeatLabel = labels[bestFeat]  # 最优特征的标签
    featLabels.append(bestFeatLabel)
    myTree = {bestFeatLabel: {}}  # 根据最优特征的标签生成树

    del (labels[bestFeat])  # 删除已经使用特征标签
    featValues = [example[bestFeat] for example in dataSet]  # 得到训练集中所有最优特征的属性值
    uniqueVals = set(featValues)  # 去掉重复的属性值
    for value in uniqueVals:  # 遍历特征，创建决策树。
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels, featLabels)

    return myTree



#获取决策树叶子结点的数目 ，即获取我们的据册数分类结果数目
def getNumLeafs(myTree):

    print('-------------')
    print(myTree)

    numLeafs = 0  # 初始化叶子
    firstStr = next(iter(myTree))

    secondDict = myTree[firstStr]  # 获取下一组字典
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':  # 测试该结点是否为字典（树节点），如果不是字典，代表此结点为叶子结点
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs




#获取决策树的depth
#原理与获取叶子节点类似
def getTreeDepth(myTree):

    maxDepth = 0  # 初始化决策树深度
    firstStr = next(iter(myTree))

    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth




#进行决策树节点绘制

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    arrow_args = dict(arrowstyle="<-")  # 定义箭头格式
    font = FontProperties(fname='E:\ML\\first_work\decision_tree/No.136-ShangShouYouRanTi-2.ttf', size=14)  # 设置中文字体
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',  # 绘制结点
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args, fontproperties=font)

def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]  # 计算标注位置
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


#绘制决策树
def plotTree(myTree, parentPt, nodeTxt):
    decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # 设置结点格式
    leafNode = dict(boxstyle="round4", fc="0.8")  # 设置叶结点格式
    numLeafs = getNumLeafs(myTree)  # 获取决策树叶结点数目，决定了树的宽度
    depth = getTreeDepth(myTree)  # 获取决策树层数
    firstStr = next(iter(myTree))  # 下个字典
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)  # 中心位置
    plotMidText(cntrPt, parentPt, nodeTxt)  # 标注有向边属性值
    plotNode(firstStr, cntrPt, parentPt, decisionNode)  # 绘制结点
    secondDict = myTree[firstStr]  # 下一个字典，也就是继续绘制子结点
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD  # y偏移
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':  # 测试该结点是否为字典，如果不是字典，代表此结点为叶子结点
            plotTree(secondDict[key], cntrPt, str(key))  # 不是叶结点，递归调用继续绘制
        else:  # 如果是叶结点，绘制叶结点，并标注有向边属性值
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD



#创建画布，简单使用pyplot

def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')  # 创建fig
    fig.clf()  # 清空fig
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # 去掉x、y轴
    plotTree.totalW = float(getNumLeafs(inTree))  # 获取决策树叶结点数目
    plotTree.totalD = float(getTreeDepth(inTree))  # 获取决策树层数
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0  # x偏移
    plotTree(inTree, (0.5, 1.0), '')  # 绘制决策树
    plt.show()  # 显示绘制结果



#### 使用决策树进行分类（递归记录树和叶子）

def classify(inputTree, featLabels, testVec):

    firstStr = next(iter(inputTree))  # 获取决策树结点
    secondDict = inputTree[firstStr]  # 下一个字典
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():

        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)

            else:
                classLabel = secondDict[key]

        else: classLabel = 'no'

    return classLabel



#数据后处理
#存储决策树
def storeTree(inputTree, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(inputTree, fw)

#读取决策树
def grabTree(filename):
    fr = open(filename, 'rb')
    return pickle.load(fr)