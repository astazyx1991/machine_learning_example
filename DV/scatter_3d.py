import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#生成空白图像
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成值个数
n = 6666

#用lambda生成给定范围内的值
f = lambda minval, maxval, n: minval + (maxval - minval) * np.random.rand(n)

# 生成值
x_vals = f(15, 41, n)
y_vals = f(-10, 70, n)
z_vals = f(-52, -37, n)

#画出值
ax.scatter(x_vals, y_vals, z_vals, c='k', marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
