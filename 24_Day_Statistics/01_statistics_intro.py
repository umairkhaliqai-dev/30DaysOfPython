# Using Python programming language to perform statistical operations—like mean,
#  median, variance, correlation—on datasets. 
# Python provides built-in tools and external libraries (e.g., statistics, numpy, pandas) 
# to summarize and interpret data.
# Simple statistical analysis with plain Python
data = [12, 15, 14, 10, 18, 20, 22, 19]

mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)

print(f"Mean: {mean:.2f}")          # Mean: 16.25
print(f"Variance: {variance:.2f}")  # Variance: 13.69
print()
print()
# Statistics is the branch of mathematics that deals with collecting, 
# organizing, analyzing, interpreting, and presenting data. 
# In Python, statistical concepts include central tendency (mean, median, mode), 
# dispersion (range, variance, standard deviation), and correlation.

# Basic statistical measures manually
ages = [23, 25, 22, 26, 24, 27, 30, 28]

# Central tendency
mean_age = sum(ages) / len(ages)
sorted_ages = sorted(ages)
n = len(sorted_ages)
median_age = (sorted_ages[n//2] if n % 2 != 0 
              else (sorted_ages[n//2 - 1] + sorted_ages[n//2]) / 2)

# Dispersion
range_age = max(ages) - min(ages)

print(f"Mean: {mean_age}, Median: {median_age}, Range: {range_age}")
# Mean: 25.625, Median: 25.5, Range: 8