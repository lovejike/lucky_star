import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 只需在末尾添加一个和起始点重合的点
data = pd.read_csv("need_data.csv", index_col=0)
data['END'] = data['N']
print(data)
# new_data = data[data.columns[::-1]]
# print(new_data)
# data = new_data
# print(data)

theta = np.array([0., 1.875, 1.75, 1.625, 1.5, 1.375, 1.25,
                  1.125, 1., 0.875, 0.75, 0.625,
                  0.5, 0.375, 0.25,  0.125, 0.])

colors_arr = ['#76EE00', '#B22222', '#EEEE00', '#FF0000',
              'sandybrown', 'yellow', 'hotpink', 'darkorange', 'darkred']

feature = 'N NNE NE ENE E ESE SE SSE S SSW SW WSW W WNW NW NNW N'.split()

ax = plt.subplot(111, polar=True)
for i in range(9):
    data_i = data.iloc[[i]].values[0]
    # print(i)
    print(data_i)
    ax.plot(theta * np.pi, data_i, 'ro-', lw=0.5,
              marker=".", mfc="b", ms=1)
    ax.fill(theta * np.pi, data_i, facecolor=colors_arr[i], alpha=1)  # 填充
    ax.set_rmax(250)

    # ax.set_theta_offset(45)
    ax.set_thetagrids(theta * 180, feature)
    ax.set_theta_zero_location("N")

plt.show()
