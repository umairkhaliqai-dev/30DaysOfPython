# Explanation: Use dtypes attribute to see the data type of each column 
# (int64, float64, object, etc.).

# Example: print(df.dtypes)
print()

import numpy as np
import pandas as pd

# Different integer types
small_num = np.int8(100)      # Uses 1 byte
big_num = np.int64(100)       # Uses 8 bytes

# In a DataFrame
df = pd.DataFrame({
    'age': [25, 30, 35],           # int64 (default)
    'salary': [50000, 60000, 70000], # int64
    'rating': [4.5, 3.8, 4.9],     # float64
    'name': ['Alice', 'Bob', 'Charlie']  # object (string)
})

print(df.dtypes)
# age         int64
# salary      int64
# rating     float64
# name        object