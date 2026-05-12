# When a dictionary is used to create a Series, the dictionary keys 
# become the index and values become the data.
import pandas as pd
data_dict = {'a': 1, 'b': 2, 'c': 3}
series = pd.Series(data_dict)
print(series)