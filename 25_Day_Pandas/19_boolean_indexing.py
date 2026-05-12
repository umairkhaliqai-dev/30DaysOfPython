# Explanation: Filter rows based on a condition (True/False mask). Only rows where condition is True are kept.


# # adults = df[df['Age'] >= 18]   # Rows where Age >= 18
# # name_start_A = df[df['Name'].str.startswith('A')]

import pandas as pd

# Sample data
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Amy', 'David'],
    'Age': [25, 16, 30, 12, 19],
    'City': ['NYC', 'LA', 'Chicago', 'Boston', 'Seattle']
})

print("Original DataFrame:")
print(df)
print()

# Filter 1: Adults (Age >= 18)
adults = df[df['Age'] >= 18]
print("Adults (Age >= 18):")
print(adults)
print()

# Filter 2: Names starting with 'A'
name_start_A = df[df['Name'].str.startswith('A')]
print("Names starting with 'A':")
print(name_start_A)