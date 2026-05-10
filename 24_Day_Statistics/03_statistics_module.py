# Python’s built-in statistics module provides functions for calculating 
# numeric statistical measures like mean(), median(), mode(), stdev(), 
# and variance(). It works with iterable data (lists, tuples).

import statistics as stats

exam_scores = [55, 67, 89, 45, 78, 92, 85, 67]

# Using statistics module functions
mean_score = stats.mean(exam_scores)
median_score = stats.median(exam_scores)
mode_score = stats.mode(exam_scores)  # most common
std_dev = stats.stdev(exam_scores)    # sample standard deviation

print(f"Mean: {mean_score}")          # Mean: 72.25
print(f"Median: {median_score}")      # Median: 72.5
print(f"Mode: {mode_score}")          # Mode: 67
print(f"Std Dev: {std_dev:.2f}")      # Std Dev: 16.06