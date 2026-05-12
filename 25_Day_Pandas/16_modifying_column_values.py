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

df['Height'] = df['Height'] * 0.01
print(df)
# Name	Country	City	Weight	Height
# 0	Asabeneh	Finland	Helsinki	74	1.73
# 1	David	UK	London	78	1.75
# 2	John	Sweden	Stockholm	69	1.69

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()
print()

df['BMI'] = bmi
print(df)
#  BMI formula: weight ÷ (height × height) or weight ÷ height²

#  Height is squared because BMI is measured in kg/m² (kilograms per square meter).