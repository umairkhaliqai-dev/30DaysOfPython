# In statistics, data are individual pieces of information—facts or 
# numbers—collected for analysis. 
# Data can be qualitative (categories, e.g., colors, yes/no) 
# or quantitative (numerical values, e.g., heights, scores).
#  Python often stores data in lists, tuples, or arrays.

# Different types of data in Python
# Quantitative (numerical) data
scores = [85, 92, 78, 90, 88]  # continuous-like

# Qualitative (categorical) data
grades = ['A', 'A-', 'B+', 'A-', 'B+']

# Converting qualitative to quantitative for analysis
grade_to_points = {'A': 4.0, 'A-': 3.7, 'B+': 3.3}
points = [grade_to_points[g] for g in grades]

print(f"Grades: {grades}")
print(f"Numeric points: {points}")  # [4.0, 3.7, 3.3, 3.7, 3.3]