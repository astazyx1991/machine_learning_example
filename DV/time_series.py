import numpy
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
import matplotlib.cbook as cbook
from matplotlib.ticker import Formatter

# 定义一个类将日期格式化
class DataFormatter(Formatter):
    def __init__(self, dates, date_format='%Y-%m-%d'):
        self.dates = dates
        self.date_format = date_format

    # 提取position 位置的时间t的值
    def __call__(self, t, position=0):
        index = int(round(t))
        if index >= len(self.dates) or index < 0:
            return ''

        return self.dates[index].strftime(self.date_format)

if __name__=='__main__':
    # 加载csv文件 
    input_file = cbook.get_sample_data('aapl.csv', asfileobj=False)

    # csv加载成numpy记录数组中
    data = csv2rec(input_file)
    
    # 提取子集并画出
    data = data[-70:]

    # 创建日期格式化对象
    formatter = DataFormatter(data.date)

    # X axis
    x_vals = numpy.arange(len(data))

    # y轴表示收盘价
    y_vals = data.close 

    # 画出数据
    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(x_vals, y_vals, 'o-')
    fig.autofmt_xdate()
    plt.show()
