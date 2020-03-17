import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# def result_pic(result):
#     """
#     雷达图的绘制
#     :param result: 分类数据
#     :return: 雷达图
#     """
#     # 解析出类别标签和种类
#     labels = ['I', 'M', 'C', 'Vin', 'Ver']
#     kinds = 1
#     result=pd.read_excel('wzsj.xlsx')
#
#     # 由于在雷达图中，要保证数据闭合，这里就再添加L列，并转换为 np.ndarray
#     result = pd.concat([result, result[['L']]], axis=1)
#     centers = np.array(result.iloc[:, 1:])
#
#     # 分割圆周长，并让其闭合
#     n = len(labels)
#
#
#     angle = np.linspace(0, 2 * np.pi, n, endpoint=False)
#     angle = np.concatenate((angle, [angle[0]]))
#
#     # 绘图
#     fig = plt.figure()
#     ax = fig.add_subplot(111, polar=True)  # 参数polar, 以极坐标的形式绘制图形
#
#     # 画线
#     for i in range(len(kinds)):
#         ax.plot(angle, centers[i], linewidth=2, label=kinds[i])
#         # ax.fill(angle, centers[i])  # 填充底色
#
#     # 添加属性标签
#     ax.set_thetagrids(angle * 180 / np.pi, labels)
#     plt.title('different kind')
#     plt.legend(loc='lower right')
#     plt.show()
#
# if __name__ == '__main__':
#     result = pd.read_csv('./data_7/cluster_center.csv', sep=',')
#     result_pic(result)
labels = np.array(['I','M','S','Vin','Ver'])
#数据个数
dataLenth = 5
#数据
data = np.array([0.92,0.9,0.7,1,0])
#========自己设置结束============

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)# polar参数！！
ax.plot(angles, data, 'bo-', linewidth=2)# 画线
ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title("top2", va='bottom', fontproperties="SimHei")
ax.set_rlim(0,1)
ax.grid(True)
plt.show()