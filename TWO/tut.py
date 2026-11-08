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



# Concatenate
pd.concat([df1, df2], axis=0)            # stack rows
pd.concat([df1, df2], axis=1)            # side by side

# Merge (SQL-style joins)
pd.merge(df1, df2, on='key')
pd.merge(df1, df2, left_on='id', right_on='user_id', how='left')
pd.merge(df1, df2, on='key', how='inner')   # outer, left, right, inner

# Join (on index)
df1.join(df2, how='left')



# Pivot
df.pivot(index='Date', columns='City', values='Sales')

# Melt (wide → long)
pd.melt(df, id_vars=['Name'], value_vars=['Age', 'Salary'])

# Stack / Unstack
df.stack()
df.unstack()

# Crosstab
pd.crosstab(df['City'], df['Senior'])



# Apply on Series
df['Name'].apply(str.upper)
df['Age'].apply(lambda x: x + 1)

# Apply on DataFrame (row or column wise)
df.apply(np.mean, axis=0)                # column means
df.apply(lambda row: row['Salary'] / row['Age'], axis=1)

# Applymap (element-wise, older) / map (newer)
df[['Age', 'Salary']].map(lambda x: x * 2)

# Vectorized string methods
df['Name'].str.lower()
df['Name'].str.contains('a')
df['Name'].str.replace('Alice', 'Alicia')



df['Salary'].rolling(window=3).mean()
df['Salary'].expanding().sum()
df['Salary'].ewm(span=3).mean()          # exponential weighted


df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df.resample('M').mean()                  # monthly
df.resample('W').sum()                   # weekly
df.shift(1)                              # lag
df.diff()                                # difference



df.rename(columns={'Name': 'FullName'})
df.rename(index={0: 'first'})
df.set_index('Name')
df.reset_index()
df.reindex([...])                        # change index order

df.replace({'NY': 'New York'})
df.replace(0, np.nan)

df.astype({'Age': 'int32', 'Salary': 'float'})
df.convert_dtypes()                      # best possible dtypes

df.sample(n=2)                           # random sample
df.nlargest(3, 'Salary')
df.nsmallest(2, 'Age')