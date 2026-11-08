import pandas as pd
import numpy as np

# From dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['NY', 'LA', 'Chicago', 'NY'],
    'Salary': [70000, 80000, 90000, 75000]
})

# From list of lists
df2 = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])

# From NumPy array
df3 = pd.DataFrame(np.random.randn(5, 3), columns=['X', 'Y', 'Z'])

# Empty DataFrame
df_empty = pd.DataFrame(columns=['A', 'B', 'C'])


df.head()          # first 5 rows
df.tail(3)         # last 3 rows
df.shape           # (rows, columns)
df.info()          # dtypes + non-null counts
df.describe()      # statistical summary (numeric)
df.columns         # column names
df.index           # index
df.dtypes          # data types
df.memory_usage()  # memory usage



# Select columns
df['Name']                 # Series
df[['Name', 'Age']]        # DataFrame

# Select rows by position
df.iloc[0]                 # first row
df.iloc[0:3]               # first 3 rows
df.iloc[0, 1]              # single value
df.iloc[:, 0:2]            # first two columns

# Select by label
df.loc[0]                  # row with index 0
df.loc[0:2, 'Name':'City'] # rows + columns by label
df.loc[df['Age'] > 30]     # boolean indexing

# Single value
df.at[0, 'Name']           # fast label-based
df.iat[0, 0]               # fast position-based


df[df['Age'] > 30]
df[(df['Age'] > 25) & (df['City'] == 'NY')]
df[df['City'].isin(['NY', 'LA'])]
df[df['Name'].str.startswith('A')]
df.query('Age > 30 and City == "NY"')   # nice string syntax


df.sort_values('Age')                    # ascending
df.sort_values('Age', ascending=False)
df.sort_values(['City', 'Age'])          # multiple columns
df.sort_index()                          # sort by index


df['Bonus'] = df['Salary'] * 0.1
df['Senior'] = df['Age'] > 30
df.insert(1, 'ID', range(1, len(df)+1))  # insert at position

# Using assign (returns new DataFrame)
df = df.assign(Tax = df['Salary'] * 0.2)

df.drop(columns=['Bonus'])               # drop columns
df.drop(index=[0, 2])                    # drop rows by index
df.drop(['Bonus', 'Senior'], axis=1, inplace=True)

df.dropna()                              # drop rows with any NaN
df.dropna(subset=['Age'])                # only if Age is NaN
df.dropna(how='all')                     # only if all values are NaN
df.drop_duplicates()                     # remove duplicate rows
df.drop_duplicates(subset=['City'])      # based on specific columns



df.isna() / df.isnull()                  # boolean mask
df.notna()
df.fillna(0)                             # fill with value
df.fillna({'Age': 30, 'Salary': df['Salary'].mean()})
df.fillna(method='ffill')                # forward fill
df.interpolate()                         # linear interpolation


df.groupby('City')['Salary'].mean()
df.groupby('City').agg({
    'Age': 'mean',
    'Salary': ['sum', 'mean', 'max']
})

df.groupby('City').size()                # count rows
df.groupby('City').count()
df.groupby('City').first()
df.groupby('City').nth(1)                # 2nd row of each group

# Transform (keeps original shape)
df['Avg_Salary_City'] = df.groupby('City')['Salary'].transform('mean')



df.duplicated()
df.value_counts()                        # for Series or DataFrame



df.to_csv('data.csv', index=False)
df.to_excel('data.xlsx', index=False)
df.to_json('data.json', orient='records')
df.to_parquet('data.parquet')

pd.read_csv('data.csv')
pd.read_excel('data.xlsx')
pd.read_json('data.json')
pd.read_parquet('data.parquet')






















































