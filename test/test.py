import numpy as np
import os
#import matplotlib as plt
import pandas as pd
df_origin = pd.read_excel("2013.xls", header=0)
print(df_origin)

# step1.将第一列时间分成 日期+时间
columns_1 = ['dt', 'hour']
df1 = df_origin['时间'].astype(str).str.split(' ', expand=True)
df1.columns = columns_1

# step2.将第二列小时只取整数
columns_2 = ['hour', 'minite', 'second']
df2 = df1['hour'].str.split(':', expand=True)
df2.columns = columns_2
df2 = df2.drop('minite', axis=1)
df2 = df2.drop('second', axis=1)

# step3.月份
columns_3 = ['y', 'm', 'd']
df3 = df1['dt'].str.split('-', expand=True)
df3.columns = columns_3
df3 = df3.drop('y', axis=1)
df3 = df3.drop('d', axis=1)

# step4.删除多余列
df_origin = df_origin.drop('时间', axis=1)
df1 = df1.drop('hour', axis=1)

# step5. 形成最终df
df = df1.join(df2).join(df3).join(df_origin)
print(df)

# step6.计算平均值
indexes = ['NO', 'O3', 'NOX', 'NO2']
tmp_list = []
for idx in indexes:
    tmp = df.filter(items=['name', 'm', 'hour', idx])
    res = tmp[tmp[idx] != 9999].groupby(['name', 'm', 'hour'], as_index=False)[idx].mean()
    # print(res)
    tmp_list.append(res)

result0 = tmp_list[0]
result1 = tmp_list[1]
result01 = pd.merge(result0, result1, on=['name', 'm', 'hour'])

result2 = tmp_list[2]
result3 = tmp_list[3]
result23 = pd.merge(result2, result3, on=['name', 'm', 'hour'])

total = pd.merge(result01, result23, on=['name', 'm', 'hour'])
print(total.to_csv('res.csv'))
# print(df)