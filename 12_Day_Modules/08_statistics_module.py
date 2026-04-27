# The statistics module provides functions for calculating mathematical statistics of numeric data — mean, median, mode, and more.
from statistics import mean, median, mode, stdev

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

print(mean(data))    # → 5.2
print(median(data))  # → 5.0
print(mode(data))    # → 2 (most frequent)
print(stdev(data))   # → 2.44 (std deviation)