
# pd.read_csv() reads a comma-separated values file into a DataFrame. 
# It’s the most common way to import tabular data.

import pandas as pd

df = pd.read_csv('curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv')
print(df)
# sample 