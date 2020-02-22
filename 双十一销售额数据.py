import matplotlib.pyplot as plt
import numpy as np
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.array([year for year in range(2009, 2020)])
y = np.array([0.5, 9.36, 52, 191, 352, 571, 912, 1207, 1682.69, 2135, 2637])

z1 = np.polyfit(x, y, 3)  # 用三次多项式拟合
p1 = np.poly1d(z1)  # 生成多项式对象

yvals = p1(x)  # 拟合值

plt.scatter(x, y, label='实际销售额')
plt.plot(x, yvals, 'r', label='拟合销售额')
plt.xlabel('年份')
plt.ylabel('销售额')
plt.legend(loc=4)  # 指定legend的位置
plt.title('2009-2019淘宝双十一销售额拟合曲线')

print('拟合多项式:\n', p1)  # 打印拟合多项式

print("-" * 40)
print('2020年预测值：\n', p1(2020))
print('2020年双十一的总销售额为：', p1(2020), '元')

plt.show()



# x=2020
# y=0.159*(x**3) - 930.2*(x**2) + (1.813e+06)*x - (1.176e+09)
# print(y)