#  A Series is a one-dimensional array-like object. If index is not specified, 
# it uses default integer index (0,1,2…).
import pandas as pd
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)