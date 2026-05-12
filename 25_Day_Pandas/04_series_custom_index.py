# You can assign meaningful labels as the index using the index parameter.
import pandas as pd
data = [85, 90, 78]
index_labels = ['Math', 'Science', 'English']
marks = pd.Series(data, index=index_labels)
print(marks)