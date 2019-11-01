# 侠的机器学习笔记

使用博客来记录自己的机器学习过程，笔记是通过网络、书籍以及自我总结而成的。

本笔记分为五部分：

1. 机器学习基础
2. 监督学习算法
3. 无监督学习算法
4. 深度学习算法
5. 强化学习身法

所有已完成的笔记都会发布到 [CSDN Blog](https://blog.csdn.net/weixin_45488228) 上，感兴趣的小伙伴可以关注一下，我将会坚持更新机器学习以及深度学习的笔记。所有的笔记都是由 Jupyter Notebook 写成的，Notebook 可以在这个 [Github](https://github.com/X1AOX1A/Machine-Learning) 库内找到。

> Q：为什么文章经常会变成 404 ？
> A：因为我会经常更新以前的文章，而修改过的文章需要一段时间进行审核。

关于各类机器学习算法的优点，可以参考[这篇文章](https://www.hackingnote.com/en/machine-learning/algorithms-pros-and-cons)

关于各类机器学习算法的应用场合，可以参考[这篇文章](https://cloud.tencent.com/developer/article/1064119)

PS：监督学习中分类算法和回归算法并没有严格的界限，分类算法可以做回归，而回归算法也可以做分类。但为了方便起见，因此将按算法首次提出时的目的进行区分。

# 1. 机器学习基础
- [x] [机器学习 | 分类评估指标](https://blog.csdn.net/weixin_45488228/article/details/98896294)
- [x] [机器学习 | 回归评估指标](https://blog.csdn.net/weixin_45488228/article/details/98897061)
- [x] [机器学习 | 聚类评估指标](https://blog.csdn.net/weixin_45488228/article/details/100549820)
- [x] [机器学习 | 距离计算](https://blog.csdn.net/weixin_45488228/article/details/100593643)
- [x] [机器学习 | 模型选择](https://blog.csdn.net/weixin_45488228/article/details/99115070)
- [x] [机器学习 | 特征缩放](https://blog.csdn.net/weixin_45488228/article/details/100680503)
- [x] [机器学习 | 网络搜索及可视化](https://blog.csdn.net/weixin_45488228/article/details/99235845)
- [x] [机器学习 | 梯度下降原理及Python实现](https://blog.csdn.net/weixin_45488228/article/details/99506171)
- [x] [机器学习 | 早期停止法原理及Python实现](https://blog.csdn.net/weixin_45488228/article/details/100101549)
- [x] [机器学习 | EM 算法原理](https://blog.csdn.net/weixin_45488228/article/details/102267311)
# 2. 监督学习
## 2.1 分类算法
- [x] [机器学习 | 分类评估指标](https://blog.csdn.net/weixin_45488228/article/details/98896294)

### 贝叶斯
- [x] [监督学习 | 朴素贝叶斯原理及Python实现](https://blog.csdn.net/weixin_45488228/article/details/98505200)
- [x] [监督学习 | 朴素贝叶斯之Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/98505609)

### 决策树
- [x] [监督学习 | ID3 决策树原理及Python实现](https://blog.csdn.net/weixin_45488228/article/details/98665115)
- [x] [监督学习 | ID3 & C4.5 决策树原理](https://blog.csdn.net/weixin_45488228/article/details/102136999)
- [x] [监督学习 | CART 分类回归树原理](https://blog.csdn.net/weixin_45488228/article/details/102171151)
- [x] [监督学习 | 决策树之Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/98751821)
- [x] [监督学习 | 决策树之网络搜索](https://blog.csdn.net/weixin_45488228/article/details/99253498)

### SVM 支持向量机
- [x] [监督学习 | SVM 之线性支持向量机原理](https://blog.csdn.net/weixin_45488228/article/details/99687673)
- [x] [监督学习 | SVM 之非线性支持向量机原理](https://blog.csdn.net/weixin_45488228/article/details/99698777)
- [x] [监督学习 | SVM 之支持向量机Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/99711744)

### KNN K近邻
- [ ] 监督学习 | KNN K近临原理及Sklearn实现

## 2.2 回归算法
- [x] [机器学习 | 回归评估指标](https://blog.csdn.net/weixin_45488228/article/details/98897061)

### 多元线性回归
- [x] [监督学习 | 线性回归 之多元线性回归原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/99345417)

### 正则线性模型
- [x] [监督学习 | 线性回归 之正则线性模型原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/100087447)
- [ ] 监督学习 | 线性回归 之Softmax回归原理及Sklearn实现

### Logistic 回归分类器
- [x] [监督学习 | 线性分类 之Logistic回归原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/100110734)

### 非线性回归
- [x] [监督学习 | 非线性回归 之多项式回归原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/100068461)

## 2.3 集成方法
### Bagging、随机森林
- [x] [监督学习 | 集成学习 之Bagging、随机森林及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/100013912)

### AdaBoost
- [x] [监督学习 | 集成学习 之AdaBoost原理及Slearn实现](https://blog.csdn.net/weixin_45488228/article/details/100027978)

# 3. 无监督学习

## 3.1 聚类算法
- [x] [机器学习 | 聚类评估指标](https://blog.csdn.net/weixin_45488228/article/details/100549820)
- [x] [机器学习 | 距离计算](https://blog.csdn.net/weixin_45488228/article/details/100593643)

### 原型聚类 - KMeans K均值
- [x] [无监督学习 | KMeans 与 KMeans++ 原理](https://blog.csdn.net/weixin_45488228/article/details/100612021)
- [x] [无监督学习 | KMeans 之Sklearn实现：电影评分聚类](https://blog.csdn.net/weixin_45488228/article/details/100637019)

### 层次聚类 - 凝聚聚类
- [x] [无监督学习 | 层次聚类 之凝聚聚类原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/102493562)

### 密度聚类 - DBSCAN
- [x] [无监督学习 | DBSCAN 原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/102470231)

### 概率聚类 - GMM 高斯混合
- [x] [无监督学习 | GMM 高斯混合聚类原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/102463264)

## 3.2 降维算法

### PCA 主成分分析

- [x] [无监督学习 | PCA 主成分分析原理及Sklearn实现](https://blog.csdn.net/weixin_45488228/article/details/102557013)
- [x] [无监督学习 | PCA 主成分分析之客户分类](https://blog.csdn.net/weixin_45488228/article/details/102574432)

### 随机投影

- [ ]  无监督学习 | 随机投影原理及Sklearn实现

### ICA 独立主成分分析

- [ ] 无监督学习 | ICA 独立主成分分析原理及Sklearn实现

# 4. 深度学习

### 深度学习基础
### BP 神经网络
### CNN 卷积神经网络

# 5. 强化学习

### 强化学习基础

### 动态规划

### 蒙特卡洛模拟

### 时间差分

### 深度 Q 学习

### 策略梯度

### 行动者-评论者方法

  

  