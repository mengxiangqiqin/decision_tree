

# 决策树之青岛天气预测



### 问题描述

​	小组第一次机器学习大作业，利用决策树（ID3）算法进行青岛天气预测（分类问题）



#### 算法核心

​	详情见word

### 项目架构

```
decision_tree
	|----datasets(数据预处理)
		|----handle_data.py
		|----equilibrium_data.csv
		|----handle_data.csv
		|----original_data.csv
		|----original_data.xls
	|----make_tree
		|----load_raindata.py (加载数据)
		|----make_tree.py (创建树)
		|----run.py (运行代码)
		|----utils.py (香农熵，特征值等)
	|----ttf
	|----venv
	|----readme(使用流程)
	|----word

```



### 数据预处理

​	本小组在青岛市信息公开网进行信息检索，找到了一系列与天气有关的数据，整理得到2W+条可用于决策树的数据。

#### 数据处理过程（已完成）

1. 获取原生xls数据
2. 转为csv格式便于读取
3. 进行数据格式整理，将 “是否下雨” 作为分类结果标签，用 0/1代替。
4. equilibrium数据，总样本数 = 正样本 + 负样本， 正样本数约等于负样本数， 使得决策树建立更准确，数据对决策误差的影响降低。



#### 数据处理流程图

![](E:\ML\first_work\decision_tree\charm\捕获.PNG)

### 运行demo

```python
#运行项目
python decision_tree.py
```

```
decision_tree.py

#是否启用pyplot绘制决策树
#line 285 
createPlot(myTree)
```



#### 如何适配你的数据

- 首先准备xls或者csv数据，注意标签不要有中文，并且数据格式统一好，确保可以被pandas正确读取。

![](E:\ML\first_work\decision_tree\charm\csv格式.PNG)

```
#修改路径
#line 6 自己xls数据集路径

python datasets/handle_data.py
```

```python
python datasets/handle_data.py
```



#### 加载数据

```python
#配置标签数据
line 38    labels = ['风速', '风向', '气压', '气温' ,'湿度']
python make_tree/load_raindata.py
```

​	加载数据后可以在本文件进行一些数据查看、乱序、切片等等。



#### 创建决策树

```python

#配置测试数据
#line 21  testVec = [4, 102, 1005, 22, 77]
python make_tree/run.py
```



#### 结果展示

​	以青岛天气各种因素对将降雨的影响，进行决策树预测

因素有风向、风速、气温、气压、湿度，预测下雨

![](E:\ML\first_work\decision_tree\charm\decision_tree.png)

​	预测结果为不下雨



#### 用于多分类问题

```python
#修改 run.py
#line 26 ~ 30 改为自己的结果规则
#注意确保在load_data.py中加载自己的数据是多分类且正确格式的
```

​	由于多分类问题我没有去做，小伙伴们可以自己试一下



#### 结果分析

​	由于是为了大作业，并无项目价值，故很明显可以看出数据质量较差而带来的数据分类效果不理想，过于拟合，可以自己想一下如何去改善数据进行构建合理的决策树

​	项目瑕疵，欢迎大佬指出修正！！

##### 在此，感谢中国石油大学（华东）孔凡华、王卫超、冒翔对本项目的合作贡献。