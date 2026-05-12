# Explanation: Methods to understand the structure and 
# content of a DataFrame, such as .head(), .tail(), .info(), .describe().

# print(df.head())     # First 5 rows
# print(df.info())     # Data types and non-null counts
# print(df.describe()) # Summary statistics for numeric columns

### Key Points from Data Exploration:

 # df.head(n) - First n rows (default 5)

# df.tail(n) - Last n rows (default 5)

# df.shape - Number of (rows, columns)

# df.columns - List of column names

# df['column_name'] - Extract a single column as a Series

# df.describe() - Statistical summary (count, mean, std, min, max, quartiles)

# df.info() - Dataset information (data types, non-null counts, memory)
import pandas as pd

df = pd.DataFrame({
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Male'],
    'Height': [73.8, 68.7, 65.1, 63.5, 70.2],
    'Weight': [241.8, 162.3, 145.6, 128.4, 190.5]
})

print(df.head(3))