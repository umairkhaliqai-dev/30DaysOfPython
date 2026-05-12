import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
# Name	Country	City
# 0	Asabeneh	Finland	Helsinki
# 1	David	UK	London
# 2	John	Sweden	Stockholm

## Let's add a weight column in the DataFrame

weights = [74, 78, 69]
df['Weight'] = weights
print(df)

# Name	Country	City	Weight
# 0	Asabeneh	Finland	Helsinki	74
# 1	David	UK	London	78
# 2	John	Sweden	Stockholm	69

heights = [173, 175, 169]
df['Height'] = heights
print(df)
