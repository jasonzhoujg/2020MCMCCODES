
import matplotlib.pyplot as plt
import seaborn as sns

#
#
# f, (ax1, ax2) = plt.subplots(figsize=(6, 4), nrows=2)
#
# # cmap用cubehelix map颜色
#
# cmap = sns.cubehelix_palette(start=1.5, rot=3, gamma=0.8, as_cmap=True)
#
# pt = df.corr()  # pt为数据框或者是协方差矩阵
#
# sns.heatmap(pt, linewidths=0.05, ax=ax1, vmax=900, vmin=0, cmap=cmap)
#
# ax1.set_title('cubehelix map')
#
# ax1.set_xlabel('')
#
# ax1.set_xticklabels([])  # 设置x轴图例为空值
#
# ax1.set_ylabel('kind')
#
# # cmap用matplotlib colormap
#

# sns.heatmap(pt, linewidths=0.05, ax=ax2, vmax=900, vmin=0, cmap='rainbow')
#
# # rainbow为 matplotlib 的colormap名称
#
# ax2.set_title('matplotlib colormap')
# ax2.set_xlabel('region')
# ax2.set_ylabel('kind')

import numpy as np

np.random.seed(0)
x = np.array([[15,14,66,89,189],[12,23,98,178,45],[8,32,207,121,34],[100,246,54,21,10],[176,132,25,13,12]])
f, (ax1, ax2) = plt.subplots(figsize=(6, 6), nrows=2)

sns.heatmap(x, annot=True, ax=ax1)
# sns.heatmap(x, annot=True, fmt='.1f', ax=ax2)

ax2.set_title('reviews and ratings')
ax2.set_xlabel('region')
ax2.set_ylabel('kind')
plt.show()