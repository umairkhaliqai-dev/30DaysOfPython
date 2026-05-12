# np.linspace() (from NumPy) creates evenly spaced numbers over a specified range, 
# which can be used as data for a Series.
import numpy as np
import pandas as pd
data = np.linspace(0, 10, 5)   # 5 numbers from 0 to 10 inclusive
series = pd.Series(data)
print(series)
