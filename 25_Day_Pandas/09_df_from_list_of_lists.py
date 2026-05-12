# Keys become column names, and values (which are lists) become column data. All lists must have the same length.
import pandas as pd 
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)