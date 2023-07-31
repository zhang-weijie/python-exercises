import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from IPython.display import display

plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif':['simhei','Arial']})
#%matplotlib inline
from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python3以上的版本！')
lianjia_df = pd.read_csv(r'C:\developmentTools\Java\bluetoothtrans\lianjia.csv')
display(lianjia_df.head(n = 2))

#添加新特征房屋均价
df = lianjia_df.copy()
df['PerPrice'] = lianjia_df['Price']/lianjia_df['Size']
#重新摆放列位置
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation', 'PerPrice', 'Price']
df = pd.DataFrame(df, columns = columns)
#重新审视数据集
display(lianjia_df.head(n = 2))

#对二手房区域分组对比二手房数量和每平米房价
df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending = False).to_frame().reset_index()
df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending = False).to_frame().reset_index()

#绘制表格，实现数据可视化
f, [ax1,ax2,ax3] = plt.subplots(3,1,figsize = (20,15))
sns.barplot(x = 'Region', y = 'PerPrice', palette = 'Blues_d', data=df_house_mean, ax = ax2)
ax2.set_title('北京各大区二手房数量对比', fontsize = 15)
ax2.set_xlabel('区域')
ax2.set_ylabel('数量')

sns.boxplot(x = 'Region', y = 'Price', data = df, ax = ax3)
ax3.set_title('北京各大区二手房房屋总价', fontsize = 15)
ax3.set_xlabel('区域')
ax3.set_ylabel('房屋总价')
plt.show()

f, [ax1,ax2] = plt.subplots(1, 2, figsize=(15, 5))
# 建房时间的分布情况
# 分布图
sns.distplot(df['Size'], bins=20, ax=ax1, color='r')
sns.kdeplot(df['Size'], shade=True, ax=ax1)
# 建房时间和出售价格的关系
sns.regplot(x='Size', y='Price', data=df, ax=ax2)
plt.show()

#移除不符合条件的特异值
df = df[(df['Layout']!='叠拼别墅')&(df['Size']<1000)]

#户型Layout的分布情况
f, ax1= plt.subplots(figsize=(20,20))
sns.countplot(y='Layout', data=df, ax=ax1)
ax1.set_title('房屋户型',fontsize=15)
ax1.set_xlabel('数量')
ax1.set_ylabel('户型')
plt.show()

# 去掉错误数据“南北”，因为爬虫过程中一些信息位置为空，导致“Direction”的特征出现在这里，需要清除或替换
df['Renovation'] = df.loc[(df['Renovation'] != '南北'), 'Renovation']
# 画幅设置
f, [ax1,ax2,ax3] = plt.subplots(1, 3, figsize=(20, 5))
sns.countplot(df['Renovation'], ax=ax1)
sns.barplot(x='Renovation', y='Price', data=df, ax=ax2)
sns.boxplot(x='Renovation', y='Price', data=df, ax=ax3)
plt.show()


# 由于存在个别类型错误，如简装和精装，特征值错位，故需要移除
df['Elevator'] = df.loc[(df['Elevator'] == '有电梯')|(df['Elevator'] == '无电梯'), 'Elevator']
# 根据楼层高度填补Elevator缺失值
df.loc[(df['Floor']>6)&(df['Elevator'].isnull()), 'Elevator'] = '有电梯'
df.loc[(df['Floor']<=6)&(df['Elevator'].isnull()), 'Elevator'] = '无电梯'

f, [ax1,ax2] = plt.subplots(1, 2, figsize=(20, 10))
sns.countplot(df['Elevator'], ax=ax1)
ax1.set_title('有无电梯数量对比',fontsize=15)
ax1.set_xlabel('是否有电梯')
ax1.set_ylabel('数量')
sns.barplot(x='Elevator', y='Price', data=df, ax=ax2)
ax2.set_title('有无电梯房价对比',fontsize=15)
ax2.set_xlabel('是否有电梯')
ax2.set_ylabel('总价')
plt.show()

#年份Year特征分析
grid = sns.FacetGrid(df, row='Elevator', col='Renovation', palette='seismic',size=4)
grid.map(plt.scatter, 'Year', 'Price')
grid.add_legend()

#楼层Floor特征分析
f, ax1= plt.subplots(figsize=(20,5))
sns.countplot(x='Floor', data=df, ax=ax1)
ax1.set_title('房屋户型',fontsize=15)
ax1.set_xlabel('数量')
ax1.set_ylabel('户型')
plt.show()

# 只考虑“室”和“厅”，将其它少数“房间”和“卫”移除
# 在正则表达式'^\d(.*?)\d.*?'中(.*?)为被析取的字符串对象
# df = df.loc[df['Layout'].str.extract('^\d(.*?)\d.*?') == '室']
# df['Layout_room_num'] = df['Layout'].str.extract('(^\d).*', expand=False).astype('int64')
# df['Layout_hall_num'] = df['Layout'].str.extract('^\d.*?(\d).*', expand=False).astype('int64')
# 以上为作者提供的源码，亲测有问题，修改
# 使用Dataframe.filter(regex = '^[^(室|厅)]')可以去除名称为'室'和'厅'的column
df = df[['Layout_room_num','Layout_hall_num']]=df['Layout'].str.extract('(\d+)室(\d+)厅',expand=False).astype('int64')
df = df.dropna()

# 按中位数对“Year”特征进行分箱
df['Year'] = pd.qcut(df['Year'],8).astype('object')

# 对“Direction”特征进行清洗，去除重复和错误的方向描述，保留以下四类合理的描述
d_list_one = ['东','西','南','北']
d_list_two = ['东西','东南','东北','西南','西北','南北']
d_list_three = ['东西南','东西北','东南北','西南北']
d_list_four = ['东西南北'] 

to_del = []
i = 0
test_df = df
for each in test_df['Direction']:
    if ((each in d_list_one) | (each in d_list_two) | (each in d_list_three) | (each in d_list_four)) == False:
        to_del.append(i)
        i += 1
for each in to_del:
    test_df.drop([each])