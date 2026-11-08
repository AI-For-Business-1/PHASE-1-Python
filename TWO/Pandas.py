# DataFrame in Pandas 🐼

# A DataFrame in Pandas is a 2-dimensional
#  data structure that stores data in rows and columns,
#  just like an Excel spreadsheet or a database table.

## 1. What does a DataFrame look like?


# ### Students DataFrame

# | Name  | Age | Grade |
# | ----- | --- | ----- |
# | Ahmed | 20  | 90    |
# | Sara  | 19  | 85    |
# | Omar  | 21  | 95    |

# 3 rows × 3 columns

# - Rows: Each row represents one student.
# - Columns: Each column represents a type of information, such as name, age, or grade.
# - Index: Labels used to identify rows. By default, Pandas uses `0, 1, 2, ...`.

## 2. How to create a DataFrame

import  pandas as pd
 
# Then create a DataFrame using a dictionary:

data = {    "Name": ["Ahmed", "Sara", "Omar"],  
            "Age": [20, 19, 21],   
           "Grade": [90, 85, 95]}
df = pd.DataFrame(data)

print(df)

# Output:

# ```
#     Name  Age  Grade
# 0  Ahmed   20     90
# 1   Sara   19     85
# 2   Omar   21     95
# ```

# Explanation:

# - `pd` is the common alias for Pandas.
# - `pd.DataFrame(data)` converts the dictionary into a DataFrame.
# - `df` is the variable that stores the DataFrame.

# ## 3. Common DataFrame operations

# Here are the most important operations to learn first.

# View the first rows


## 4. DataFrame vs Series

# | Feature    | DataFrame        | Series               |
# | ---------- | ---------------- | -------------------- |
# | Dimensions | 2D               | 1D                   |
# | Structure  | Rows and columns | One labeled sequence |
# | Example    | `df`             | `df["Name"]`         |
# | Similar to | Excel table      | One Excel column     |

## 5. Why do we use DataFrames?

# DataFrames help us:

# - Organize large amounts of data.
# - Filter and sort information.
# - Calculate statistics such as averages.
# - Handle missing values.
# - Read and analyze CSV and Excel files.

# For example, to calculate the average grade:


# Remember: A DataFrame is one of the main tools in Pandas for working with structured data.
