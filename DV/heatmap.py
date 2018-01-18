import numpy as np
import matplotlib.pyplot as plt

# 2组数据集
group1 = ['France', 'Italy', 'Spain', 'Portugal', 'Germany'] 
group2 = ['Japan', 'China', 'Brazil', 'Russia', 'Australia']

# 随机值
data = np.random.rand(5, 5)

fig, ax = plt.subplots()

# 创建热力图
heatmap = ax.pcolor(data, cmap=plt.cm.gray)

# 坐标轴位置
ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

# 显示为表 
ax.invert_yaxis()
ax.xaxis.tick_top()

# 加标签
ax.set_xticklabels(group2, minor=False)
ax.set_yticklabels(group1, minor=False)

plt.show()
