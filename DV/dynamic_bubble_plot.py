import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def tracker(cur_num):
    # 获取当前索引
    cur_index = cur_num % num_points

    # 设置当前点颜色
    datapoints['color'][:, 3] = 1.0

    # 修改圈大小
    datapoints['size'] += datapoints['growth']

    # 修改就数据点位置
    datapoints['position'][cur_index] = np.random.uniform(0, 1, 2)
    datapoints['size'][cur_index] = 7
    datapoints['color'][cur_index] = (0, 0, 0, 1)
    datapoints['growth'][cur_index] = np.random.uniform(40, 150)

    # 更新散点图参数
    scatter_plot.set_edgecolors(datapoints['color'])
    scatter_plot.set_sizes(datapoints['size'])
    scatter_plot.set_offsets(datapoints['position'])

if __name__=='__main__':
    # 生成图像
    fig = plt.figure(figsize=(9, 7), facecolor=(0,0.9,0.9))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1), ax.set_xticks([])
    ax.set_ylim(0, 1), ax.set_yticks([])

    # 随机位置创建，初始化数据。随机增长率
    
    num_points = 20
    datapoints = np.zeros(num_points, dtype=[('position', float, 2),
            ('size', float, 1), ('growth', float, 1), ('color', float, 4)])
    datapoints['position'] = np.random.uniform(0, 1, (num_points, 2))
    datapoints['growth'] = np.random.uniform(40, 150, num_points)

    # 创建一个每一帧都更新的散点图
    scatter_plot = ax.scatter(datapoints['position'][:, 0], datapoints['position'][:, 1],
                      s=datapoints['size'], lw=0.7, edgecolors=datapoints['color'],
                      facecolors='none')

    # 用tracker启动动态模拟
    animation = FuncAnimation(fig, tracker, interval=10)

    plt.show()
