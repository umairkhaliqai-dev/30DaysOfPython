# You can create a Series where all values are the same (constant) across all indices.
import pandas as pd
const_series = pd.Series(5, index=range(4))
print(const_series)   # 5,5,5,5