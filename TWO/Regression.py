import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
#python -m pip install scikit-learn


df = pd.read_csv(r'D:\\Programming\\AI\\mater\\house_data.csv')#  D:\Programming\AI\mater
print(df.head())
print ("="*50)
print(df.describe())
print("="*50)
print(df.info())

missing_values = df.isnull().sum()
print("Missing values in each column:" )
print(missing_values[missing_values > 0])

#calculate the  percentage of missing values in each column
# missing_percentage = (missing_values / len(df)) * 100
# print("Percentage of missing values in each column:")
# print(missing_percentage)
# house_data = df.drop(['Alley','FireplaceQu','PoolQC','Fence','MiscFeature'], axis=1)  
# # Drop the 'id' column
# print("="*50)
# print("Shape of the dataset after dropping columns:", house_data.shape)
# print("="*50)

# print("Columns in the dataset after dropping columns:")
# print(house_data.columns.tolist())
# print (house_data)

# missing_values = df.isnull().sum()
# print("Missing values in each column:" )
# print(missing_values[missing_values > 0])

# df['LotFrontage'] = df['LotFrontage'].fillna(df['LotFrontage'].mean())
# df['MasVnrType'] = df['MasVnrType'].fillna(df['MasVnrType'].mode()[0])
# df['MasVnrArea'] = df['MasVnrArea'].fillna(df['MasVnrArea'].mean())
# df['BsmtQual'] = df['BsmtQual'].fillna(df['BsmtQual'].mode()[0])
# df['BsmtCond'] = df['BsmtCond'].fillna(df['BsmtCond'].mode()[0])
# df['BsmtExposure'] = df['BsmtExposure'].fillna(df['BsmtExposure'].mode()[0])
# df['BsmtFinType1'] = df['BsmtFinType1'].fillna(df['BsmtFinType1'].mode()[0])
# df['BsmtFinType2'] = df['BsmtFinType2'].fillna(df['BsmtFinType2'].mode()[0])
# df['Electrical'] = df['Electrical'].fillna(df['Electrical'].mode()[0])
# df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])
# df['GarageFinish'] = df['GarageFinish'].fillna(df['GarageFinish'].mode()[0])
# df['GarageQual'] = df['GarageQual'].fillna(df['GarageQual'].mode()[0])
# df['GarageCond'] = df['GarageCond'].fillna(df['GarageCond'].mode()[0])
# df['SaleType'] = df['SaleType'].fillna(df['SaleType'].mode()[0])



categorical_cols = df.select_dtypes(include=['object']).columns
print("Categorical columns:", categorical_cols.tolist())
len(categorical_cols)
le= preprocessing.LabelEncoder()

cols=categorical_cols.tolist()
for col in cols:
    df[col] = le.fit_transform(df[col].astype(str))
    print(f"Encoded column: {le.classes_} for {col}")


x= df.drop(['SalePrice'], axis=1)
y=df['SalePrice']
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)

print("Shape of training data:", xtrain)
print("Shape of testing data:", xtest)

regressor = LinearRegression()
regressor.fit(xtrain, ytrain)
print("Model trained successfully.")
y_pred = regressor.predict(xtest)
mse = mean_squared_error(ytest, y_pred)
r2 = r2_score(ytest, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
print("Model evaluation completed.")
