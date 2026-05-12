# A DataFrame is a 2-dimensional labeled data structure with columns of
#  potentially different types (like a spreadsheet or SQL table).
import pandas as pd
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)