# D:\AI\mater
import pandas as pd
import numpy as np

# dfsalary = pd.read_csv(r"D:\\AI\\mater\\Salary_Data.csv")
# print(dfsalary)
# print(dfsalary.head())
# print(dfsalary.tail())
# # print(dfsalary.describe())
# # print(dfsalary.info())
# # print(dfsalary.shape)
# # print(dfsalary.columns)
# # print(dfsalary.dtypes)


train = pd.read_csv(r"D:\\AI\\mater\\train.csv")
print(train)
print(train.head())
print(train.info())

print(train.isnull())
print(train.isnull().sum())

