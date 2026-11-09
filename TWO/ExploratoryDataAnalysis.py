#Handle el data
import numpy as np
import pandas as pd

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

"""# **Read  data**

# **EDA**
"""
df = pd.read_csv(r'D:\\AI\\mater\\supermarket_sales.csv')#  student_performance.csv

# print(df.shape)
# print ("@" * 100)
# print(df.info())
# print ("@" * 100)

# print(df.describe())
# print ("@" * 100)
# # None
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #               Age  Study_Hours  Attendance     Midterm       Final         GPA
# # count  502.000000   497.000000  494.000000  502.000000  502.000000  502.000000
# # mean    21.007968     4.053722   80.884008   44.879283   44.042829    1.778327
# # std      2.002976     1.828612   11.759945   13.053217   13.914869    0.493319
# # min     18.000000     0.000000   45.200000    9.000000    0.000000    0.180000
# # 25%     19.000000     2.800000   73.900000   35.825000   34.400000    1.460000
# # 50%     21.000000     4.000000   81.550000   44.800000   44.050000    1.780000
# # 75%     23.000000     5.400000   88.875000   53.475000   52.800000    2.100000
# # max     24.000000     9.900000  100.000000   85.800000   90.300000    3.160000
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# """# **Check nulls and duplicates**"""

# print (df.isnull().sum())
# # Student_ID     0
# # Name           0
# # Gender         0
# # Age            0
# # Department     0
# # Study_Hours    5
# # Attendance     8
# # Midterm        0
# # Final          0
# # GPA            0
# # Passed         0
# # dtype: int64
# # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# print ("^" * 100)

# print (df.duplicated().sum())
# # 2

print ("^" * 100)

"""# **Cleaning**"""

df['Study_Hours'] = df['Study_Hours'].fillna(df['Study_Hours'].mean())
print(df['Study_Hours'])
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].median())
print(df['Attendance'] )

df = df.drop_duplicates()
print (df)
"""# **Sorting**"""

top_performance = df.sort_values(by='GPA', ascending=False).head()

top_performance

print(top_performance[['Name', 'Department', 'GPA']])

"""# **  Filtering**"""

top = df[(df['Passed']== 'Yes') & (df['GPA'] >= 2.5)]

print("the number of blablabla : ", len(top))

print(top[['Name','GPA','Department']])

"""# **Visualizations**"""

import matplotlib.pyplot as plt
import seaborn as sns

avg_gpa = df.groupby('Department')['GPA'].mean().sort_values(ascending=False)

plt.figure(figsize=(8,5))
plt.bar(avg_gpa.index, avg_gpa.values)

plt.title('Average GPA by Department')
plt.xlabel('Department')
plt.ylabel('BlaBlaBla')

plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['GPA'], bins=20, color='green', edgecolor='black', kde=True)
plt.xlabel('blablabla')
plt.ylabel('BlaBlaBla')
plt.title('Distribution of GPA')
plt.show()

plt.figure(figsize=(8,5))

sns.scatterplot(x='GPA', y='Study_Hours', data=df, hue='Passed', palette='Set2')

plt.show()

