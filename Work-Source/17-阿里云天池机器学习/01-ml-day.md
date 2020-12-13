###  2020年12月13日

-----------------------------------------------------------------



01 -day 

1. 理论知识： 

	逻辑回归是一个分类模型,其本质上是一个线性的分类器，很多时候我们也会拿逻辑回归模型去做一些**__任务尝试的基线__**（基础水平）,逻辑模型比较简单，可读性比较强.

    - 优点：实现简单，易于理解和实现；计算代价不高，速度很快，存储资源低；
   
    - 缺点：容易欠拟合，分类精度可能不高
   
      
   
   逻辑回归模型广泛用于各个领域，包括机器学习，大多数医学领域和社会科学
   
   逻辑回归模型现在同样是很多分类算法的**基础组件**,比如 分类任务中基于GBDT算法+LR逻辑回归实现的信用卡交易反欺诈，CTR(点击通过率)预估等，其好处在于__输出值自然地落在0到1之间__，并且有**_概率意义_**。模型清晰，有对应的概率学理论基础
   
   它拟合出来的**参数**就代表了每一个特征(feature)**_对结果的影响_**
   
   
   
2.  代码流程

    - Step1:库函数导入   
    - Step2:模型训练
    - Step3:模型参数查看
    - Step4: 数据和模型可视化
    - Step5 :模型预测

 3. 算法实践

    - Step1:库函数导入       
      ```python   

        ##  基础函数库
        import numpy as np 

        ## 导入画图库
        import matplotlib.pyplot as plt
        import seaborn as sns

        ## 导入逻辑回归模型函数
        from sklearn.linear_model import LogisticRegression

      ```
      
    - Step2: 模型训练
    
       ```python  
		## 构造数据集
        x_fearures = np.array([[-1, -2], [-2, -1], [-3, -2], [1, 3], [2, 1], [3, 2]])
        y_label = np.array([0, 0, 0, 1, 1, 1])

        ## 调用逻辑回归模型
        lr_clf = LogisticRegression()

        ## 用逻辑回归模型拟合构造的数据集
        lr_clf = lr_clf.fit(x_fearures, y_label) #其拟合方程为 y=w0+w1*x1+w2*x2
      ```
    
    - Step3:模型参数查看
        ```python  
            ## 查看其对应模型的w
            print('the weight of Logistic Regression:',lr_clf.coef_)

            ## 查看其对应模型的w0
            print('the intercept(w0) of Logistic Regression:',lr_clf.intercept_)
        ```
    
    - Step4: 数据和模型可视化
    	```python
    	  plt.figure()
        plt.scatter(x_fearures[:,0],x_fearures[:,1], c=y_label, s=50, cmap='viridis')
        plt.title('Dataset')
        plt.show()
    	```
    - Step5 :模型预测





 ###  机器学习算法（一）: 基于逻辑回归的分类预测--ML&阿里云天池机器学习
-----------------------------------------------------------------