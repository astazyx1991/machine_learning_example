import numpy as np
import matplotlib.pyplot as plt

# 定义气泡个数
num_vals = 40

# 生成随机值
x = np.random.rand(num_vals)
y = np.random.rand(num_vals)

# 定义每个点的个数
# 最大半径
max_radius = 25
area = np.pi * (max_radius * np.random.rand(num_vals)) ** 2  

# 生成颜色
colors = np.random.rand(num_vals)

# 画出数据点
plt.scatter(x, y, s=area, c=colors, alpha=1.0)

#show
plt.show()
