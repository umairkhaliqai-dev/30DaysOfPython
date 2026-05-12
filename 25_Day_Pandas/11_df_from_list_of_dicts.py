# Each dictionary represents one row. 
# Keys common across dictionaries become column names.
import pandas as pd 
data = [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}]
df = pd.DataFrame(data)
print(df)