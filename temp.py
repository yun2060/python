# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
path=r"C:\Users\20601\OneDrive - dba4.tw\桌面\ML\class\一元线性回归.xls"

data=pd.read_excel(path)

x=data['广告费'].values.reshape((-1,1))
y=data['销售额'].values

model=LinearRegression()
model.fit(x,y)
k1=model.coef_[0]
b1=model.intercept_

k2=(np.mean(x)*np.mean(y)-np.mean(data['广告费'].values*y))/((np.mean(x)**2)-np.mean(x**2))
b2=np.mean(y)-k2*np.mean(x)

x_cor=np.linspace(0,20,50)
y1=k1*x_cor+b1
y2=k2*x_cor+b2

plt.plot(x_cor,y1,'r-',x_cor,y2,'b--')
plt.scatter(x,y)
plt.legend(['sklearn','ours'])