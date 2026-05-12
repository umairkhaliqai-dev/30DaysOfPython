import pandas as pd

# Create sample data
data = {
    'Name': ['John', 'Sarah', 'Mike', 'Lisa', 'David'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'Salary': [50000, 45000, 60000, 48000, 52000],
    'Years_Experience': [3, 7, 8, 2, 6]
}

# Save to CSV
df_original = pd.DataFrame(data)
df_original.to_csv('employees.csv', index=False)
print("CSV file created!")
print()


df_read = pd.read_csv('employees.csv')
print(df_read)
print()

print()
# Load CSV into DataFrame
df = pd.read_csv('employees.csv')
print("File loaded successfully!")

print()
# Check first 5 rows
print(df.head())
print('0')


# Check last 5 rows
print(df.tail())
print('1')
# Check total rows and columns
print(df.shape)
print('2')
# Check column names
print(df.columns)
print('3')
# Check data types
print(df.dtypes)
print('4')
# Check summary info
print(df.info())
print('5')

print()
print('Next')
print()
# Add new column 'Bonus' = Salary × 0.10
df['Bonus'] = df['Salary'] * 0.10
print(df)
print()

print()
print('next # 1')
print()
# Increase all salaries by 5%
df['Salary'] = df['Salary'] * 1.05
print(df)

print()
# Keep only rows where Years_Experience >= 5
filtered_df = df[df['Years_Experience'] >= 5]
print(filtered_df)
print()

print()
# Average salary of filtered DataFrame
average_salary = filtered_df['Salary'].mean()
print("Average salary (5+ years exp):", average_salary)
