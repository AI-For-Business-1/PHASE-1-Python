# ============================================================
# Supermarket Sales - Full EDA (Fixed Version)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (9, 5)

# ============================================================
# 1. Read the data
# ============================================================

df = pd.read_csv('supermarket_sales.csv')

print("="*50)
print("COLUMNS IN YOUR FILE:")
print(df.columns.tolist())
print("="*50)
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe(include='all'))
print("\nFirst 5 rows:")
print(df.head())
print("\n")

# ============================================================
# 2. Check nulls & duplicates
# ============================================================

print("Null values:")
print(df.isnull().sum())
print("\nDuplicated rows:", df.duplicated().sum())
print("\n")

# ============================================================
# 3. Cleaning
# ============================================================

df = df.drop_duplicates()

# Uncomment if needed:
# df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
# df['Total'] = df['Total'].fillna(df['Total'].median())

print("After cleaning - Nulls:")
print(df.isnull().sum())
print("Duplicated rows after cleaning:", df.duplicated().sum())
print("\n")

# ============================================================
# 4. Sorting
# ============================================================

print("===== Top 5 Sales by Total =====")
top_sales = df.sort_values(by='Total', ascending=False).head()
print(top_sales)
print("\n")

# ============================================================
# 5. Filtering
# ============================================================

print("===== High Value + High Rating Transactions =====")
high_value = df[(df['Total'] >= 1000) & (df['Rating'] >= 7)]
print("Number of high value + high rating transactions:", len(high_value))
print(high_value.head(10))
print("\n")

# ============================================================
# 6. Visualizations
# ============================================================

# --- Average Total by City ---
if 'City' in df.columns:
    avg_city = df.groupby('City')['Total'].mean().sort_values(ascending=False)
    plt.figure()
    avg_city.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Total Sales by City')
    plt.ylabel('Average Total')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# --- Distribution of Total ---
plt.figure()
sns.histplot(df['Total'], bins=20, color='green', kde=True, edgecolor='black')
plt.title('Distribution of Total Sales')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# --- Average Rating by Product line ---
product_col = None
for col in df.columns:
    if 'product' in col.lower():
        product_col = col
        break

if product_col:
    avg_rating = df.groupby(product_col)['Rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10,5))
    sns.barplot(x=avg_rating.index, y=avg_rating.values, palette='viridis')
    plt.title('Average Rating by Product Line')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# --- Quantity vs Total ---
if 'Quantity' in df.columns:
    plt.figure()
    sns.scatterplot(data=df, x='Quantity', y='Total', hue='Payment' if 'Payment' in df.columns else None, palette='Set2')
    plt.title('Quantity vs Total Sales')
    plt.tight_layout()
    plt.show()

# --- Transactions by Branch ---
if 'Branch' in df.columns:
    plt.figure()
    sns.countplot(data=df, x='Branch', palette='pastel', order=df['Branch'].value_counts().index)
    plt.title('Number of Transactions by Branch')
    plt.tight_layout()
    plt.show()

print("===== Done! =====")